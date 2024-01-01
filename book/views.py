from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status


class BookAPIView(APIView):
    serializer_class = BookSerializer

    @method_decorator(cache_page(60*5))
    def get(self, request, id):
        cache_data = cache.get('books')
        if cache_data is not None:
            return Response(cache_data, status=status.HTTP_200_OK)
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)
        cache.set('books', serializer.data, 60*5)
        return Response(serializer.data, status=status.HTTP_200_OK)
