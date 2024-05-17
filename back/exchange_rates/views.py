from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json
from datetime import datetime
from django.utils.dateformat import DateFormat

# 환율 가져오는 api
SECRET_KEY = settings.SECRET_KEY
@api_view(['GET'])
def today_exchange_rate(request):
    max_retries = 7  # 최대 7일 전까지 시도
    retries = 0
    today_datetime = datetime.now()
    while retries < max_retries:
        today = DateFormat(today_datetime).format('Ymd')
        url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/'
        params = {
            'authkey': SECRET_KEY,
            'data': 'AP01',
            'searchdate': today
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            response_json = response.json()
            if response_json:  # 비어 있지 않으면 데이터를 반환
                return Response(response_json)

        # 데이터를 찾지 못한 경우 하루 전으로 이동
        today_datetime -= timedelta(days=1)
        retries += 1
    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)
