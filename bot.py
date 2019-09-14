import telebot

bot = telebot.TeleBot('')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Hi', 'Bye')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, you just start this bot', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, 'Hello my friend')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Bye my friend. See you soon')
    elif message.text.lower() == 'i love you':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else:
        bot.send_message(message.chat.id, 'Hahahha, nice joke')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
