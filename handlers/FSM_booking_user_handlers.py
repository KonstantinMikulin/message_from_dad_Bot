from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from FSM.fsm import FSMBooking, user_dict_booking
from lexicon.lexicon import LEXICON_BOOKING_RU

router = Router()


# Handler for beginning booking
@router.message(Command(commands=['booking']), StateFilter(default_state))
async def process_booking_cmd(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_BOOKING_RU['pick_date'])
    await state.set_state(FSMBooking.pick_date)


# Handler if name was correct and switch to pick_time state
@router.message(StateFilter(FSMBooking.pick_date), F.data.slplit(':').isdigit())
async def process_picked_data(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer(text=LEXICON_BOOKING_RU['pick_time'])
    await state.set_state(FSMBooking.pick_time)


# Handler if date was incorrect
@router.message(StateFilter(FSMBooking.pick_date))
async def warning_not_date(message: Message):
    await message.answer(text=LEXICON_BOOKING_RU['not_date'])


# Handler if time was correct and switch to fill_name state
@router.message(StateFilter(FSMBooking.pick_time), F.data.split(':').isdigit())
async def process_sent_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(text=LEXICON_BOOKING_RU['fill_name'])
    await state.set_state(FSMBooking.fill_name)


# Handler if time was incorrect
@router.message(StateFilter(FSMBooking.pick_time))
async def warning_not_time(message: Message):
    await message.answer(text=LEXICON_BOOKING_RU['not_time'])


# Handler if name was correct and switch to fill_phone_number
@router.message(StateFilter(FSMBooking.fill_name),
                lambda x: x.text.split().isalpha and 3 < x.text.split() < 55)
async def process_sent_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_BOOKING_RU['fill_phone_number'])
    await state.set_state(FSMBooking.fill_phone_number)



































