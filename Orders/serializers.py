from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem
from Products.serializers import ProductSerializer

class MyOrderItemSerializer(ModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = OrderItem
		fields = (
			'price',
			'product',
			'quantity'
		)

class MyOrderSerializer(ModelSerializer):

	items = MyOrderItemSerializer(many=True)

	class Meta:
		model = Order
		fields = (
			'user',
			'first_name',
			'last_name',
			'email',
			'address',
			'zipcode',
			'place',
			'phone_number',
			'created_at',
			'paid_price',
			'stripe_token',
			'items',
			'paid_price'
		)

class OrderItemSerializer(ModelSerializer):
	class Meta:
		model = OrderItem
		fields = (
			'price',
			'product',
			'quantity'
		)


class OrderSerializer(ModelSerializer):

	items = OrderItemSerializer(many=True)

	class Meta:
		model = Order
		fields = (
			'user',
			'first_name',
			'last_name',
			'email',
			'address',
			'zipcode',
			'place',
			'phone_number',
			'created_at',
			'paid_price',
			'stripe_token',
			'items',
		)

	def create(self, validated_data):
		items_data = validated_data.pop('items')

		try:
			order = Order.objects.create(**validated_data)
		except Exception as e:
			print(e)

		for item_data in items_data:
			OrderItem.objects.create(order=order, **item_data)

		return order