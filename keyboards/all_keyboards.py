from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from create_bot import admins


def main_Kb(user_tg_id: int):
    kb_list = [
        [KeyboardButton(text="О нас!"), KeyboardButton(text="Профиль")],
        [KeyboardButton(text="Заполнит анкету"), KeyboardButton(text="Каталог")]             
    ]
    if user_tg_id in admins:
        kb_list.append([KeyboardButton(text="Панель админа")])
        
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Воспользуйся мной!")
    
    return keyboard

def spec_kb():
    kb_list = [
        [KeyboardButton(text="Отправить его", request_location=True)],
        [KeyboardButton(text="Поделиться номером", request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся мной!"
    )
    
    return keyboard