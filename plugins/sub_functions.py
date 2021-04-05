import os
import os.path
import time
from pyrogram import (Client, InlineKeyboardButton, InlineKeyboardMarkup, Filters)
from translation import Translation
from plugins.help import help_me

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(Filters.photo)
async def save_photo(client, update):
    # received single photo
    if update.from_user.id not in Config.AUTH_USERS:
        await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
        a = await update.message.reply_text(text=Translation.NOT_AUTH_TXT, disable_web_page_preview=True)
        time.sleep(5)
        await a.delete()
        await help_me(client, update)
        return
    await client.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
    thumb_image = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    await client.download_media(message=update, file_name=thumb_image)
    await update.delete()
    b = await client.send_message(chat_id=update.chat.id, text=Translation.SAVED_CUSTOM_THUMB_NAIL)
    time.sleep(5)
    await b.delete()


async def view_thumbnail(client, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
        c = await update.message.reply_text(text=Translation.NOT_AUTH_TXT, disable_web_page_preview=True)
        time.sleep(5)
        await c.delete()
        await help_me(client, update)
        return
    await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    thumb_image = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    if os.path.exists(thumb_image):
        await client.send_photo(
            chat_id=update.message.chat.id,
            photo=thumb_image,
            caption=Translation.THUMB_CAPTION,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("DEL THUMB", callback_data="thumb_del_conf"),
                                                InlineKeyboardButton("Back", callback_data="help")]]))
    else:
        await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
        e = await client.send_message(chat_id=update.message.chat.id, text=Translation.NO_THUMB)
        time.sleep(5)
        await e.delete()
        await help_me(client, update)


async def delete_thumbnail(client, update):
    await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    thumb_image = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    try:
        os.remove(thumb_image)
        a = await client.send_message(chat_id=update.message.chat.id, text=Translation.DEL_CUSTOM_THUMB_NAIL)
        time.sleep(5)
        await a.delete()
        await help_me(client, update)
    except IndexError:
        pass

async def del_thumb_confirm(client, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
        g = await update.message.reply_text(text=Translation.NOT_AUTH_TXT, disable_web_page_preview=True)
        time.sleep(5)
        await g.delete()
        await help_me(client, update)
        return
    await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    thumb_image_path = os.getcwd() + "/" + "thumbnails" + "/" + str(update.from_user.id) + ".jpg"
    if os.path.exists(thumb_image_path):
        await client.send_message(
            chat_id=update.message.chat.id,
            text=Translation.DEL_THUMB_CONFIRM,
            reply_to_message_id=update.message.message_id,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✅ Sure, Delete It", callback_data="del_sure"),
                                                InlineKeyboardButton("Back", callback_data="help")]]))
    else:
        await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
        h = await client.send_message(chat_id=update.message.chat.id, text=Translation.NO_THUMB)
        time.sleep(5)
        await h.delete()
        await help_me(client, update)

async def close_button(client, update):
    await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)