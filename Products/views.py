from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from  .serializers import ProductSerializer
from .models import Product

# Create your views here.

class LatestProductsList(APIView):
	def get(self, request, formate=None):
		products = Product.objects.all()[0:4]
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)