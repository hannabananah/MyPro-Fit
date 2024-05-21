from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.EmailField(required=True, allow_blank=False)
    nickname = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "nickname": self.validated_data.get("nickname", ""),
        }


UserModel = get_user_model()


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        if hasattr(UserModel, "USERNAME_FIELD"):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, "EMAIL_FIELD"):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, "nickname"):
            extra_fields.append("nickname")
        if hasattr(UserModel, "age"):
            extra_fields.append("age")
        if hasattr(UserModel, "gender"):
            extra_fields.append("gender")
        if hasattr(UserModel, "asset"):
            extra_fields.append("asset")
        if hasattr(UserModel, "is_pension"):
            extra_fields.append("is_pension")
        if hasattr(UserModel, "is_internet"):
            extra_fields.append("is_internet")
        if hasattr(UserModel, "is_BLSR"):
            extra_fields.append("is_BLSR")
        if hasattr(UserModel, "is_free"):
            extra_fields.append("is_free")
        model = UserModel
        fields = ("pk", *extra_fields)
        read_only_fields = ("username", "email")
