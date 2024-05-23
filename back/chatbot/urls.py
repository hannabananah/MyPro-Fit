from django.urls import path
from . import views

urlpatterns = [
    path("", views.chatbot),
    path("commend/", views.chatbot_commend),
]
