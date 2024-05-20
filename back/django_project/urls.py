from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("articles/", include("articles.urls")),
    path("products/", include("products.urls")),
    path("accounts/", include("accounts.urls")),
    path('exchange-rate/', include('exchange_rates.urls'))
]
