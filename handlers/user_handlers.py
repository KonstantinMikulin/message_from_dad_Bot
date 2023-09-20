from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from keyboards import keyboards
from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(LEXICON_RU[message.text])
    # TODO: Add user to DB


@router.message(Command(commands=['help']))
async def process_help_cmd(message: Message):
    await message.answer(LEXICON_RU[message.text])
