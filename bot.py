from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

# Замените значения ниже своими данными
source_channel_username = 'source_channel_username'
destination_channel_username = 'destination_channel_username'
bot_token = 'your_bot_token'

# Функция для получения постов из исходного канала и отправки их в другой канал
def forward_posts(update, context):
    try:
        # Получение последних 5 постов из исходного канала
        source_channel_posts = context.bot.get_chat_history(chat_id=source_channel_username, limit=5)
        
        # Отправка постов в целевой канал
        for post in source_channel_posts:
            context.bot.send_message(chat_id=destination_channel_username, text=post.text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        context.bot.send_message(chat_id=update.message.chat_id, text="Произошла ошибка при получении и отправке постов.")

# Создание и настройка бота
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Добавление обработчика команды для получения и отправки постов
forward_posts_handler = CommandHandler('forward_posts', forward_posts)
dispatcher.add_handler(forward_posts_handler)

# Запуск бота
updater.start_polling()
updater.idle()
