from dataclasses import dataclass
from typing import Any

from app.application.interactors.admin.broadcast import BroadcastInteractor
from app.application.interactors.admin.stats import AdminStatsInteractor
from app.application.interactors.admin.users import AdminUsersInteractor
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.admin.panel import AdminPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class AdminFlow(BaseFlow):
    stats_interactor: AdminStatsInteractor
    users_interactor: AdminUsersInteractor
    broadcast_interactor: BroadcastInteractor
    presenter: AdminPresenter
    renderer: Renderer

    async def invalid_arguments(self) -> Any:
        return await self.renderer.apply(self.presenter.invalid_arguments())

    async def show_stats(self) -> Any:
        # TODO(M4)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def ban(self, user_id: int) -> Any:
        # TODO(M4)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def unban(self, user_id: int) -> Any:
        # TODO(M4)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def grant_premium(self, user_id: int, days: int) -> Any:
        # TODO(M4)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def revoke_premium(self, user_id: int) -> Any:
        # TODO(M4)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def broadcast(self, text: str) -> Any:
        # TODO(M4): confirmation step through BroadcastSG before sending
        return await self.renderer.apply(self.presenter.not_implemented())
