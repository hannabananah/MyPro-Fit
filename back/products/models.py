from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


# 금융 상품
class Deposit(models.Model):
    dcls_month = models.TextField(null=False)  # 공시제출월
    fin_co_no = models.TextField(null=False)  # 금융 회사 코드
    fin_prdt_cd = models.TextField(null=False)  # 금융 상품 코드
    kor_co_nm = models.TextField(null=False)  # 금융 회사 명
    fin_prdt_nm = models.TextField(null=False)  # 금융 상품 명
    join_deny = models.TextField(null=True, blank=True)   # 가입 제한 여부
    join_member = models.TextField(null=True, blank=True)   # 가입 대상
    mtrt_int = models.TextField(null=True, blank=True)   # 만기후 이자율
    max_limit = models.TextField(null=True, blank=True)   # 최고 한도
    join_way = models.TextField(null=True, blank=True)   # 가입 방법
    spcl_cnd = models.TextField(null=True, blank=True)   # 우대 조건
    # 옵션
    month_6 = models.FloatField(null=True, blank=True)   # 6 개월 금리
    month_12 = models.FloatField(null=True, blank=True)   # 12 개월 금리
    month_24 = models.FloatField(null=True, blank=True)   # 24 개월 금리
    month_36 = models.FloatField(null=True, blank=True)   # 36 개월 금리
    # 유저
    deposit_like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="deposit_like_products", blank=True
    )  # 장바구니 한 유저
    deposit_joined_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="deposit_join_products", blank=True
    )  # 가입한 유저
    # 필터링을 위한 필드
    age_filter = models.IntegerField(null=True, blank=True,  default=0)
    gender_filter = models.TextField(null=True, blank=True,  default='')
    BLSR_filter = models.TextField(null=True, blank=True,  default='')
    internet_filter = models.BooleanField(null=True, blank=True)

class Saving(models.Model):
    dcls_month = models.TextField(null=False)  # 공시제출월
    fin_co_no = models.TextField(null=False)  # 금융 회사 코드
    fin_prdt_cd = models.TextField(null=False)  # 금융 상품 코드
    kor_co_nm = models.TextField(null=False)  # 금융 회사 명
    fin_prdt_nm = models.TextField(null=False)  # 금융 상품 명
    join_deny = models.TextField(null=True, blank=True)   # 가입 제한 여부
    join_member = models.TextField(null=True, blank=True)   # 가입 대상
    mtrt_int = models.TextField(null=True, blank=True)   # 만기후 이자율
    max_limit = models.TextField(null=True, blank=True)   # 최고 한도
    join_way = models.TextField(null=True, blank=True)   # 가입 방법
    spcl_cnd = models.TextField(null=True, blank=True)   # 우대 조건
    # 옵션
    month_6 = models.FloatField(null=True, blank=True)   # 6 개월 금리
    month_12 = models.FloatField(null=True, blank=True)   # 12 개월 금리
    month_24 = models.FloatField(null=True, blank=True)   # 24 개월 금리
    month_36 = models.FloatField(null=True, blank=True)   # 36 개월 금리
    # 유저
    saving_like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="saving_like_products", blank=True
    )  # 장바구니 한 유저
    saving_joined_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="saving_join_products", blank=True
    )  # 가입한 유저
    # 필터링을 위한 필드
    age_filter = models.IntegerField(null=True, blank=True,  default=0)
    gender_filter = models.TextField(null=True, blank=True,  default='')
    BLSR_filter = models.TextField(null=True, blank=True,  default='')
    internet_filter = models.BooleanField(null=True, blank=True)

class Annuity(models.Model):
    dcls_month = models.TextField(null=False)  # 공시제출월
    fin_co_no = models.TextField(null=False)  # 금융 회사 코드
    fin_prdt_cd = models.TextField(null=False)  # 금융 상품 코드
    kor_co_nm = models.TextField(null=False)  # 금융 회사 명
    fin_prdt_nm = models.TextField(null=False)  # 금융 상품 명
    join_deny = models.TextField(null=True, blank=True)   # 가입 제한 여부
    join_member = models.TextField(null=True, blank=True)   # 가입 대상
    join_way = models.TextField(null=True, blank=True)   # 가입 방법
    pnsn_kind_nm = models.TextField(null=True, blank=True)   # 연금 저축 종류 명
    prdt_type_nm = models.TextField(null=True, blank=True)   # 상품 유형명
    avg_prft_rate = models.FloatField(null=True, blank=True)   # 평균 수익률
    btrm_prft_rate_1 = models.FloatField(null=True, blank=True)   # 전년도 수익률
    btrm_prft_rate_2 = models.FloatField(null=True, blank=True)   # 2년전 수익률
    btrm_prft_rate_3 = models.FloatField(null=True, blank=True)   # 3년전 수익률
    annuity_like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="annuity_like_products", blank=True
    )  # 장바구니 한 유저
    annuity_joined_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="annuity_join_products", blank=True
    )  # 장바구니 한 유저
    # 필터링을 위한 필드
    age_filter = models.IntegerField(null=True, blank=True,  default=0)
    gender_filter = models.TextField(null=True, blank=True,  default='')
    BLSR_filter = models.TextField(null=True, blank=True,  default='')
    internet_filter = models.BooleanField(null=True, blank=True)