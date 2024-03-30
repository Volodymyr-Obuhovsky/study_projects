from aiogram.types import BotCommand

private_commands = [
    BotCommand(command="about", description="про нас"),
    BotCommand(command="topics", description="популярні теми"),
    BotCommand(command="portfolio", description="наші портфоліо"),
    BotCommand(command="faq", description="часто задавані питання"),
    BotCommand(command="contacts", description="наші контакти"),
    BotCommand(command="help", description="список доступних команд")
]