import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.utils.markdown import link
import markups as nav
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/start - начало работы с ботом
/help - список команд
/description - о работе бота
"""




async def on_startup(_):
    print('Bot launched successfully!')


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
        This handler will be called when user sends `/start` command
    """
    await bot.send_message(message.from_user.id, 'Hi {0.first_name}'.format(message.from_user) +' 👋', reply_markup=nav.mainMenu)
    await message.delete()


@dp.message_handler(commands=['help'])
async def send_helper(message: types.Message):
    """
        This handler will be called when user sends  `/help` command
    """
    await message.reply(text=HELP_COMMAND)


@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer("The bot will improve itself every day in search of something interesting")
    await message.delete()


@dp.message_handler()
async def choose(message: types.Message):
    # await message.answer("I'm sorry, I haven't set up scripts yet, but the developers are working on it" + ' 😅')
    # await message.reply(message.text + '❤️' + '🤗 ')
    if message.text == '🔢 Random Number':
        await bot.send_message(message.from_user.id, 'Your number is: ' + str(random.randint(0, 1001)))
        await message.delete()
    elif message.text == '🧭 Main Menu':
        await bot.send_message(message.from_user.id, '🧭 Main Menu', reply_markup= nav.mainMenu)
        await message.delete()
    elif message.text == '⏩ Other':
        await bot.send_message(message.from_user.id, '⏩ Other', reply_markup= nav.otherMenu)
        await message.delete()
    elif message.text == '🤖 Info':
        await bot.send_message(message.from_user.id, "🧬 Fear is stupid. I'm sorry I was affraid, 1960" )
        await message.delete()
    elif message.text == '🎵 Music':
        await bot.send_message(message.from_user.id, '🎵 Music', reply_markup= nav.otherMenu)
        await message.reply('<a href="https://music.yandex.ru">Listen to music</a>',parse_mode="HTML")
        await message.delete()
    else:
        await message.reply("I will try understand you in the future 💋")



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
