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
    topFinGrpNo = models.TextField(null=False) # 권역 코드
    kor_co_nm = models.TextField(null=False) # 금융 회사 명
    fin_prdt_nm = models.TextField(null=False) # 금융 상품 명
    join_deny = models.TextField(null=False) # 가입 제한 여부
    mtrt_int = models.TextField(null=True) # 만기후 이자율
    max_limit = models.TextField(null=True) # 최고 한도
    join_way = models.TextField(null=True) # 가입 방법
    spcl_cnd = models.TextField(null=True) # 우대 조건
    pnsn_kind_nm = models.TextField(null=True) # 연금 종류 명
    brtm_prft_rate_1 = models.TextField(null=True) # 전년도 수익률
    brtm_prft_rate_2 = models.TextField(null=True) # 전전년도 수익률
    brtm_prft_rate_3 = models.TextField(null=True) # 전전전년도 수익률

# 가입한 상품
class JoinedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)