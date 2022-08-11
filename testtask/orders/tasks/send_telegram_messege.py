from django.utils import timezone
from testtask.celery import app
from orders.models import User
from orders.models import Order
from telebot import bot


@app.task
def sent_telegram_messege():
    orders_list_delivery_time_end = Order.objects.filter(delivery_time=timezone.now().date()).values_list('booking_id')
    users_list_id = User.objects.values_list('telegram_id')
    if orders_list_delivery_time_end == []:
        for user_id in users_list_id:
            bot.send_message(user_id[0],
                             "Нет заказов у которых заканчивается срок поставки")

    else:
        str_orders_list_delivery_time_end = 'Заканчивается срок поставки\n'
        for order_delivery_time_end in orders_list_delivery_time_end:
            str_orders_list_delivery_time_end = str_orders_list_delivery_time_end + str(
                order_delivery_time_end[0]) + "\n"
        for user_id in users_list_id:
            bot.send_message(user_id[0], str_orders_list_delivery_time_end)
            print(orders_list_delivery_time_end)

# settings.TOKEN = "5532049646:AAHBev5EvdCh-6OHUDkf2wZtZSp4g8SQC4A"
# settings.TELEGRAM_CHAT_IDS = [5124150975, ]
