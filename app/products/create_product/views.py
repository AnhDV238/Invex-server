from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models.products import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "1",
                "response": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "2",
            "response": "error"
        })

