from datetime import timedelta

from app.application.interactors.progress.summary import ProgressInteractor
from app.application.models.dto.llm import Correction
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.mistake_category import MistakeCategory
from app.domain.enums.practice_mode import PracticeMode
from app.domain.user import User
from app.utils.time import datetime_now
from tests.mocks.gateways import (
    FakeConversationsGateway,
    FakeLessonsGateway,
    FakeMistakesGateway,
    FakeUsersGateway,
    FakeVocabularyGateway,
    make_user,
)


def make_progress(user: User) -> ProgressInteractor:
    return ProgressInteractor(
        user=user,
        users_gateway=FakeUsersGateway(),
        lessons_gateway=FakeLessonsGateway(completed=2),
        conversations_gateway=FakeConversationsGateway(),
        vocabulary_gateway=FakeVocabularyGateway(total=7),
        mistakes_gateway=FakeMistakesGateway(),
    )


async def test_first_activity_starts_a_streak() -> None:
    user = make_user()

    await make_progress(user).track_activity()

    assert user.current_streak == 1
    assert user.last_activity_at is not None


async def test_streak_grows_when_user_studied_yesterday() -> None:
    yesterday = datetime_now().date() - timedelta(days=1)
    user = make_user(current_streak=3, last_study_date=yesterday)

    await make_progress(user).track_activity()

    assert user.current_streak == 4


async def test_streak_does_not_grow_twice_a_day() -> None:
    user = make_user(current_streak=3, last_study_date=datetime_now().date())

    await make_progress(user).track_activity()

    assert user.current_streak == 3


async def test_streak_resets_after_a_missed_day() -> None:
    long_ago = datetime_now().date() - timedelta(days=3)
    user = make_user(current_streak=9, last_study_date=long_ago)

    await make_progress(user).track_activity()

    assert user.current_streak == 1


async def test_summary_shows_most_common_mistakes_first() -> None:
    progress = make_progress(make_user(english_level=EnglishLevel.B1, current_streak=5))
    await progress.conversations_gateway.create(user_id=1, mode=PracticeMode.GENERAL)
    for category in (
        MistakeCategory.ARTICLES,
        MistakeCategory.VERB_TENSE,
        MistakeCategory.ARTICLES,
    ):
        correction = Correction(
            original_text="a",
            corrected_text="b",
            explanation="c",
            category=category,
        )
        await progress.mistakes_gateway.add_many(user_id=1, corrections=[correction])

    summary = await progress.get_summary()

    assert summary.level is EnglishLevel.B1
    assert summary.practice_sessions == 1
    assert summary.completed_lessons == 2
    assert summary.learned_words == 7
    assert summary.current_streak == 5
    assert summary.common_mistakes == [
        (MistakeCategory.ARTICLES, 2),
        (MistakeCategory.VERB_TENSE, 1),
    ]
