from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
]
