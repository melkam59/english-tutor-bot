# Architecture

## Processes
| Process | Entrypoint | Role |
|---------|-----------|------|
| bot | `python -m app` | aiogram dispatcher inside a FastAPI app: webhook endpoint (secret-token protected) or polling, plus healthcheck |
| worker | `python -m app.worker` | periodic background jobs: vocabulary revision reminders, subscription expiry |
| postgres | | persistent data |
| redis | | FSM storage, cache, daily counters, throttling, update de-duplication |

## Request pipeline
```
Telegram update
  → middlewares (logging → dedup → throttling → ban)
  → Handler      parses the update, one call into a Flow
  → Flow         orchestrates interactors + presenters
  → Interactor   use-case logic, knows nothing about Telegram
  → Presenter    builds a View (text + keyboard)
  → Renderer     the only place that calls the Bot API
```
Application errors (`LimitError`, `LLMError`, `SpeechError`, ...) bubble up to
`handlers/extra/errors.py`, which answers with a friendly localized message.
Dependencies are wired with dishka (`app/providers/`), resolved via `FromDishka[...]`.

## Layers
```
app/
├── domain/                  SQLAlchemy entities + enums
│   ├── user, conversation, message, user_mistake, vocabulary_item, lesson, usage_record
│   └── enums/               EnglishLevel (A1–C1), PracticeMode, RolePlayScenario, MistakeCategory, ...
├── application/             framework-agnostic core
│   ├── interactors/         onboarding, assessment, tutor, lessons, vocabulary, progress,
│   │                        subscription, limits, voice, admin
│   ├── services/            PromptBuilder, ConversationContextService, AccessPolicy,
│   │                        CostEstimator, AssessmentBank, spaced_repetition
│   ├── ports/               protocols: repositories, llm, speech, limits, payments, telegram
│   ├── models/              config (env + yaml), dto, FSM state models
│   ├── errors/              limits / llm / speech error hierarchy
│   └── storage/keys/        typed Redis keys (daily counters, throttle, dedup)
├── infrastructure/          port implementations
│   ├── postgres/            UoW, SqlRepositoryHelper, repositories
│   ├── llm/                 openai / anthropic / gemini gateways + factory
│   ├── speech/              STT / TTS + ffmpeg converter
│   ├── redis/               cache, key-value repository, usage counters, throttler
│   └── telegram/            lifespan, file download, broadcaster
├── presentation/
│   ├── telegram/            handlers, flows, presenters, keyboards, callbacks, states, middlewares
│   └── fastapi/             webhook endpoint + healthcheck
├── providers/               dishka providers
├── runners/                 polling / webhook lifespans
└── worker/                  scheduler + background tasks
assets/
├── commands.yml             bot command menu
├── assessment.yml           level test question bank
├── messages/<locale>/*.ftl  interface texts (Project Fluent)
└── prompts/*.md             LLM prompt templates
```

## Key design decisions
- **LLM provider isolation** — interactors depend on `LLMGateway`; the concrete provider is
  chosen from `LLM_PROVIDER` in `infrastructure/llm/factory.py`.
- **Structured tutor output** — the LLM answers in a JSON schema (`TutorReply`: corrected text,
  corrections with category + native-language explanation, better phrases, reply with a
  follow-up question). Corrections are stored as `UserMistake` rows and fed back into prompts.
- **Limited context** — only the last `LLM_CONTEXT_MESSAGES` messages plus a rolling
  `Conversation.summary` are sent; older messages are folded into the summary with a cheaper
  model after `LLM_SUMMARIZE_AFTER_MESSAGES`.
- **Cost control** — daily quotas per plan in Redis, input/voice length limits, output token cap,
  per-user throttling, every request logged to `usage_records` with estimated cost.
- **Subscriptions** — `AccessPolicy` is a pure feature matrix; `SubscriptionInteractor` flips the
  status, a real provider (Telegram Stars) plugs in through `PaymentsGateway`.
- **Enums are stored as VARCHAR** (non-native), so adding a member needs no migration.
- **Interface locale vs native language** — `User.language` drives the bot UI (Fluent files),
  `User.native_language` is what the LLM uses for explanations.
