from dataclasses import dataclass

from app.domain.enums.practice_mode import PracticeMode
from app.domain.user import User


@dataclass(frozen=True)
class AccessPolicy:
    """Free / Premium feature matrix. Pure logic, no I/O."""

    def is_premium(self, user: User) -> bool:
        # TODO(M4): PREMIUM type and subscription_expires_at in the future (or None = lifetime)
        raise NotImplementedError

    def can_use_mode(self, user: User, mode: PracticeMode) -> bool:
        # TODO(M4): free plan -> PracticeMode.GENERAL only
        raise NotImplementedError

    def can_use_lessons(self, user: User) -> bool:
        raise NotImplementedError

    def can_use_vocabulary(self, user: User) -> bool:
        raise NotImplementedError

    def can_see_full_progress(self, user: User) -> bool:
        raise NotImplementedError
