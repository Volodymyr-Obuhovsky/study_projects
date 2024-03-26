from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

info_router = Router()

LIST_COMMANDS = """
/start - початок роботи з ботом
/help - список команд для взаємодії з ботом
/description - загальний опис бота
/topics - список останніх обговорюваних тем на каналі
/portfolio - наші портфоліо
/faq - часто задавані питання
/contacts - контакти для бізнесу
"""


@info_router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(LIST_COMMANDS)


@info_router.message(Command("description"))
async def description_cmd(message: Message) -> None:
    await message.answer("Цей бот створений як персональний помічник в telegram-каналі RetouchUA. "
                         "Він допоможе Вам з пошуком контенту, користуванні освітніми матеріалами, "
                         "посиланнями на корисні ресурси та з відповідями на часто задавані питання.")


