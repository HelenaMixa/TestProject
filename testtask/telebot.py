# TOKEN = "5532049646:AAHBev5EvdCh-6OHUDkf2wZtZSp4g8SQC4A"
# CHAT_ID = 5124150975

import os
import telebot
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testtask.settings")
django.setup()

from orders.models import User

# bot = telebot.TeleBot('5344051604:AAHl0HVkNG6UEX0h0DYR7nqnwPTSnKanzwI')
bot = telebot.TeleBot('5532049646:AAHBev5EvdCh-6OHUDkf2wZtZSp4g8SQC4A')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Ежедневно в 10:00 будут приходить заказы, у которых закончился срок поставки')
    User.objects.create(telegram_id=m.chat.id)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
