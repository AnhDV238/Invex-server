from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .sql import *
from django.db import connection
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from datetime import timedelta, date, datetime

class GetRevenue(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            time_type = request.query_params.get('timeType')
            data_type = request.query_params.get('dataType')
            now = datetime.now()

            if time_type == '0':
                today_start = datetime(now.year, now.month, now.day, 0,0,0,0)
                today_end = datetime(now.year, now.month, now.day, 23,59,59,0)
                yesterday = now - timedelta(days=1)
                yesterday_start = datetime(yesterday.year, yesterday.month, yesterday.day, 0,0,0,0)
                yesterday_end = datetime(yesterday.year, yesterday.month, yesterday.day, 23,59,59,59)

                with connection.cursor() as cursor:
                    if data_type == '0':
                        cursor.execute(GET_REVENUE, [today_start, today_end])
                        revenue_today = cursor.fetchone()[0] or 0

                        cursor.execute(GET_REVENUE, [yesterday_start, yesterday_end])
                        revenue_yesterday = cursor.fetchone()[0] or 0

                    if data_type == '1':
                        cursor.execute(GET_INVENTORY_EXPIRY_DATE, [today_start, today_end])
                        revenue_today = cursor.fetchone()[0] or 0
                        revenue_yesterday = 0

                return Response({
                    "status": "1",
                    "response": {
                        "revenue": revenue_today,
                        "revenue_before": revenue_yesterday
                    }
                })
            elif time_type == '1':  # Tháng
                first_day_this_month = datetime(now.year, now.month, 1, 0,0,0,0)
                this_month_start = first_day_this_month
                this_month_end = datetime(now.year, now.month, now.day, 23, 59, 59)

                last_day_last_month = first_day_this_month - timedelta(days=1)
                first_day_last_month = datetime(last_day_last_month.year, last_day_last_month.month, 1, 0,0,0,0)
                last_month_start = first_day_last_month
                last_month_end = datetime(last_day_last_month.year, last_day_last_month.month, last_day_last_month.day, 23, 59, 59, 59)

                first_day_next_month = datetime(now.year, now.month + 1, 1) if now.month < 12 else datetime(now.year + 1, 1, 1)
                last_day_of_month = first_day_next_month - timedelta(days=1)

                with connection.cursor() as cursor:
                    if data_type == '0':
                        cursor.execute(GET_REVENUE, [this_month_start, this_month_end])
                        revenue_this_month = cursor.fetchone()[0] or 0

                        cursor.execute(GET_REVENUE, [last_month_start, last_month_end])
                        revenue_last_month = cursor.fetchone()[0] or 0

                    if data_type == '1':
                        cursor.execute(GET_INVENTORY_EXPIRY_DATE, [now, last_day_of_month])
                        revenue_this_month = cursor.fetchone()[0] or 0
                        revenue_last_month = 0

                return Response({
                    "status": "1",
                    "response": {
                        "revenue": revenue_this_month,
                        "revenue_before": revenue_last_month
                    }
                })
        except Exception as error:
            return Response({
                "status": "2",
                "response": error
            })