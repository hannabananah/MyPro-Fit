from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from products.models import Annuity, Deposit, Saving


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

class UserProductSerializer(serializers.ModelSerializer):
    class DepositSerizer(serializers.ModelSerializer):
        class Meta:
            model = Deposit
            fields = '__all__'
        
    deposit_join_products = DepositSerizer(many=True)

    class SavingSerizer(serializers.ModelSerializer):
        class Meta:
            model = Saving
            fields = '__all__'
    saving_join_products = SavingSerizer(many=True)


    class AnnuitySerizer(serializers.ModelSerializer):
        class Meta:
            model = Annuity
            fields = '__all__'
    annuity_join_products = AnnuitySerizer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('nickname', 'username', 'annuity_join_products', 'saving_join_products', 'deposit_join_products',)