import asyncio

from app.tgbot import base

if __name__ == '__main__':
    try:
        asyncio.run(base())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
