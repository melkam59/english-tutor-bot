from dataclasses import dataclass
from typing import Any

from app.application.interactors.onboarding.profile import ProfileInteractor
from app.domain.user import User
from app.presentation.telegram.callbacks.settings import SettingsField
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.profile import ProfilePresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class ProfileFlow(BaseFlow):
    user: User
    interactor: ProfileInteractor
    presenter: ProfilePresenter
    renderer: Renderer

    async def show_profile(self) -> Any:
        return await self.renderer.apply(self.presenter.profile(user=self.user))

    async def show_settings(self) -> Any:
        return await self.renderer.apply(self.presenter.settings())

    async def edit_field(self, field: SettingsField) -> Any:
        # TODO(M1): reuse the onboarding keyboards, save through ProfileInteractor
        return await self.renderer.apply(self.presenter.not_implemented())
