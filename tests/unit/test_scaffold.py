"""Smoke tests that keep the scaffold wired correctly while features are being filled in."""

from dishka import AsyncContainer

import app.domain  # noqa: F401  (registers every entity in Base.metadata)
from app.const import MESSAGES_SOURCE_DIR
from app.domain.base import Base
from app.domain.enums.practice_mode import PracticeMode
from app.presentation.telegram.handlers import admin, extra, main
from app.providers.container import create_container


def test_all_entities_are_registered() -> None:
    assert set(Base.metadata.tables) == {
        "users",
        "conversations",
        "messages",
        "user_mistakes",
        "vocabulary_items",
        "lessons",
        "usage_records",
    }


def test_dependency_graph_is_valid() -> None:
    # dishka validates the whole graph when the container is created
    container: AsyncContainer = create_container()
    assert container is not None


def test_routers_are_importable() -> None:
    assert admin.router and extra.router and main.router


def test_every_practice_mode_has_a_button_text() -> None:
    ftl: str = (MESSAGES_SOURCE_DIR / "en" / "practice.ftl").read_text(encoding="utf-8")
    for mode in PracticeMode:
        assert f"buttons-practice-{mode.value} =" in ftl
