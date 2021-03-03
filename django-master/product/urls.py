from django.urls import path
from .views import ProductView

urlpatterns = [
	path('add/', ProductView.as_view(), name='product-add'),
]
