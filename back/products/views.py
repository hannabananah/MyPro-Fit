from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser
from rest_framework import status
from .models import Deposit, Saving, Annuity
from .serializers import DepositListSerializer, SavingListSerializer, AnnuityListSerializer, DepositDetailSerializer, SavingDetailSerializer, AnnuityDetailSerializer

import requests, json

# Create your views here.
PRODUCT_KEY = settings.PRODUCT_KEY

# 관리자가 아니면 GET 요청만 허용
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET 요청은 모든 인증된 사용자에게 허용
        if request.method in ['GET']:
            return request.user and request.user.is_authenticated
        # PUT, DELETE 요청은 관리자에게만 허용
        if request.method in ['PUT', 'DELETE']:
            return request.user and request.user.is_staff
        return False
    
# 데이터 DB로 저장 -> 관리자만
@api_view(['GET'])
@permission_classes([IsAdminUser])
def fetch_deposit(request):
    # 예금 가져오기
    for page in range(1,4):
        url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_KEY}&topFinGrpNo=020000&pageNo={page}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:  # 비어 있지 않으면 데이터를 반환
                for pdt in data['result']['baseList']:
                    print(pdt)
                    if Deposit.objects.filter(fin_prdt_cd = pdt['fin_prdt_cd']).exists():
                        continue
                    dcls_month = pdt.get('dcls_month')
                    fin_co_no = pdt.get('fin_co_no')
                    fin_prdt_cd = pdt.get('fin_prdt_cd')
                    kor_co_nm = pdt.get('kor_co_nm')
                    fin_prdt_nm = pdt.get('fin_prdt_nm')
                    join_deny = pdt.get('join_deny', None)
                    join_member = pdt.get('join_member', None)
                    mtrt_int = pdt.get('mtrt_int', None)
                    max_limit = pdt.get('max_limit', None)
                    join_way = pdt.get('join_way', None)
                    spcl_cnd = pdt.get('spcl_cnd', None)
                    saving_product = Deposit(dcls_month = dcls_month, fin_co_no=fin_co_no, fin_prdt_cd=fin_prdt_cd, 
                                             kor_co_nm=kor_co_nm, fin_prdt_nm=fin_prdt_nm, join_deny=join_deny,
                                             join_member=join_member, mtrt_int=mtrt_int, max_limit=max_limit,
                                             join_way=join_way, spcl_cnd=spcl_cnd)
                    saving_product.save()
                for opt in data['result']['optionList']:
                    product = Deposit.objects.get(fin_prdt_cd=opt['fin_prdt_cd'])
                    if product:
                        if opt['save_trm'] in ["6", "12", "24", "36"]:  # 해당 기간이 있는지 확인합니다.
                            month = opt['save_trm']
                            # 해당 기간에 대한 필드를 업데이트합니다.
                            Deposit.objects.update_or_create(
                                fin_prdt_cd=opt['fin_prdt_cd'],
                                defaults={f'month_{month}': opt['intr_rate']},
                            )
                        
                return Response({'result': '데이터 저장 성공'})

    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def fetch_saving(request):
    # 적금 가져오기
    for page in range(1,4):
        url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={PRODUCT_KEY}&topFinGrpNo=020000&pageNo={page}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:  # 비어 있지 않으면 데이터를 반환
                for pdt in data['result']['baseList']:
                    fin_prdt_cd = pdt['fin_prdt_cd']
                    if Saving.objects.filter(fin_prdt_cd = fin_prdt_cd).exists():
                        continue
                    dcls_month = pdt.get('dcls_month')
                    fin_co_no = pdt.get('fin_co_no')
                    fin_prdt_cd = pdt.get('fin_prdt_cd')
                    kor_co_nm = pdt.get('kor_co_nm', None)
                    fin_prdt_nm = pdt.get('fin_prdt_nm')
                    join_deny = pdt.get('join_deny', None)
                    join_member = pdt.get('join_member', None)
                    mtrt_int = pdt.get('mtrt_int', None)
                    max_limit = pdt.get('max_limit', None)
                    join_way = pdt.get('join_way', None)
                    spcl_cnd = pdt.get('spcl_cnd', None)

                    deposit_product = Saving(kor_co_nm=kor_co_nm, join_member=join_member, fin_prdt_nm=fin_prdt_nm,
                                             join_deny=join_deny, mtrt_int=mtrt_int, max_limit=max_limit, dcls_month=dcls_month,
                                            join_way=join_way, spcl_cnd=spcl_cnd, fin_co_no=fin_co_no, fin_prdt_cd=fin_prdt_cd)
                    deposit_product.save()
                
                for opt in data['result']['optionList']:
                    product = Saving.objects.get(fin_prdt_cd=opt['fin_prdt_cd'])
                    if product:
                        if opt['save_trm'] in ["6", "12", "24", "36"]:  # 해당 기간이 있는지 확인합니다.
                            month = opt['save_trm']
                            # 해당 기간에 대한 필드를 업데이트합니다.
                            Saving.objects.update_or_create(
                                fin_prdt_cd=opt['fin_prdt_cd'],
                                defaults={f'month_{month}': opt['intr_rate']},
                            )
                        
                return Response({'result': '데이터 저장 성공'})

    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def fetch_annuity(request):
    # 연금 가져오기
    for page in range(1,4):
        url = f'http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json?auth={PRODUCT_KEY}&topFinGrpNo=060000&pageNo={page}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:  # 비어 있지 않으면 데이터를 반환
                for pdt in data['result']['baseList']:
                    print(pdt)
                    fin_prdt_cd = pdt['fin_prdt_cd']
                    if Annuity.objects.filter(fin_prdt_nm = fin_prdt_cd).exists():
                        continue
                    dcls_month = pdt.get('dcls_month')
                    fin_co_no = pdt.get('fin_co_no')
                    fin_prdt_cd = pdt.get('fin_prdt_cd')
                    kor_co_nm = pdt.get('kor_co_nm', None)
                    fin_prdt_nm = pdt.get('fin_prdt_nm')
                    join_deny = pdt.get('join_deny', None)
                    join_member = pdt.get('join_member', None)
                    join_way = pdt.get('join_way', None)
                    pnsn_kind_nm = pdt.get('pnsn_kind_nm', None)
                    prdt_type_nm = pdt.get('prdt_type_nm', None)
                    avg_prft_rate = pdt.get('avg_prft_rate', None)
                    btrm_prft_rate_1 = pdt.get('btrm_prft_rate_1', None)
                    btrm_prft_rate_2 = pdt.get('btrm_prft_rate_2', None)
                    btrm_prft_rate_3 = pdt.get('btrm_prft_rate_3', None)
                    deposit_product = Annuity(kor_co_nm=kor_co_nm, prdt_type_nm=prdt_type_nm, avg_prft_rate=avg_prft_rate,
                                             join_deny=join_deny, fin_prdt_nm=fin_prdt_nm, join_member=join_member, dcls_month=dcls_month,
                                            join_way=join_way, pnsn_kind_nm=pnsn_kind_nm,
                                            btrm_prft_rate_1=btrm_prft_rate_1, btrm_prft_rate_2=btrm_prft_rate_2,
                                            btrm_prft_rate_3=btrm_prft_rate_3, fin_co_no=fin_co_no, fin_prdt_cd=fin_prdt_cd)
                    deposit_product.save()
                return Response({'result': '데이터 저장 성공'})

    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)

