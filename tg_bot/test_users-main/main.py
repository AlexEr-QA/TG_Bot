import random
import string
import telebot
import os

# Получаем токен
token = ''

# Создаем объект бота
bot = telebot.TeleBot(token)

all_chars = string.ascii_letters + string.digits + '!@#$%^&*()'

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('Generate Password'), telebot.types.KeyboardButton('Exit'))
    bot.send_message(message.chat.id, 'Привет! Я генератор паролей. Просто выбери одну из опций ниже:', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Generate Password')
def generate_password(message):
    length = random.randint(8, 16)
    password = ''.join(random.choice(all_chars) for _ in range(length))
    bot.send_message(message.chat.id, f'Ваш сгенерированный пароль: {password}')

@bot.message_handler(func=lambda message: message.text == 'Exit')
def exit_command(message):
    bot.send_message(message.chat.id, 'Пока! Возвращайся ещё.')

def main():
    try:
        bot.polling()
    except Exception as e:
        print(f'Произошла ошибка: {e}')

if __name__ == '__main__':
    main()