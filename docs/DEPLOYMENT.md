# Deployment (VPS: Hetzner / DigitalOcean / AWS / GCP)

## 1. Server
Install Docker + the compose plugin, clone the repository, then:
```bash
cp .env.dist .env && chmod 600 .env
cp docker-compose.example.yml docker-compose.yml
```
In production remove the `ports:` sections of `postgres` and `redis` in `docker-compose.yml`
so they are reachable only inside the Docker network, and use strong passwords.

## 2. Configuration
- `TELEGRAM_BOT_TOKEN` — from @BotFather
- `COMMON_ADMIN_CHAT_ID` — Telegram user ID of the admin
- `LLM_*`, `SPEECH_*` — provider, API keys, models, prices
- `LIMITS_*` — daily quotas and input limits

Secrets live only in `.env` (git-ignored) and are wrapped in `SecretStr`, so they never
appear in logs.

## 3. Webhook
```
TELEGRAM_USE_WEBHOOK=True
TELEGRAM_WEBHOOK_PATH=/telegram
TELEGRAM_WEBHOOK_SECRET=<long random string>     # checked on every request
SERVER_URL=https://bot.example.com
SERVER_PORT=8080
```
Put nginx (or Caddy) with a TLS certificate in front of the bot and proxy
`https://bot.example.com/telegram` to `127.0.0.1:8080` — see `nginx/caller.example.conf`.
The bot registers the webhook itself on startup. With `TELEGRAM_USE_WEBHOOK=False` it uses
long polling and needs no domain.

## 4. Start
```bash
make app-build && make app-run     # migrations run automatically
make app-logs
```
Update: `git pull && make app-build && make app-run`.

## 5. Backups
```bash
# dump (add to cron, copy off the server)
docker compose exec -T postgres sh -c 'pg_dump -U "$POSTGRES_USER" -Fc "$POSTGRES_DB"' \
  > backup_$(date +%F).dump
# restore
docker compose exec -T postgres sh -c 'pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" --clean' \
  < backup.dump
```
Redis only holds FSM state, counters and cache and does not need backups.

## 6. Monitoring (optional)
`COMMON_SENTRY_DSN` for error tracking; the FastAPI app exposes a healthcheck endpoint
(`app/presentation/fastapi/healthcheck.py`) for uptime checks.
