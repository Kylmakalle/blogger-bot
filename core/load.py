from core import misc


def load_modules():
    misc.loader.load_packages(f"modules.{item}" for item in [
        'tg',  # Telegram
    ])
