#----------------------------------- https://github.com/m4mallu/DeleteMediaRobot -------------------------------------#

import os
import time

from bot import Bot
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from helper.get_messages import get_messages
from pyrogram.errors import ChatAdminRequired
from presets import Presets

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

@Bot.on_message(filters.group & filters.command('cleanmedia'))
async def del_all_command_fn(client: Bot, message: Message):
    await message.delete()
    if message.from_user.id not in Config.AUTH_USERS:
        return
    try:
        status_message = await client.send_message(
            chat_id=message.chat.id,
            text=Presets.DELETING_MESSAGE,
            parse_mode='html',
            disable_web_page_preview=True
        )
    except ChatAdminRequired:
        status_message = None
    try:
        await get_messages(
            client.USER,
            message.chat.id,
            0,
            status_message.message_id if status_message else message.message_id,
            []
        )
    except FloodWait as e:
        time.sleep(e.x)
    await client.edit_message_text(
        chat_id=message.chat.id,
        text=Presets.DELETED_MESSAGE,
        message_id=status_message.message_id,
        parse_mode='html',
        disable_web_page_preview=True
    )
