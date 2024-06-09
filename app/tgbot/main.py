import logging
import os

from dotenv import find_dotenv, load_dotenv

from app.tgbot.handlers import router

load_dotenv(find_dotenv())

from aiogram import Bot, Dispatcher


async def base() -> None:
    bot = Bot(token=os.getenv('TG_BOT_TOKEN'), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(router)

    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")



    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")

