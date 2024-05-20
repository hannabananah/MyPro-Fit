from rest_framework import serializers
from .models import Product

# 상품 목록 조회
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'month_6', 'month_12', 'month_24', 'month_36']

# 연금 저축 목록 조회
class PrdtListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['dcls_month', 'kor_co_nm', 'fin_prdt_nm', 'prdt_type_nm', 'avg_prft_rate', 'btrm_prft_rate_1', 'btrm_prft_rate_2', 'btrm_prft_rate_3']

