from rest_framework import serializers

from .models import Annuity, Deposit, Saving


#  목록 조회
class DepositListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            "dcls_month",
            "fin_prdt_cd",
            "kor_co_nm",
            "fin_prdt_nm",
            "month_6",
            "month_12",
            "month_24",
            "month_36",
            "deposit_like_users",
        ]


class SavingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = [
            "dcls_month",
            "fin_prdt_cd",
            "kor_co_nm",
            "fin_prdt_nm",
            "month_6",
            "month_12",
            "month_24",
            "month_36",
            "saving_like_users",
        ]


class AnnuityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annuity
        fields = [
            "dcls_month",
            "fin_prdt_cd",
            "kor_co_nm",
            "fin_prdt_nm",
            "prdt_type_nm",
            "avg_prft_rate",
            "btrm_prft_rate_1",
            "btrm_prft_rate_2",
            "btrm_prft_rate_3",
            "annuity_like_users",
        ]


# 상세 조회
class DepositDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = "__all__"


class SavingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = "__all__"


class AnnuityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annuity
        fields = "__all__"
