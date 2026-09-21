from typing import Any, Final

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from dishka import FromDishka

from app.presentation.telegram.flows.admin.panel import AdminFlow

router: Final[Router] = Router(name=__name__)


def _int_args(command: CommandObject, count: int) -> list[int] | None:
    args: list[str] = (command.args or "").split()
    if len(args) != count or not all(arg.isdigit() for arg in args):
        return None
    return [int(arg) for arg in args]


@router.message(Command("stats"))
async def show_stats(_: Message, flow: FromDishka[AdminFlow]) -> Any:
    return await flow.show_stats()


@router.message(Command("ban"))
async def ban(_: Message, command: CommandObject, flow: FromDishka[AdminFlow]) -> Any:
    """/ban <user_id>"""
    if (args := _int_args(command, count=1)) is None:
        return await flow.invalid_arguments()
    return await flow.ban(user_id=args[0])


@router.message(Command("unban"))
async def unban(_: Message, command: CommandObject, flow: FromDishka[AdminFlow]) -> Any:
    """/unban <user_id>"""
    if (args := _int_args(command, count=1)) is None:
        return await flow.invalid_arguments()
    return await flow.unban(user_id=args[0])


@router.message(Command("premium"))
async def grant_premium(_: Message, command: CommandObject, flow: FromDishka[AdminFlow]) -> Any:
    """/premium <user_id> <days>"""
    if (args := _int_args(command, count=2)) is None:
        return await flow.invalid_arguments()
    return await flow.grant_premium(user_id=args[0], days=args[1])


@router.message(Command("unpremium"))
async def revoke_premium(_: Message, command: CommandObject, flow: FromDishka[AdminFlow]) -> Any:
    """/unpremium <user_id>"""
    if (args := _int_args(command, count=1)) is None:
        return await flow.invalid_arguments()
    return await flow.revoke_premium(user_id=args[0])


@router.message(Command("broadcast"))
async def broadcast(_: Message, command: CommandObject, flow: FromDishka[AdminFlow]) -> Any:
    """/broadcast <text>"""
    if not command.args:
        return await flow.invalid_arguments()
    return await flow.broadcast(text=command.args)
