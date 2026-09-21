# English Tutor Bot

AI-powered Telegram bot that helps users learn and practice English: text and voice
conversation with corrections, level assessment, personalized lessons, mistake tracking,
vocabulary trainer with spaced repetition, progress statistics, Free / Premium plans and
admin commands.

> **Status: working demo slice.** Onboarding, AI conversation with corrections explained in
> the user's native language, conversation memory, mistake tracking, daily limits with token
> cost logging and `/progress` work end to end (DeepSeek by default). Everything else is
> stubbed with `TODO(M1..M5)` markers, see [docs/ROADMAP.md](docs/ROADMAP.md).

Built on top of [wakaree/aiogram_bot_template](https://github.com/wakaree/aiogram_bot_template) (MIT).

## ⚙️ System dependencies
- Python 3.12
- Docker + docker compose
- make
- [uv](https://docs.astral.sh/uv/)
- ffmpeg (only outside Docker, for voice messages)

## 🐳 Quick start with Docker Compose
```bash
cp .env.dist .env                                   # fill in tokens and API keys
cp docker-compose.example.yml docker-compose.yml
make app-build
make app-run                                        # postgres, redis, bot, worker
make app-logs
```
Migrations are applied automatically on bot start (`scripts/run-bot.sh`).

## 🔧 Development
```bash
uv sync                 # install dependencies
make app-run-db         # postgres + redis only (set POSTGRES_HOST/REDIS_HOST=localhost in .env)
make migrate            # apply migrations
make run                # bot (polling unless TELEGRAM_USE_WEBHOOK=True)
make run-worker         # background worker
make test               # pytest
make lint               # ruff + mypy
make migration message=add_something   # autogenerate a migration
```
Find the next thing to implement: `grep -rn "TODO(M1" app`.

## 🤖 Commands
| User | Admin (only in `COMMON_ADMIN_CHAT_ID`) |
|------|-------|
| `/start` `/help` `/profile` `/practice` `/lesson` `/vocabulary` `/progress` `/settings` `/subscription` | `/stats` `/ban <id>` `/unban <id>` `/premium <id> <days>` `/unpremium <id>` `/broadcast <text>` |

Any non-command text or voice message goes to the AI tutor (`handlers/main/chat.py`).

## 🧠 LLM configuration
The provider is selected with `LLM_PROVIDER` (`deepseek` / `openai` / `anthropic` / `gemini`) plus
`LLM_API_KEY`, `LLM_MODEL` and `LLM_SUMMARY_MODEL`. Business logic only depends on the
`LLMGateway` port, so a new provider is one class in `app/infrastructure/llm/` registered in
`factory.py`. Token and cost controls (`LLM_MAX_OUTPUT_TOKENS`, `LLM_CONTEXT_MESSAGES`,
`LLM_SUMMARIZE_AFTER_MESSAGES`, `LIMITS_*`, prices per 1M tokens) are described in `.env.dist`.

## 📚 Documentation
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — layers, request pipeline, where things live
- [docs/ROADMAP.md](docs/ROADMAP.md) — milestones mapped to files and acceptance criteria
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) — VPS deployment, webhook, backups

## 📝 License
MIT, see [LICENSE](LICENSE).
