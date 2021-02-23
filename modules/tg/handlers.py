from aiogram import types
from aiogram.utils.markdown import hcode

from core.misc import dp, bot
from modules.content_processor.aparser import parse_url

test_url = 'https://www.chanty.com/blog/components-effective-team-communication'


@dp.message_handler(commands=['start'])
async def cmd_start(m: types.Message):
    s = f"""
Hi! Send me a link to get a small summary of an Article with hashtags. Should be useful for blogging or Linkedin.

`<url> <max_summary_sentences> <max_summary_words> <language>`

url - mandatory url to article
max_summary_sentences - optional, defaults to `4`
max_summary_words - optional, defaults to `100`
language - optional, defaults to `en`

Example
{test_url} 5 100 en
"""
    await m.reply(s, reply=False, parse_mode='Markdown')


@dp.message_handler(content_types=['text', 'photo', 'document'])
async def process_url(m: types.Message):
    await bot.send_chat_action(m.from_user.id, 'typing')
    for e in (m.entities or m.caption_entities):
        if e.type == 'url':
            url = e.get_text(m.text or m.caption)
            splitted = (m.text or m.caption).split(' ')
            num_sentences = 4
            # Max sentences for summary
            try:
                num_sentences = int(splitted[1])
            except (IndexError, ValueError):
                pass

            num_words = 100
            # Max words for summary
            try:
                num_words = int(splitted[2])
            except (IndexError, ValueError):
                pass

            lang = 'en'
            # Max words for summary
            try:
                lang = splitted[3].lower()
                if len(lang) != 2:
                    await m.reply(
                        'Language parameter must be two chars long. Example: {}'.format(', '.join(hcode('ru', 'en'))))
                    return
            except (IndexError, ValueError):
                pass

            try:
                await m.reply(parse_url(url, num_sentences, num_words, lang))
            except Exception as e:
                await m.reply('Sorry, got error {}'.format(hcode(str(e))))
            return

    await m.reply('Cant find any urls in message!')
