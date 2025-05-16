from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import connection
from .sql import *

class GetOrderItemAll(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        limit = request.query_params.get("limit", 20)
        with connection.cursor() as cursor:
            cursor.execute(GET_ALL_ORDER, [limit])
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in rows]
            return Response({
                "status": "1",
                "response": data
            })