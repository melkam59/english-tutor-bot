from dataclasses import dataclass

from app.application.models.dto.llm import TutorReply
from app.presentation.telegram.keyboards.menu import practice_modes_keyboard
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class PracticePresenter(BasePresenter):
    def choose_mode(self) -> View:
        return View(
            text=self.i18n.messages.practice.choose_mode(),
            reply_markup=practice_modes_keyboard(i18n=self.i18n),
            edit=False,
        )

    def tutor_reply(self, reply: TutorReply) -> View:
        # TODO(M2): corrected sentence + explanation block + the follow-up question
        raise NotImplementedError

    def transcription(self, text: str) -> View:
        # TODO(M4): echo what the bot heard in a voice message
        raise NotImplementedError
