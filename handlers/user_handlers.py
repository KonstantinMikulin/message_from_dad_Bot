from copy import deepcopy
import time

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from keyboards.keyboards import create_inline_joke_kb
from lexicon.lexicon import LEXICON_MESSAGES_RU

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(LEXICON_MESSAGES_RU[message.text])
    # TODO: Add user to DB
    time.sleep(2)
    await message.answer(text='Хочешь пошучу?',
                         reply_markup=create_inline_joke_kb())


@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message):
    await message.answer(LEXICON_MESSAGES_RU[message.text])
