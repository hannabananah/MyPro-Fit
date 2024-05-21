from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/deposit/', views.fetch_deposit),
    path('api/v1/saving/', views.fetch_saving),
    path('api/v1/annuity/', views.fetch_annuity),
    path('deposit-list/', views.deposit_list),
    path('saving-list/', views.saving_list),
    path('annuity-list/', views.annuity_list),
    path('deposit/<str:code>/', views.deposit_detail),
    path('saving/<str:code>/', views.saving_detail),
    path('annuity/<str:code>/', views.annuity_detail),
    path('deposit/<str:code>/likes/', views.deposit_likes),
]
