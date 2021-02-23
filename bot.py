from aiogram import Dispatcher

from core import config, misc
from core.load import load_modules


async def startup_polling(dp: Dispatcher):
    await dp.bot.delete_webhook()


async def shutdown(dp: Dispatcher):
    pass


def main():
    # Include all modules
    load_modules()

    # Register startup/shutdown callbacks
    misc.runner.on_startup(startup_polling, polling=True, webhook=False)
    misc.runner.on_shutdown(shutdown)
    # Run is selected mode
    misc.runner.start_polling()


if __name__ == '__main__':
    main()
