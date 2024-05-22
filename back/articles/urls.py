from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comments/', views.comments),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment),
]
