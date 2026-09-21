from datetime import datetime

from app.domain.vocabulary_item import VocabularyItem


def schedule_next_review(item: VocabularyItem, is_correct: bool, now: datetime) -> datetime:
    """
    Simplified spaced repetition (Leitner-like).

    TODO(M3): interval grows with the correct-answer streak
     (e.g. 1d, 2d, 4d, 7d, 14d, 30d) and resets to ~10 minutes on a wrong answer.
    """
    raise NotImplementedError
