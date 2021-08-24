import stripe

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import serializers, status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer
# Create your views here.

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
	serializer = OrderSerializer(data=request.data)

	if serializer.is_valid():
		# stripe.api_key = settings.STRIPE_SECRET_KEY
		paid_ammount = sum(item.get('quantity')*item.get('product').price for item in serializer.validated_data['items'])

		try:
			# charge = stripe.Charge.create(
			# 	ammount=int(paid_ammount*100),
			# 	currency='USD',
			# 	description='Charging for the shopping',
			# 	source=serializer.validated_data['stripe_token']
			# )
			serializer.save(user=request.user, paid_price=paid_ammount)

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		except Exception:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]

	def get(self, requst, format=None):
		orders = Order.objects.filter(user=requst.user)
		serializer = MyOrderSerializer(orders, many=True)
		return Response(serializer.data, status.HTTP_200_OK)