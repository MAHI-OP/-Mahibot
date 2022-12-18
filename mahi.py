import os
from telethon import TelegramClient, events, functions, types, Button
APP_ID = 15700407
API_HASH = "8a3651638b152f524d923cd6df87e40d"
BOT_TOKEN = "5925198362:AAFVTA3y7-W0LUPbnh09HBHbaAV5mHc48xs"
bot = TelegramClient('baby', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
@bot.on(events.NewMessage(pattern="/start"))
async def legendboy(event):
await event.reply("hey baby how are you")  
