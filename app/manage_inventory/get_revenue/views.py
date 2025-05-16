from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .sql import *
from django.db import connection
from rest_framework.response import Response
from django.utils.dateparse import parse_date

class GetRevenue(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            time_start = request.query_params.get('timeStart')
            time_end = request.query_params.get('timeEnd')
        except Exception as error:
            return Response({
                "status": "2",
                "response": "error"
            })

        with connection.cursor() as cursor:
            cursor.execute(GET_REVENUE, [time_start, time_end])
            data = cursor.fetchone()[0]
            return Response({
                "status": "1",
                "response": data
            })