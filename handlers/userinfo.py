from aiogram import Router, F
from aiogram.types import Message


info_router = Router()

@info_router.message(F.text == "/my_info")
async def cmd_start(message: Message):
    await message.answer(f"ID: {message.from_user.id}\nFirst name: {message.from_user.first_name}\nLast name: {message.from_user.last_name}\nPremium: {message.from_user.is_premium}")
