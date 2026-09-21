"""
Background worker entrypoint: ``python -m app.worker`` (``worker`` service in docker-compose).

Runs periodic jobs next to the bot process so long-running work never blocks update handling.
"""

import asyncio
import logging
from contextlib import suppress
from typing import Final

from dishka import AsyncContainer

from app.providers.container import create_container
from app.utils.logging import setup_logger
from app.worker.scheduler import Scheduler
from app.worker.tasks.subscriptions import expire_subscriptions
from app.worker.tasks.vocabulary import send_vocabulary_reminders

logger: Final[logging.Logger] = logging.getLogger(name=__name__)


async def main() -> None:
    setup_logger()
    container: AsyncContainer = create_container()
    scheduler: Scheduler = Scheduler(container=container)
    scheduler.every(seconds=60 * 60, task=send_vocabulary_reminders)
    scheduler.every(seconds=10 * 60, task=expire_subscriptions)
    try:
        await scheduler.run_forever()
    finally:
        await container.close()


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
