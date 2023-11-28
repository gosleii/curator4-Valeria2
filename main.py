import telebot

bot = telebot.TeleBot('6715966441:AAEOG3ECsj-DDsnUUZ6VwPdNsmPBhAoJCrI')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Wildberries!', parse_mode='Markdown')


@bot.message_handler(commands=['catalog'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Вот каталог товаров, доступных на Wildberries:', parse_mode='Markdown')
    bot.send_message(message.chat.id, 'большая книга по питону', parse_mode='Markdown')


@bot.message_handler(commands=['discounts'])
def main(message):
    bot.send_message(message.chat.id, 'Вот текущие акции и скидки на товары в Wildberries: купи один получи два!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['delivery'])
def main(message):
    bot.send_message(message.chat.id,
                     'Информация о доставке в Wildberries. Введите адрес для получения товара и система рассчитает стоимость доставки..',
                     parse_mode='Markdown')


bot.infinity_polling()
