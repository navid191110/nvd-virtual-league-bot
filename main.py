from rubka import Robot, filters

TOKEN = "CDGFCJ0HZONMVANNGMOSWGKUEWFSLXFZRVKKJXSJXSWYRQEDHNZFJERHMLBCPVLC"

bot = Robot(token=TOKEN)

@bot.on_message(filters.is_command.start)
async def start(bot, message):
    await message.reply(
        "⚽ سلام!\n\n"
        "به ربات لیگ مجازی NVD خوش اومدی 🤩\n\n"
        "ربات با موفقیت فعال شد."
    )

bot.run()
