from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class CreateOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response({
                "status": "1",
                "response": order
            })
        return Response(serializer.errors, status=400)
