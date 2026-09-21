import pytest

pytestmark = pytest.mark.skip(reason="scaffold: implement together with M5")


def test_start_shows_onboarding_for_new_user() -> None: ...


def test_start_shows_menu_for_onboarded_user() -> None: ...


def test_admin_commands_are_rejected_for_regular_users() -> None: ...
