from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_currency_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Рубли", callback_data='rubbles_currency')
    kb.button(text="Юань", callback_data='yuan_currency')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)