import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.utils.markdown import link
import markups as nav
import random
# from tictactoe import main

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/start - начало работы с ботом
/help - список команд
/tictactoe - о работе бота
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


@dp.message_handler(commands=['tictactoe'])
async def description(message: types.Message):
    board = list(range(1, 10))
    wins_coordinate = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

    def draw_board():
        print('-------------')
        for i in range(3):
            print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')

    def take_input(player_signal):
        while True:
            value = input('Выберите позицию: ' + player_signal + ' ? ')
            if not (value in '123456789'):
                print('Такого числа нет в таблице. Повторите пожалуйта!')
                continue  # Возвращает на начало цикла while
            value = int(value)
            if str(board[value - 1]) in 'XO':
                print('Эта клетка уже занята')
                continue
            board[value - 1] = player_signal
            break

    def check_win():
        for each in wins_coordinate:
            if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
                return board[each[1] - 1]
        else:
            return False

    def main():
        counter = 0
        while True:
            draw_board()
            if counter % 2 == 0:
                take_input('X')
            else:
                take_input('O')
            if counter > 3:
                winner = check_win()
                if winner:
                    draw_board()
                    print(winner, 'выиграл!')
                    break
            counter += 1
            if counter > 8:
                draw_board()
                print('Ничья!')
                break

    main()


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
