from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from django.core.cache import cache


class CreateProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        cache_products = cache.get('products')
        if cache_products:
            return Response(cache_products, status=status.HTTP_200_OK)
        products = Product.objects.all()
        cache.set('products', products, 600)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete('products')

    def perform_update(self, serializer):
        serializer.save()
        cache.delete('products')
