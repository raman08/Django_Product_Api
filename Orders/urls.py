from django.urls import path

from Orders.views import checkout, OrdersList

urlpatterns = [
	path('checkout/', checkout, name='Checkout'),
	path('orders/', OrdersList.as_view(), name='Orders'),
]