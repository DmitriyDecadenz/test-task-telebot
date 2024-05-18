from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='/add')],
                                     [KeyboardButton(text='/tsk')],],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')
