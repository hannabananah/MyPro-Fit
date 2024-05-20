from django.urls import include, path
from .views import DeleteAccountView,PasswordResetView,CustomPasswordResetConfirmView

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path('', include('dj_rest_auth.registration.urls')),
    path('', include('allauth.urls')),
   path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('signup/', include('dj_rest_auth.registration.urls')),
    # path('userinfo/', view=views.userinfo),
    path("delete/", DeleteAccountView.as_view()),
]
