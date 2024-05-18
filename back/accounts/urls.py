from django.urls import include, path

from .views import DeleteAccountView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("signup/", include("dj_rest_auth.registration.urls")),
    path("delete/", DeleteAccountView.as_view(), name="account-delete"),
]
