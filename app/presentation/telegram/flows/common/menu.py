from dataclasses import dataclass
from typing import Any

from app.domain.user import User
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.menu import CommonMenuPresenter
from app.presentation.telegram.presenters.common.onboarding import OnboardingPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class CommonMenuFlow(BaseFlow):
    user: User
    presenter: CommonMenuPresenter
    onboarding_presenter: OnboardingPresenter
    renderer: Renderer

    async def start(self) -> Any:
        if not self.user.is_onboarded:
            # TODO(M1): set OnboardingSG.native_language
            return await self.renderer.apply(
                self.onboarding_presenter.ask_native_language(user=self.user)
            )
        return await self.renderer.apply(self.presenter.greeting(user=self.user))

    async def help(self) -> Any:
        return await self.renderer.apply(self.presenter.help())
