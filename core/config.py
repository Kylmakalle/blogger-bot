import os
import pathlib


def get_value(key, default=None, converter=None):
    value = os.environ.get(key, default) or default
    if converter:
        return converter(value)
    return str(value)


# About
author = "Kylmakalle"
git_repository = "https://github.com/Kylmakalle/linkedin-bot"

# Telegram
bot_token = get_value('BOT_TOKEN', '')
skip_updates = get_value('SKIP_UPDATES', False, bool)

# Database
mongodb = {
    'host': get_value('MONGODB_HOST', 'mongodb'),
    'maxPoolSize': get_value('MONGODB_MAX_POOL_SIZE', 1000, int),
    'retryWrites': get_value('MONGODB_RETRY_WRITES', True, bool)
}


sentry_url = get_value('SENTRY_URL', '')
