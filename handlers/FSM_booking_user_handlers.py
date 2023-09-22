from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from phonenumbers import parse, is_valid_number

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


# Handler if name was incorrect
@router.message(StateFilter(FSMBooking.fill_name))
async def warning_not_name(message: Message):
    await message.answer(text=LEXICON_BOOKING_RU['not_name'])


# Handler if phone number was correct
@router.message(StateFilter(FSMBooking.fill_phone_number),
                lambda x: is_valid_number(parse(x.data)))
async def process_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer(text=LEXICON_BOOKING_RU['payment'])
    await state.set_state(FSMBooking.payment)


# Handler if phone number was incorrect
@router.message(StateFilter(FSMBooking.fill_phone_number))
async def warning_not_phone_number(message: Message):
    await message.answer(text=LEXICON_BOOKING_RU['not_phone_number'])


# Handler if payment was correct
@router.message(StateFilter(FSMBooking.payment), F.data.split(':').isdigit())
async def process_payment(message: Message, state: FSMContext):
    await state.update_data(payment=True)
    await message.answer(text=LEXICON_BOOKING_RU['sum_data'])
    user_dict_booking[message.from_user.id] = await state.get_data()
    await message.answer(text=f'Дата: {user_dict_booking[message.from_user.id]["date"]}\n'
                              f'Время: {user_dict_booking[message.from_user.id]["time"]}\n'
                              f'Имя: {user_dict_booking[message.from_user.id]["name"]}\n'
                              f'Номер телефона: {user_dict_booking[message.from_user.id]["phone_number"]}\n'
                              f'Оплачено: {user_dict_booking[message.from_user.id]["payment"]}'
                         )
