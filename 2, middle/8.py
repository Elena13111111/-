
# pip install pyTelegramBotAPI - это команда установки
# https://t.me/BotFather
# https://t.me/zlskjezihjbot
import telebot

bot = telebot.TeleBot("6082824370:AAEX7PpWGiqZYxFLg6RuUo4lMxEwQLZ_Ok0")

@bot.message_handler(content_types=['text'])
def answer(message):
	bot.send_message(message.chat.id, f'Ты написал мне: {message.text}')

bot.infinity_polling()