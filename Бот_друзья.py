import telebot
from telebot import types

bot = telebot.TeleBot('5653834366:AAEjt6fkeR5U7KB8Js0qGNDceSHO2Ob48xA')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Приветствую, {message.from_user.first_name}!'
    bot.send_message(message.chat.id, mess, parse_mode = 'html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=3)
    Dmitr = types.KeyboardButton('Дмитрий')
    Anas = types.KeyboardButton('Анастасия Д')
    Konst = types.KeyboardButton('Константин')
    Ura = types.KeyboardButton('Юрий')
    Nast = types.KeyboardButton('Анастасия Ю')
    Evg = types.KeyboardButton('Евгений')
    Dian = types.KeyboardButton('Диана')
    Alex = types.KeyboardButton('Алексей')
    Poli = types.KeyboardButton('Полина')
    Dania = types.KeyboardButton('Данил')
    Elis = types.KeyboardButton('Елизавета')
    Dav = types.KeyboardButton('Давид')
    Vlad = types.KeyboardButton('Владислав')
    Vika = types.KeyboardButton('Виктория')
    markup.add(Dmitr, Anas, Konst, Ura, Nast, Evg, Dian, Alex, Poli, Dania, Elis, Dav, Vlad, Vika)
    bot.send_message(message.chat.id, "Выберите нужного пользователя", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    markup = types.InlineKeyboardMarkup()
    if message.text == 'Дмитрий':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/dmitriy_l_0_0'))
        bot.send_message(message.chat.id, "Дмитрий Алексеевич \n22 года \nДень рождения 12.05", reply_markup=markup)
        photo = open('Я.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Анастасия Д':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/id145454257'))
        bot.send_message(message.chat.id, "Анастасия Сергеевна \n21 год \nДень рождения 13.04", reply_markup=markup)
    elif message.text == 'Константин':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/kosta_chel'))
        bot.send_message(message.chat.id, "Константин Сергеевич \n22 года \nДень рождения 27.10", reply_markup=markup)
        photo = open('Старый.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Юрий':
        markup.add(types.InlineKeyboardButton('Перейдите на страницу', url='https://vk.com/dobleer'))
        bot.send_message(message.chat.id, "Юрий Евгеньевич \n20 год \nДень рождения 04.03 год \nДень рождения 13.04", reply_markup=markup)
        photo = open('Юрка.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Анастасия Ю':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/lalisavi'))
        bot.send_message(message.chat.id, "Анастасия Андреевна \n18 год \nДень рождения 16.02", reply_markup=markup)
    elif message.text == 'Евгений':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/vlaadik_a'))
        bot.send_message(message.chat.id, "Евгений Сергеевич \n22 год \nДень рождения 27.12", reply_markup=markup)
        photo = open('Жека.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Диана':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/littledinn'))
        bot.send_message(message.chat.id, "Дианы \n22 год \nДень рождения 10.05", reply_markup=markup)
    elif message.text == 'Алексей':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/rmk890'))
        bot.send_message(message.chat.id, "Алексея Юрьевич \n21 год \nДень рождения 25.10", reply_markup=markup)
        photo = open('Леха.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Полина':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/id104947270'))
        bot.send_message(message.chat.id, "Полина  \n22 года \nДень рождения 04.10", reply_markup=markup)
    elif message.text == 'Данил':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/id272541694'))
        bot.send_message(message.chat.id, "Данил Дмитриевич \n21 год \nДень рождения 29.09", reply_markup=markup)
        photo = open('Даня.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Елизавета':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/elkul'))
        bot.send_message(message.chat.id, "Елизавета Ильинична \n19 лет \nДень рождения 02.02", reply_markup=markup)
    elif message.text == 'Давид':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/tuchin_david'))
        bot.send_message(message.chat.id, "Давид Вадимович \n26 лет \nДень рождения 31.10", reply_markup=markup)
        photo = open('Давид.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Владислав':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/mssvyat'))
        bot.send_message(message.chat.id, "Владислав Максимович \n21 год \nДень рождения 27.09", reply_markup=markup)
        photo = open('Влад.jpg', 'rb')
        bot.send_photo(message.chat.id, photo, parse_mode = 'html')
    elif message.text == 'Виктория':
        markup.add(types.InlineKeyboardButton('Посетить страницу', url='https://vk.com/demawwww'))
        bot.send_message(message.chat.id, "Виктория \n20 лет \nДень рождения 07.06", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode = 'html')

bot.polling(none_stop = True)

