from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU, STICKERS_DICT

router = Router()


# Handlers for any messages beside states
@router.message()
async def process_any_message(message: Message):
    await message.answer(text=LEXICON_RU['say_what'])
    await message.answer_sticker(sticker=STICKERS_DICT['say_what_sticker'])
