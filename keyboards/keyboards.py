from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_MESSAGES_RU


def create_inline_joke_kb(width: int = 2) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    button_1 = InlineKeyboardButton(text=LEXICON_MESSAGES_RU['yes'], callback_data='yes_joke')
    button_2 = InlineKeyboardButton(text=LEXICON_MESSAGES_RU['no'], callback_data='no_joke')

    kb_builder.row(button_1, button_2, width=width)

    return kb_builder.as_markup()


def create_rating_kb(width: int = 2) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    buttons = [InlineKeyboardButton(text=str(value), callback_data=str(value))
               for value in range(1, 6)]

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()
