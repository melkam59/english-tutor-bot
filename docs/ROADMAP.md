# Roadmap

Every stub in the code is tagged `TODO(Mx)`. List them with `grep -rn "TODO(M2" app`.

## M1 — Project setup and basic bot
Done by the scaffold: structure, Docker, PostgreSQL schema + migration, user registration on
first update, all commands registered, `/help`, `/profile`, `/settings` screens.
- [ ] Onboarding chain: `flows/common/onboarding.py`, `interactors/onboarding/profile.py`
- [ ] Settings editing: `flows/common/profile.py`
- [ ] Localized enum titles in `/profile`

## M2 — LLM tutor
- [ ] Provider gateway: `infrastructure/llm/<provider>.py`
- [ ] Prompts: `services/prompts.py`, `assets/prompts/`
- [ ] Conversation: `interactors/tutor/conversation.py`, `flows/common/practice.py`
- [ ] Context + summarization: `services/context.py`
- [ ] Repositories: conversations, messages
- [ ] Limits: `interactors/limits/usage.py`, `infrastructure/redis/limits.py`, throttling middleware

## M3 — Learning features
- [ ] Assessment: `assets/assessment.yml`, `services/assessment_bank.py`, `interactors/assessment/`
- [ ] Lessons: `interactors/lessons/personalized.py`, `flows/common/lesson.py`
- [ ] Mistakes repository + usage in prompts
- [ ] Vocabulary: `interactors/vocabulary/trainer.py`, `services/spaced_repetition.py`, reminders task
- [ ] Progress: `interactors/progress/summary.py`

## M4 — Voice and subscriptions
- [ ] Voice: `interactors/voice/transcription.py`, `infrastructure/speech/`, `infrastructure/telegram/files.py`
- [ ] Premium logic: `services/access.py`, `interactors/subscription/manage.py`, expiry task
- [ ] Usage + cost: `services/cost.py`, usage repository
- [ ] Admin: `interactors/admin/`, `flows/admin/panel.py`, ban middleware, broadcaster

## M5 — Testing and deployment
- [ ] Un-skip and implement `tests/unit/*`, add `tests/integration/*`
- [ ] Update de-duplication + structured logging middlewares, catch-all error handler, Sentry
- [ ] Production deployment following `docs/DEPLOYMENT.md`

## Acceptance criteria → where it is covered
| Criterion | Location |
|-----------|----------|
| Register and configure a learning profile | `UserProvider`, onboarding flow |
| Hold a conversation, correct and explain | `TutorConversationInteractor`, `PracticePresenter.tutor_reply` |
| Context is preserved | `ConversationContextService` |
| Mistakes and vocabulary stored | `user_mistakes`, `vocabulary_items` |
| Personalized exercises | `LessonsInteractor` |
| Voice messages | `VoiceInteractor` |
| Daily limits | `UsageLimitsInteractor` |
| Admin statistics | `AdminStatsInteractor` |
| Docker Compose / migrations / tests / docs | `docker-compose.example.yml`, `migrations/`, `tests/`, `docs/` |
