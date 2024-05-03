from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import BOT

add_group_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Add group", url=f"https://t.me/{BOT}?startgroup=true")
        ]
    ]


)














