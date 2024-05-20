from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

# 금융 상품
class Product(models.Model):
    OPTION_ONE = 1
    OPTION_TWO = 2
    OPTION_THREE = 3
    OPTION_CHOICES = [
        (OPTION_ONE, '정기 예금 상품'),
        (OPTION_TWO, '적금 상품'),
        (OPTION_THREE, '연금 저축 상품'),
    ]
    type = models.IntegerField(choices=OPTION_CHOICES) # 상품 코드
    dcls_month = models.TextField(null=False) # 공시제출월
    fin_co_no = models.TextField(null=False) # 금융 회사 코드
    fin_prdt_cd = models.TextField(null=False) # 금융 상품 코드
    kor_co_nm = models.TextField(null=False) # 금융 회사 명
    fin_prdt_nm = models.TextField(null=False) # 금융 상품 명
    join_deny = models.TextField(null=True) # 가입 제한 여부
    mtrt_int = models.TextField(null=True) # 만기후 이자율
    max_limit = models.TextField(null=True) # 최고 한도
    join_way = models.TextField(null=True) # 가입 방법
    spcl_cnd = models.TextField(null=True) # 우대 조건
    pnsn_kind_nm = models.TextField(null=True) # 가입 유형명
    btrm_prft_rate_1 = models.FloatField(null=True) # 전년도 수익률
    btrm_prft_rate_2 = models.FloatField(null=True) # 전전년도 수익률
    btrm_prft_rate_3 = models.FloatField(null=True) # 전전전년도 수익률
    # 연금
    prdt_type_nm = models.TextField(null=True) # 상품 유형명 (연금)
    avg_prft_rate = models.FloatField(null=True) # 평균 수익률 (연금)
    # 옵션
    month_6 = models.FloatField(null=True) # 6 개월 금리
    month_12 = models.FloatField(null=True) # 12 개월 금리
    month_24 = models.FloatField(null=True) # 24 개월 금리
    month_36 = models.FloatField(null=True) # 36 개월 금리
    # 유저
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products') # 장바구니 한 유저
    joined_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='join_products') # 가입한 유저
