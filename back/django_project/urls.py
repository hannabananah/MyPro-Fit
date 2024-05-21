from django.contrib import admin
from django.urls import include, path

from accounts.views import DeleteAccountView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("articles.urls")),
    path("articles/", include("articles.urls")),
    path("products/", include("products.urls")),
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/signup/", include("dj_rest_auth.registration.urls")),
    path("accounts/delete/", DeleteAccountView.as_view()),
    path("exchange-rate/", include("exchange_rates.urls")),
]
