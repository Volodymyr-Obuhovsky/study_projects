from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

portfolio_router = Router()

portfolio_topics = """
/glass products
/matte products
/gadgets and devices
/bags and backpacks
/dress
"""


# F - is magic filter
@portfolio_router.message(Command("portfolio"))
async def portfolio_handler(message: Message) -> None:
    await message.answer(f"Ви увійшли до меню доступного контенту.\n"
                         f"Оберіть, будь-ласка, категорію : {portfolio_topics}")
