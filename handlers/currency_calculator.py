from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Bot
import math

from keyboards.currency_keyboard import get_currency_kb
from currency.currency import get_currency

router = Router()

class CurrencyState(StatesGroup):
    yuan = State()
    rubbles = State()


@router.callback_query(F.data == 'currency_calculator')
async def currency_state(callback_query: CallbackQuery, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer('Выберете валюту: ', reply_markup=get_currency_kb())


@router.callback_query(F.data == 'yuan_currency')
async def yuan_start(callback_query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer('Введите валюту в юанях')
    await state.set_state(CurrencyState.yuan)


@router.callback_query(F.data == 'rubbles_currency')
async def rubbles_start(callback_query: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.answer_callback_query(callback_query.id)
    await callback_query.message.answer('Введите валюту в рублях')
    await state.set_state(CurrencyState.rubbles)


@router.message(CurrencyState.yuan)
async def yuan_calculator(message: Message, state: FSMContext):
    print(message.text.isdigit(), message.text)
    if message.text.isdigit():
        await state.update_data(yuan=message.text)
        data = await state.get_data()
        currency = get_currency()
        price = int(data['yuan']) * currency
        await message.answer(f'{price} рублей')
        await state.clear()
    else:
        await state.clear()
        await message.answer('Введено не число')


@router.message(CurrencyState.rubbles)
async def rubbles_calculator(message: Message, state: FSMContext):
    print(message.text.isdigit(), message.text)
    if message.text.isdigit():
        await state.update_data(rubbles=message.text)
        data = await state.get_data()
        currency = get_currency()
        price = round(int(data['rubbles']) / currency, 3)
        await message.answer(f'{price} юаней')
        await state.clear()
    else:
        await state.clear()
        await message.answer('Введено не число')




