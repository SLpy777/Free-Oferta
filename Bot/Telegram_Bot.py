from telebot import TeleBot, types

# Вставь сюда токен своего бота
bot = TeleBot("7666817977:AAFmJVWR-JQRPpAg2_TTp_nYQK5Un1XetBU")  

# Команда /start
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📄 Оферта", "🌐 VPS")
    bot.send_message(chat_id, "Привет! Выберите действие:", reply_markup=keyboard)

# Обработка нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def menu(message):
    chat_id = message.chat.id
    text = message.text

    if text == "📄 Оферта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                "Открыть оферту",
                web_app=types.WebAppInfo(
                    url="https://SLpy777.github.io/Free-Oferta/offer.html"
                )
            )
        )
        bot.send_message(chat_id, "Откройте оферту:", reply_markup=keyboard)

    elif text == "🌐 VPS":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                "Открыть интерфейс VPS",
                web_app=types.WebAppInfo(
                    url="http://127.0.0.1:5500/MiniApp/index.html"  # заменишь на свой MiniApp позже
                )
            )
        )
        bot.send_message(chat_id, "Интерфейс VPS:", reply_markup=keyboard)

# Сообщение в терминал для проверки запуска
print("Бот запущен, polling стартует...")

# Запуск бота
bot.infinity_polling()