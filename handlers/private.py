import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME, BOT_USERNAME, ASSISTANT_NAME, OWNER, GROUP_SUPPORT, UPDATES_CHANNEL, PROJECT_NAME as bn
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**👋🏻 Halo {message.from_user.first_name}, saya adalah {BOT_NAME}, bot yang dapat memutar musik di voice chat group kamu.

✨ Welcome back to {bn}, Saya adalah bot musik yang dirancang agar dapat memutar musik di voice chat group anda dengan cara yang mudah dan praktis, klik /guide untuk membaca panduan penggunaan.

👩‍💻 Bot ini dikelola oleh {OWNER}.

💁🏻‍♀️ Anda ingin memutar musik di vcg?, silahkan tambahkan saya dan [assistant bot](https://t.me/{ASSISTANT_NAME}) ke grup anda dan jadikan admin.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ TAMBAHKAN KE GRUP ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "🌻 GROUP 🌻", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🌸 CHANNEL 🌸", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🎁 DONATION", url="https://t.me/dlwrml"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✅ bot music player is online.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌸 CHANNEL 🌸", url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        )
   )

@Client.on_message(
    filters.command("inline")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
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
                        "📜 PANDUAN MEMAKAI BOT 📜", url="https://telegra.ph/VEEZ-MUSIC-GUIDE-07-27"
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
                        "🌻 GROUP", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "🌸 CHANNEL", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
   )

@Client.on_message(
    filters.command("guide")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        """📚 **silahkan baca panduan yang sudah kami siapkan dibawah ini untuk menggunakan bot musik ini:** https://telegra.ph/VEEZ-MUSIC-GUIDE-07-27""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔮 CHANNEL SUPPORT", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        ),
    )
