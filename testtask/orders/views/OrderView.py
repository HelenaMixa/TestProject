from django.views.generic import TemplateView
from orders.models import Order


class Order_View(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        return {
            'orders': [
                {
                    'id': order.serial_number,
                    'order_number': order.booking_id,
                    'cost_usd': order.cost_usd,
                    'cost_rub': order.cost_uah,
                    'delivery_time': order.delivery_time,
                }
                for order in Order.objects.all().order_by('serial_number')
            ],
        }
