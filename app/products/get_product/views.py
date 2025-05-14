from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from products.models.products import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from .sql import *
from rest_framework.permissions import IsAuthenticated

class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(GET_PRODUCTS, [10])
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in rows]
            return Response({
                "status": "1",
                "response": data
            })