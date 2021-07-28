from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME, BOT_USERNAME, ASSISTANT_NAME, OWNER, GROUP_SUPPORT, UPDATES_CHANNEL, PROJECT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELBV5g_zDtu5CEiT6hNd5ZcL7QCzGznAACDQIAAqWPKVTYFqnjbykUNiAE")
    await message.reply_text(
        f"""**👋🏻 Halo {message.from_user.first_name}, saya adalah {BOT_NAME}, bot yang dapat memutar musik di voice chat group kamu.

✨ Welcome back to {bn}, Saya adalah bot musik yang dirancang agar dapat memutar musik di voice chat group anda dengan cara yang mudah dan praktis.

👩‍💻 Bot ini dikelola oleh {OWNER}.

💁🏻‍♀️ Anda ingin memutar musik di vcg?, silahkan tambahkan saya dan @{ASSISTANT_NAME} ke grup anda dan jadikan admin.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ TAMBAHKAN KE GROUP ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🔰 GROUP 🔰", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📮 CHANNEL 📮", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 DONATION", url="https://t.me/boyfriendnice"
                    )]
            ]
        ),
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ bot music player is online.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📮 CHANNEL 📮", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        )
   )

@Client.on_message(
    filters.command("inline")
    & filters.group
    & ~ filters.edited
)
async def inline(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah anda ingin mencari link youtube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ iya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ tidak", callback_data="close"
                    )
                ]
            ]
        )
    )
        
@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**💁🏻‍♀️ Hai, silahkan tekan tombol dibawah untuk melihat panduan untuk menggunakan bot ini, terimakasih.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜PANDUAN MENGGUNAKAN BOT📜", url="https://t.me/BeKing_Bots/9"
                    )
                ]
            ]
        ),
    )  

    
@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👩‍💻 OWNER", url=f"https://t.me/{OWNER}"
                    ),
                    InlineKeyboardButton(
                        "📮 CHANNEL", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
   )
