from django.urls import path
from .views import ProductAPIView, ProductRetriveUpdateDestroyAPIView, CreateProductAPIView


urlpatterns = [
    path('products', ProductAPIView.as_view(), name="products"),
    path('product/<int:pk>/',
         ProductRetriveUpdateDestroyAPIView.as_view(), name='product'),
    path('create/', CreateProductAPIView.as_view(), name='create')
]
