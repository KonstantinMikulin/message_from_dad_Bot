from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


storage = MemoryStorage()

user_dict: dict[int, dict[str, str | int | bool]] = {}
user_dict_booking: dict[int, dict[str, str | int | bool]] = {}


# FSM state group for filling form
class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_gender = State()
    upload_photo = State()


# FSM state group for booking
class FSMBooking(StatesGroup):
    pick_date = State()  # key: date
    pick_time = State()  # key: time
    fill_name = State()  # key: name
    fill_phone_number = State()  # key: phone_number
    payment = State()  # key: payment
    sum_data = State()
    confirmation = State()
