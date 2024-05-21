from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field, user_username
from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]


class User(AbstractUser):
    username = models.EmailField(unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=50, default="unknown")
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    asset = models.IntegerField(null=True)
    is_pension = models.BooleanField(null=True)
    is_internet = models.BooleanField(null=True)
    is_BLSR = models.BooleanField(null=True)
    is_free = models.BooleanField(null=True)
    email = models.EmailField(unique=True, null=True, blank=True)


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        nickname = data.get("nickname")
        age = data.get("age")
        gender = data.get("gender")
        asset = data.get("asset")
        is_pension = data.get("is_pension")
        is_internet = data.get("is_internet")
        is_BLSR = data.get("is_BLSR")
        is_free = data.get("is_free")
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        if age:
            user_field(user, "age", age)
        if gender:
            user_field(user, "gender", gender)
        if asset:
            user_field(user, "asset", asset)
        if is_pension:
            user_field(user, "is_pension", is_pension)
        if is_internet:
            user_field(user, "is_internet", is_internet)
        if is_BLSR:
            user_field(user, "is_BLSR", is_BLSR)
        if is_free:
            user_field(user, "is_free", is_free)
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
