from django.urls import path, include

from .views import LatestProductsList

urlpatterns = [
	path('latest-products', LatestProductsList.as_view())
]