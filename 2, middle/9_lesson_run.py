# pip install pyTelegramBotAPI - это команда установки
# https://t.me/BotFather
# https://t.me/zlskjezihjbot
# /start  -начинаем с ботом
import telebot
import lesson_9_Game_telegram

bot = telebot.TeleBot("6082824370:AAEX7PpWGiqZYxFLg6RuUo4lMxEwQLZ_Ok0")

CURRENT_PLAYER = ['X'] # скобки нужны, чтобы менять данные. А переменную нельзя менять CURRENT_PLAYER[0]


@bot.message_handler(commands=['start']) # /start  -начинаем с ботом
def start_game(message):
	lesson_9_Game_telegram.clear_data() # очищаем поле от предыдущей игры
	bot.send_message(message.chat.id, "Новая игра началась")
	bot.send_message(message.chat.id, lesson_9_Game_telegram.print_game_field()) # отправка сообщений в телеграме
	bot.send_message(message.chat.id, f'Ваш ход: {CURRENT_PLAYER[0]}')

# техника для хода в телеграмме
@bot.message_handler(content_types=['text'])
def start_game(message):
	bot.send_message(
		message.chat.id,
		lesson_9_Game_telegram.input_value(message.text, CURRENT_PLAYER[0]) # делаем ход
	)
	if lesson_9_Game_telegram.check_is_game_end() == lesson_9_Game_telegram.STATUS_CONTINUE: # проверяем игру,статус игры
		bot.send_message(
			message.chat.id,
			lesson_9_Game_telegram.print_game_field()
		)
		if CURRENT_PLAYER[0] == 'X':
			CURRENT_PLAYER[0] = 'O'
		else:
			CURRENT_PLAYER[0] = 'X'
		bot.send_message(
			message.chat.id,
			f'Сейчас ходит: {CURRENT_PLAYER[0]}'
		)
	else:
		bot.send_message(message.chat.id, f'Игра закончена, победа: {lesson_9_Game_telegram.check_is_game_end()}')


bot.infinity_polling()
