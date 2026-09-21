import pytest

from app.application.errors.profile import ProfileIncompleteError
from app.application.interactors.onboarding.profile import ProfileInteractor
from app.domain.enums.communication_format import CommunicationFormat
from app.domain.enums.english_level import EnglishLevel
from app.domain.enums.learning_goal import LearningGoal
from tests.mocks.gateways import FakeUsersGateway, make_user


def make_interactor() -> tuple[ProfileInteractor, FakeUsersGateway]:
    gateway = FakeUsersGateway()
    return ProfileInteractor(user=make_user(), users_gateway=gateway), gateway


async def test_english_level_selection_is_persisted() -> None:
    interactor, gateway = make_interactor()

    await interactor.set_english_level(EnglishLevel.B1)

    assert gateway.users[1].english_level is EnglishLevel.B1


async def test_onboarding_saves_learning_profile() -> None:
    interactor, gateway = make_interactor()

    await interactor.set_native_language("pl")
    await interactor.set_english_level(EnglishLevel.A2)
    await interactor.set_learning_goal(LearningGoal.TRAVEL)
    await interactor.set_communication_format(CommunicationFormat.TEXT)
    await interactor.complete_onboarding()

    saved = gateway.users[1]
    assert saved.native_language == "pl"
    assert saved.learning_goal is LearningGoal.TRAVEL
    assert saved.communication_format is CommunicationFormat.TEXT
    assert saved.is_onboarded


async def test_onboarding_cannot_complete_with_missing_answers() -> None:
    interactor, _ = make_interactor()

    await interactor.set_native_language("pl")

    with pytest.raises(ProfileIncompleteError):
        await interactor.complete_onboarding()
