from dataclasses import dataclass

from app.application.models.dto.progress import ProgressSummary
from app.presentation.telegram.presenters.base import BasePresenter
from app.presentation.telegram.view.models import View


@dataclass(frozen=True)
class ProgressPresenter(BasePresenter):
    def summary(self, summary: ProgressSummary) -> View:
        mistakes: str = "\n".join(
            f"• {self.i18n.get(f'mistakes-{category.value}')} — {count}"
            for category, count in summary.common_mistakes
        )
        return View(
            text=self.i18n.messages.progress.summary(
                level=summary.level.value if summary.level else "—",
                lessons=summary.completed_lessons,
                sessions=summary.practice_sessions,
                words=summary.learned_words,
                minutes=summary.total_study_seconds // 60,
                streak=summary.current_streak,
                mistakes=mistakes or "—",
            ),
            edit=False,
        )
