from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat

# Create your views here.
PRODUCT_KEY = settings.PRODUCT_KEY
@api_view(['GET'])
def product_list(request):
    pass