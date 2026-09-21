from dataclasses import dataclass

from aiogram import html

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
        parts: list[str] = []
        if reply.corrections:
            if reply.corrected_text:
                parts.append(f"✅ {html.bold(html.quote(reply.corrected_text))}")
            explanations: list[str] = [self.i18n.messages.practice.explanation()]
            for correction in reply.corrections:
                explanations.append(
                    f"• {html.strikethrough(html.quote(correction.original_text))}"
                    f" → {html.bold(html.quote(correction.corrected_text))}\n"
                    f"  {html.italic(html.quote(correction.explanation))}"
                )
            parts.append("\n".join(explanations))
        if reply.better_phrases:
            phrases: str = "\n".join(f"• {html.quote(phrase)}" for phrase in reply.better_phrases)
            parts.append(f"{self.i18n.messages.practice.better_phrases()}\n{phrases}")
        parts.append(f"💬 {html.quote(reply.reply)}")
        return View(text="\n\n".join(parts), edit=False, reply=bool(reply.corrections))

    def transcription(self, text: str) -> View:
        # TODO(M4): echo what the bot heard in a voice message
        raise NotImplementedError
