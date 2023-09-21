from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import CallbackQuery, Message, PhotoSize
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from lexicon.lexicon import (LEXICON_MESSAGES_RU, LEXICON_FILLFORM_RU)
from FSM.fsm import FSMFillForm, user_dict

router = Router()


# Handler for "/cancel" if FSM in default state
@router.message(Command(commands=['cancel']), StateFilter(default_state))
async def process_cancel_cmd(message: Message):
    await message.answer(text=LEXICON_MESSAGES_RU[message.text])


# Handler for "/cancel" if FSM in some state
@router.message(Command(commands=['cancel']), ~StateFilter(default_state))
async def process_cancel_cmd_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_MESSAGES_RU['cancel_state'])
    await state.clear()


# Handler for beginning filling form
@router.message(Command(commands=['fillform']), StateFilter(default_state))
async def process_fillform_cmd(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_FILLFORM_RU['fill_name'])
    await state.set_state(FSMFillForm.fill_name)


# Handler if name was sent correct
# and switch to fill_age state
@router.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
async def process_sent_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FILLFORM_RU['fill_age'])
    await state.set_state(FSMFillForm.fill_age)


# Handler if incorrect name was sent
@router.message(StateFilter(FSMFillForm.fill_name))
async def warning_not_name(message: Message):
    await message.answer(text=LEXICON_FILLFORM_RU['not_name'])


# Handler if age was correct
# and switch to fill_gender
@router.message(StateFilter(FSMFillForm.fill_age),
                lambda x: x.text.isdigit() and 4 <= int(x.text) <= 120)
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(age=message.text)