from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.menu_keyboard import get_menu_kb

router = Router()

from dotenv import load_dotenv, find_dotenv
import json
import os

load_dotenv(find_dotenv())

@router.message(Command(commands='start'))
async def menu_handler(message: Message):
    await message.reply('Добро пожаловать в Balkonskiy Store', reply_markup=get_menu_kb())