from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_MESSAGES_RU, LEXICON_STICKERS
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state

router = Router()


# Handlers for any messages beside states
@router.message(StateFilter(default_state))
async def process_any_message(message: Message):
    await message.answer(text=LEXICON_MESSAGES_RU['say_what'])
    await message.answer_sticker(sticker=LEXICON_STICKERS['say_what_sticker'])
    await message.forward(chat_id=828900493)
