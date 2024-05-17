from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/stop')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='/prof')
button6 = types.KeyboardButton(text='/Погода по городам')


keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6]
]


keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
