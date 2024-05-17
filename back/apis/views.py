from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json

# Create your views here.
SECRET_KEY = settings.SECRET_KEY
@api_view(['GET'])
def exchange_rate(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/'
    params = {
        'authkey': SECRET_KEY,
        'data': 'AP01',
        'searchdate':'20240514'
    }
    response = requests.get(url, params=params)
    products_data = response.json()
    print(response.text)
    return Response(products_data)
