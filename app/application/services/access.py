from dataclasses import dataclass

from app.domain.enums.practice_mode import PracticeMode
from app.domain.enums.subscription import SubscriptionType
from app.domain.user import User
from app.utils.time import datetime_now


@dataclass(frozen=True)
class AccessPolicy:
    """Free / Premium feature matrix. Pure logic, no I/O."""

    def is_premium(self, user: User) -> bool:
        if user.subscription_type is not SubscriptionType.PREMIUM:
            return False
        # No expiration date means lifetime access
        expires_at = user.subscription_expires_at
        return expires_at is None or expires_at > datetime_now()

    def can_use_mode(self, user: User, mode: PracticeMode) -> bool:
        # TODO(M4): free plan -> PracticeMode.GENERAL only
        raise NotImplementedError

    def can_use_lessons(self, user: User) -> bool:
        raise NotImplementedError

    def can_use_vocabulary(self, user: User) -> bool:
        raise NotImplementedError

    def can_see_full_progress(self, user: User) -> bool:
        raise NotImplementedError
