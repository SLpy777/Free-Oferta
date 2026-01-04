from telebot import TeleBot, types

# Токен бота
bot = TeleBot("7666817977:AAFmJVWR-JQRPpAg2_TTp_nYQK5Un1XetBU")

# Команда /start
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("📄 Оферта", "🌐 VPS")

    welcome_text = (
        "👋 Добро пожаловать в *Shadow VPN!*\n\n"
        "🔐 Безопасный и стабильный VPN для анонимности в сети\n"
        "⚡ Высокая скорость • 🌍 Свобода доступа • 🛡 Защита данных\n\n"
        "Выберите нужный раздел ниже ⬇️"
    )

    bot.send_message(
        chat_id,
        welcome_text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

# Обработка кнопок
@bot.message_handler(func=lambda message: True)
def menu(message):
    chat_id = message.chat.id
    text = message.text

    if text == "📄 Оферта":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                "📄 Открыть оферту",
                web_app=types.WebAppInfo(
                    url="https://raw.githubusercontent.com/SLpy777/Free-Oferta/main/offer.html"
                )
            )
        )
        bot.send_message(
            chat_id,
            "📑 Публичная оферта Shadow VPN:",
            reply_markup=keyboard
        )

    elif text == "🌐 VPS":
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(
                "🌐 Открыть интерфейс VPS",
                web_app=types.WebAppInfo(
                    url="http://72.56.97.182/MiniApp/"  # твой MiniApp
                )
            )
        )
        bot.send_message(
            chat_id,
            "🖥 Панель управления VPS:",
            reply_markup=keyboard
        )

# Проверка запуска
print("✅ Бот успешно запущен. Ожидание сообщений...")

# Запуск
bot.infinity_polling()