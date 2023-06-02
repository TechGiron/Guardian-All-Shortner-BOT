from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**VIP **
	Price 200 🇮🇳/🌎 2.5$  per Month
		
	Pay Using Upi I'd ```rahulrathee52402@okhdfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/unicornguardian")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/unicornguardian")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
