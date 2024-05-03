from aiogram.filters import CommandStart
from loader import dp
from aiogram import types
from keyboards.inline.buttons import add_group_button
from filters import *

text = "Salom alaykum bratim kanalga azo buling ", "bu guruh"




@dp.message(CommandStart(),IsPrivate())
async def start_bot(message: types.Message):
    await message.answer(text=text[0], reply_markup=add_group_button)



@dp.message(CommandStart(),IsGroup())
async def start_bot(message: types.Message):
    await message.answer(text=text[1], reply_markup=add_group_button)
















