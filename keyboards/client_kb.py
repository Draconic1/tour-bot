from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # , ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Посмотреть_туры')
b4 = KeyboardButton('/Завершить')
'''b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где я', request_location=True)'''

kb_client = ReplyKeyboardMarkup(resize_keyboard=True) #, one_time_keyboard=True)

kb_client.row(b1, b2).row(b3, b4)