# 예금 리스트 출력
@api_view(['GET'])
def deposit_list(request):
    deposits = Deposit.objects.all()
        # JSON 으로 포장 -> return
    serializer = DepositListSerializer(deposits, many=True)
    return Response(serializer.data)

# 적금 리스트 출력
@api_view(['GET'])
def saving_list(request):
    savings = Saving.objects.all()
        # JSON 으로 포장 -> return
    serializer = SavingListSerializer(savings, many=True)
    return Response(serializer.data)

# 연금 리스트 출력
@api_view(['GET'])
def annuity_list(request):
    annuities = Annuity.objects.all()
        # JSON 으로 포장 -> return
    serializer = AnnuityListSerializer(annuities, many=True)
    return Response(serializer.data)

# 상세정보 출력
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminOrReadOnly])
def deposit_detail(req,code):
    deposit=get_object_or_404(Deposit,fin_prdt_cd=code)
    if req.method=='GET':
        serializer=DepositDetailSerializer(deposit)
        return Response(serializer.data)
    
    elif req.method=='PUT':
        serializer=DepositDetailSerializer(deposit,data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    elif req.method=='DELETE':
        deposit.delete()
        data={
            'delete':f'예금 {code}이/가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminOrReadOnly])
def saving_detail(req,code):
    saving=get_object_or_404(Saving,fin_prdt_cd=code)
    print(saving)
    if req.method=='GET':
        serializer=SavingDetailSerializer(saving)
        return Response(serializer.data)
    
    elif req.method=='PUT':
        serializer=SavingDetailSerializer(saving,data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    elif req.method=='DELETE':
        saving.delete()
        data={
            'delete':f'적금 {code}이/가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminOrReadOnly])
def annuity_detail(req,code):
    annuity=get_object_or_404(Annuity,fin_prdt_cd=code)
    if req.method=='GET':
        serializer=AnnuityDetailSerializer(annuity)
        return Response(serializer.data)
    
    elif req.method=='PUT':
        serializer=AnnuityDetailSerializer(annuity,data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    elif req.method=='DELETE':
        annuity.delete()
        data={
            'delete':f'적금 {code}이/가 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)

# 찜하기 기능
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_likes(request, code):
    deposit = Deposit.objects.get(fin_prdt_cd=code)
    # 역참조
    if request.user in deposit.deposit_like_users.all():
        deposit.deposit_like_users.remove(request.user)
    else:
        deposit.deposit_like_users.add(request.user)
    serializer = DepositDetailSerializer(deposit)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def saving_likes(request, code):
    saving = Saving.objects.get(fin_prdt_cd=code)
    # 역참조
    if request.user in saving.saving_like_users.all():
        saving.saving_like_users.remove(request.user)
    else:
        saving.saving_like_users.add(request.user)
    serializer = SavingDetailSerializer(saving)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def annuity_likes(request, code):
    annuity = Annuity.objects.get(fin_prdt_cd=code)
    # 역참조
    if request.user in annuity.annuity_like_users.all():
        annuity.annuity_like_users.remove(request.user)
    else:
        annuity.annuity_like_users.add(request.user)
    serializer = AnnuityDetailSerializer(annuity)
    return Response(serializer.data)

