from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('🧭 Main Menu')


# ---Main Menu ---
btnRandom = KeyboardButton('🔢 Random Number')
btnOther = KeyboardButton('⏩ Other')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)

# ---Other Menu---
btnInfo = KeyboardButton('🤖 Info')
btnMusic = KeyboardButton('🎵 Music')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnMusic, btnMain)