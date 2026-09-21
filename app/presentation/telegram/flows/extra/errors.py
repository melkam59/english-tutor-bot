from dataclasses import dataclass
from typing import Any

from app.application.errors.limits import (
    DailyLimitReachedError,
    InputTooLongError,
    LimitError,
    PremiumRequiredError,
    VoiceLimitReachedError,
    VoiceTooLongError,
)
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.extra.errors import ExtraErrorsPresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class ExtraErrorsFlow(BaseFlow):
    presenter: ExtraErrorsPresenter
    renderer: Renderer

    async def answer_something_went_wrong(self) -> Any:
        return await self.renderer.apply(self.presenter.something_went_wrong())

    async def answer_limit_error(self, error: LimitError) -> Any:
        views = {
            DailyLimitReachedError: self.presenter.daily_limit_reached,
            VoiceLimitReachedError: self.presenter.voice_limit_reached,
            VoiceTooLongError: self.presenter.voice_too_long,
            InputTooLongError: self.presenter.input_too_long,
            PremiumRequiredError: self.presenter.premium_required,
        }
        view = views.get(type(error), self.presenter.something_went_wrong)
        return await self.renderer.apply(view())

    async def answer_llm_error(self) -> Any:
        return await self.renderer.apply(self.presenter.llm_unavailable())

    async def answer_speech_error(self) -> Any:
        return await self.renderer.apply(self.presenter.voice_not_recognized())
