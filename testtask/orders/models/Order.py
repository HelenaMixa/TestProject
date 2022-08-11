from django.db import models


class Order(models.Model):
    serial_number = models.PositiveSmallIntegerField(default=0, null=False)
    booking_id = models.CharField = models.IntegerField(default=0, null=False, unique=True)
    cost_usd = models.DecimalField(default=0, null=False, max_digits=10, decimal_places=2)
    cost_uah = models.DecimalField(default=0, null=False, max_digits=10, decimal_places=2)
    delivery_time = models.DateField(null=False)

    message_to_telegram_sent = models.BooleanField(default=False)

    class Meta:
        ordering = ('serial_number', )
