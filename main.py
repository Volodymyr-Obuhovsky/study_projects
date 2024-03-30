import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommandScopeAllPrivateChats
from aiogram.utils.markdown import hbold

from common.commands import private_commands
from environment import set_environment
from handlers.info import info_router
from handlers.portfolio import portfolio_router
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router


set_environment("test_local")

# receive our token from environment variables
TOKEN_API = os.getenv("BOT_TOKEN")
dp = Dispatcher()
ALLOWED_UPDATES = ["message", "edited_message",
                   "channel_post", "edited_channel_post"]


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        f"Hi {hbold(message.from_user.full_name)}, i am TestRetouchUABot and i will help you as much as possible")


dp.include_routers(info_router, portfolio_router, user_private_router, user_group_router)


async def main() -> None:
    bot = Bot(TOKEN_API, parse_mode=ParseMode.HTML)

    # it is necessary for situation, when bot hasn't worked anytime and
    # after start, it will not answer on collected messages in chat
    await bot.delete_webhook(drop_pending_updates=True)

    # delete bot menu
    # await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())

    # create bot menu
    await bot.set_my_commands(commands=private_commands, scope=BotCommandScopeAllPrivateChats())
    # only updates is pointed in allowed_updates will be handled
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
