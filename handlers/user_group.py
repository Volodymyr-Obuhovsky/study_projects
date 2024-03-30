from string import punctuation, digits

from aiogram import types, Router
from aiogram.utils.markdown import hbold

from app_filters.chat_types import ChatTypes
from common.restrictions import restricted_words

user_group_router = Router()
user_group_router.message.filter(ChatTypes(['group', 'supergroup']))

user_group_router.message()


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation + digits))


@user_group_router.edited_message()
@user_group_router.message()
async def restrictions_handler(message: types.Message):
    message_words: set = set(clean_text(message.text).lower().split())
    if restricted_words.intersection(message_words):
        await message.delete()
        await message.answer(f"{hbold(message.from_user.first_name)} будь-ласка не лайтеся\n"
                             f"та дотримуйтесь правил користування чатом")
