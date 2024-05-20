from rest_framework import serializers
from .models import Deposit, Saving, Annuity

#  목록 조회
class DepositListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'month_6', 'month_12', 'month_24', 'month_36']
class SavingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = ['dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'month_6', 'month_12', 'month_24', 'month_36']
class AnnuityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annuity
        fields = ['dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'prdt_type_nm', 'avg_prft_rate', 'btrm_prft_rate_1', 'btrm_prft_rate_2', 'btrm_prft_rate_3']

