from pyrogram import (Client, InlineKeyboardButton, InlineKeyboardMarkup, Filters)
from translation import Translation

@Client.on_message(Filters.command(["start"]))
async def start(client, update):
    #await client.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
    await client.send_message(
        chat_id=update.chat.id,
        text=Translation.WELCOME_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("OPTIONS", callback_data="help")]
            ])
    )

async def start_bot(client, update):
    await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    await client.send_message(
        chat_id=update.message.chat.id,
        text=Translation.WELCOME_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("OPTIONS", callback_data="help")]
            ])
    )


async def help_me(client, update):
    await client.delete_messages(chat_id=update.message.chat.id, message_ids=update.message.message_id)
    await client.send_message(
        chat_id=update.message.chat.id,
        text=Translation.HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("VIEW THUMB", callback_data="view_thumb"),
                 InlineKeyboardButton("DEL THUMB", callback_data="thumb_del_conf")],
                [InlineKeyboardButton("HELP", callback_data="start"),
                 InlineKeyboardButton("Close", callback_data="close")]
            ])
    )
