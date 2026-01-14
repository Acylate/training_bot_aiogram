from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from keyboards.all_keyboards import main_kb, spec_kb
from keyboards.inline_kbs import ease_link_kb
from utils.my_utils import get_random_person

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()', reply_markup=main_kb(message.from_user.id))
    
@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()', reply_markup=spec_kb())
    
@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Запуск сообщения по команде /start_3 используя фильтр F.text')
    
@start_router.message(F.text == 'Инлайн')
async def get_inline_btn_link(message: Message):
    await message.answer('Инлайн', reply_markup=ease_link_kb())
    
@start_router.callback_query(F.data == 'get_person')
async def send_random_person(call: CallbackQuery):
    user = get_random_person()
    formatted_message = (
        f"👤 Имя: {user['name']}\n"
        f"🏠 Адрес: {user['address']}\n"
        f"📧 Email: {user['email']}\n"
        f"📞 Телефон: {user['phone_number']}\n"
        f"🎂 Дата рождения: {user['birth_date']}\n"
        f"🏢 Компания: {user['company']}\n"
        f"💼 Должность: {user['job']}\n"
    )
    
    await call.message.answer(formatted_message)