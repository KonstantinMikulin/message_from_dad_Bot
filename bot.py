from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from config_data import config
from lexicon.lexicon import LEXICON_RU

BOT_TOKEN = config.TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# Handler for /start cmd
@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(
        text=LEXICON_RU['start']
    )


# Handler for /help cmd
@dp.message(Command(commands=['help']))
async def process_help_cmd(message: Message):
    await message.answer(
        text=LEXICON_RU['help']
    )


if __name__ == '__main__':
    dp.run_polling(bot)
