from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo

def get_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Курс Юаня", callback_data='yuan_course')
    kb.button(text="Магазин", web_app=WebAppInfo(url='https://project14286403.tilda.ws/'))
    kb.button(text="Кулькулятор валют", callback_data='currency_calculator')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)