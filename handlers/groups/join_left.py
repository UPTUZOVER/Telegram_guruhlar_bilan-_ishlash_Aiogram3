from aiogram import F, types, html
from loader import *
from filters import IsGroup
@dp.message(F.new_chat_members, IsGroup())
async def new_member(message: types.Message):
    join = message.new_chat_members
    member = ", ".join([html.link(value=f"{m.first_name}", link=f"tg://user?id={m.id}") for m in join])
    aw
    await message.answer(f"Hello {member}!")


@dp.message(F.left_chat_members, IsGroup())
async def left_member(message: types.Message):
    join = message.left_chat_members
    member = html.link(value=f"{join.first_name}", link=f"tg://user?id={join.id}")
    await message.answer(f"{member} guruhni tark etdi!")





