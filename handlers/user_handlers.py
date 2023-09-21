import time

from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import default_state

from keyboards.keyboards import create_inline_joke_kb, create_rating_kb
from lexicon.lexicon import (LEXICON_MESSAGES_RU, LEXICON_JOKES,
                             LEXICON_JOKES_STICKERS, LEXICON_STICKERS, LEXICON_FILLFORM_RU)
from services.services import get_random_value
from FSM.fsm import user_dict

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_cmd(message: Message):
    await message.answer(LEXICON_MESSAGES_RU[message.text])
    # TODO: Add user to DB
    time.sleep(2)
    await message.answer(text='Хочешь пошучу?',
                         reply_markup=create_inline_joke_kb())


@router.message(Command(commands=['help']), StateFilter(default_state))
async def process_help_cmd(message: Message):
    await message.answer(LEXICON_MESSAGES_RU[message.text])


# Handler for 'joke' cmd
@router.message(Command(commands=['joke']))
async def process_joke_cmd(message: Message):
    dictionary = LEXICON_JOKES

    await message.answer(text=get_random_value(dictionary))
    time.sleep(3)
    await message.answer(text='Ещё?',
                         reply_markup=create_inline_joke_kb())


# Handler for 'rate" cmd
@router.message(Command(commands=['rate']))
async def process_rate_cmd(message: Message):
    await message.answer(text='Rate please',
                         reply_markup=create_rating_kb(width=5))


# Handler for callback data 'yes_joke'
@router.callback_query(F.data == 'yes_joke')
async def process_yes_joke_press(callback: CallbackQuery):
    time.sleep(1)
    await callback.message.answer(text=get_random_value(LEXICON_JOKES))
    time.sleep(2)
    await callback.bot.send_sticker(chat_id=callback.message.chat.id,
                                    sticker=get_random_value(LEXICON_JOKES_STICKERS))
    time.sleep(2)
    await callback.message.answer(text='Ещё?',
                                  reply_markup=create_inline_joke_kb())

    await callback.answer()


# Handler for callback data 'no_joke'
@router.callback_query(F.data == 'no_joke')
async def process_no_joke_press(callback: CallbackQuery):
    dictionary = LEXICON_JOKES

    time.sleep(1)
    await callback.message.answer(text=LEXICON_MESSAGES_RU['yes_to_no'])
    time.sleep(1)
    await callback.message.answer(text=get_random_value(dictionary))
    time.sleep(2)
    await callback.bot.send_sticker(chat_id=callback.message.chat.id,
                                    sticker=get_random_value(LEXICON_JOKES_STICKERS))
    time.sleep(2)
    await callback.message.answer(text='Ещё пошутить?',
                                  reply_markup=create_inline_joke_kb())

    await callback.answer()


# Handler for "/showdata" cmd
@router.message(Command(commands=['showdata']), StateFilter(default_state))
async def process_showdata_cmd(message: Message):
    if message.from_user.id in user_dict:
        await message.answer_photo(photo=user_dict[message.from_user.id]['photo_id'],
                                   caption=f'Имя: {user_dict[message.from_user.id]["name"]}\n'
                                           f'Возраст: {user_dict[message.from_user.id]["age"]}\n'
                                           f'Пол: {user_dict[message.from_user.id]["gender"]}\n')
    else:
        await message.answer(text=LEXICON_FILLFORM_RU['no_form'])
