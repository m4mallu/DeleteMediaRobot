#----------------------------------- https://github.com/m4mallu/DeleteMediaRobot -------------------------------------#

import time

from pyrogram import Client, filters
from presets import Presets

@Client.on_message(filters.private & filters.command(['start', 'help']))
async def help_me(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=Presets.WELCOME_TEXT.format(message.from_user.first_name),
        parse_mode='html',
        disable_web_page_preview=True
    )


@Client.on_message(filters.private & filters.command('cleanmedia'))
async def not_here(client, message):
    await message.delete()
    a = await client.send_message(
        chat_id=message.chat.id,
        text=Presets.NOT_HERE_TEXT,
        parse_mode='html'
    )
    time.sleep(5)
    await a.delete()


@Client.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    await message.delete()
