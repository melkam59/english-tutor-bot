from dataclasses import dataclass
from typing import Any

from app.application.interactors.limits.usage import UsageLimitsInteractor
from app.application.interactors.progress.summary import ProgressInteractor
from app.application.interactors.tutor.conversation import TutorConversationInteractor
from app.application.interactors.voice.transcription import VoiceInteractor
from app.domain.enums.practice_mode import PracticeMode, RolePlayScenario
from app.domain.enums.request_type import RequestType
from app.presentation.telegram.flows.base import BaseFlow
from app.presentation.telegram.presenters.common.practice import PracticePresenter
from app.presentation.telegram.view.renderer import Renderer


@dataclass(frozen=True)
class PracticeFlow(BaseFlow):
    tutor: TutorConversationInteractor
    limits: UsageLimitsInteractor
    voice: VoiceInteractor
    progress: ProgressInteractor
    presenter: PracticePresenter
    renderer: Renderer

    async def choose_mode(self) -> Any:
        return await self.renderer.apply(self.presenter.choose_mode())

    async def select_mode(self, mode: PracticeMode) -> Any:
        # TODO(M2): ROLE_PLAY -> scenario keyboard, otherwise tutor.start(mode) + opening line
        return await self.renderer.apply(self.presenter.not_implemented())

    async def select_scenario(self, scenario: RolePlayScenario) -> Any:
        # TODO(M2)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def stop(self) -> Any:
        # TODO(M2)
        return await self.renderer.apply(self.presenter.not_implemented())

    async def reply_text(self, text: str) -> Any:
        await self.limits.check_text_message(text)
        await self.renderer.typing()
        reply = await self.tutor.reply(text)
        await self.limits.record_llm_usage(RequestType.CHAT, reply.usage)
        await self.progress.track_activity()
        return await self.renderer.apply(self.presenter.tutor_reply(reply))

    async def reply_voice(self, file_id: str, duration: int) -> Any:
        # TODO(M4): limits.check_voice_message -> voice.transcribe -> limits.record_stt_usage
        #  -> same pipeline as reply_text (+ optional TTS answer)
        return await self.renderer.apply(self.presenter.not_implemented())
