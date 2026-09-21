from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from typing import Awaitable, Callable, Final

from dishka import AsyncContainer

logger: Final[logging.Logger] = logging.getLogger(name=__name__)

Task = Callable[[AsyncContainer], Awaitable[None]]


@dataclass
class Scheduler:
    """
    Minimal asyncio interval scheduler. Swap for taskiq / arq when jobs need
    persistence, retries or several worker replicas.
    """

    container: AsyncContainer
    _jobs: list[tuple[int, Task]] = field(default_factory=list)

    def every(self, seconds: int, task: Task) -> None:
        self._jobs.append((seconds, task))

    async def _loop(self, seconds: int, task: Task) -> None:
        while True:
            try:
                await task(self.container)
            except NotImplementedError:
                logger.warning("Task %s is not implemented yet", task.__name__)
            except Exception:
                logger.exception("Background task %s failed", task.__name__)
            await asyncio.sleep(seconds)

    async def run_forever(self) -> None:
        await asyncio.gather(*(self._loop(seconds, task) for seconds, task in self._jobs))
