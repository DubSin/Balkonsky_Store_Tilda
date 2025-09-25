from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram import Bot

from currency.currency import get_currency

router = Router()


@router.callback_query(F.data == 'yuan_course')
async def currency_state(callback_query: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    currency = get_currency()
    await callback_query.message.answer(f'Текущий курс: {currency} рублей')