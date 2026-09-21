import pytest

pytestmark = pytest.mark.skip(reason="scaffold: implement together with M2")


def test_free_user_is_blocked_after_daily_limit() -> None: ...


def test_premium_user_has_higher_limit() -> None: ...


def test_too_long_input_is_rejected() -> None: ...


def test_voice_duration_limit() -> None: ...
