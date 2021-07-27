# Copyriht (C) 2021 By VeezProject

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as veez
from config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`memulai global cast...`")
        if not message.reply_to_message:
            await wtf.edit("tolong balas ke pesan apapun untuk broadcast!")
            return
        lmao = message.reply_to_message.text
        async for dialog in veez.iter_dialogs():
            try:
                await veez.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`global cast...` \n\n**Mengirim ke:** `{sent}` Chats \n**gagal di:** {failed} Chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
                #await wtf.edit(f"`Melakukan gcast...` \n\n**Mengirim ke:** `{sent}` Chats \n**gagal di:** {failed} Chats")
                
            
        await message.reply_text(f"`gcast berhasil ` \n\n**Mengirim ke:** `{sent}` Chats \n**gagal di:** {failed} Chats")
