from django.urls import path, include
from orders.views import Order_View


urlpatterns = [
    path('', Order_View.as_view(),),
]
