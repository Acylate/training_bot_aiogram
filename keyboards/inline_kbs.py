from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text='Генерировать пользователя', callback_data='get_person')],
        [InlineKeyboardButton(text='На главную', callback_data='back_home')]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)