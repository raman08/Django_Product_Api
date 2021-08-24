from django.db import models
from Users.models import User

from Products.models import Product

# Create your models here.

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', blank=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	address = models.CharField(max_length=255)
	zipcode = models.CharField(max_length=255)
	place = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	paid_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	stripe_token = models.CharField(max_length=255)

	class Meta:
		ordering = ['-created_at',]

	def __str__(self) -> str:
		return self.first_name

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
	price = models.DecimalField(max_digits=8, decimal_places=2)
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return str(self.id)