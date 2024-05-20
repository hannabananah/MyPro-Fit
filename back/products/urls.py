from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/deposit/', views.fetch_deposit),
    path('api/v1/saving/', views.fetch_saving),
    path('api/v1/annuity/', views.fetch_annuity),
    path('list/', views.product_list)
]
