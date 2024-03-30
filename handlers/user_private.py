from aiogram import Router, F, filters
from aiogram.filters import Command
from aiogram.types import Message

from app_filters.chat_types import ChatTypes

user_private_router = Router()
user_private_router.message.filter(ChatTypes(["private"]))


# F - is magic filter
@user_private_router.message(F.text)
async def test(message: Message) -> None:
    await message.answer("This is magic filter")
