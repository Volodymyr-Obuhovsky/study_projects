from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

user_private_router = Router()


@user_private_router.message(Command("menu"))
async def menu_(message: Message) -> None:
    await message.answer("Accessed menu:")
