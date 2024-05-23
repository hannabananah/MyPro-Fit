import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .models import Annuity, Deposit, Saving
from .serializers import (
    AnnuityDetailSerializer,
    AnnuityListSerializer,
    DepositDetailSerializer,
    DepositListSerializer,
    SavingDetailSerializer,
    SavingListSerializer,
)

PRODUCT_KEY = settings.PRODUCT_KEY


# 관리자가 아니면 GET 요청만 허용
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET 요청은 모든 인증된 사용자에게 허용
        if request.method in ["GET"]:
            return request.user and request.user.is_authenticated
        # PUT, DELETE 요청은 관리자에게만 허용
        if request.method in ["PUT", "DELETE"]:
            return request.user and request.user.is_staff
        return False


# 데이터 DB로 저장 -> 관리자만
@api_view(["GET"])
@permission_classes([IsAdminUser])
def fetch_deposit(request):
    # 예금 가져오기
    for page in range(1, 4):
        url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_KEY}&topFinGrpNo=020000&pageNo={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:  # 비어 있지 않으면 데이터를 반환
                for pdt in data["result"]["baseList"]:
                    print(pdt)
                    if Deposit.objects.filter(fin_prdt_cd=pdt["fin_prdt_cd"]).exists():
                        continue
                    dcls_month = pdt.get("dcls_month")
                    fin_co_no = pdt.get("fin_co_no")
                    fin_prdt_cd = pdt.get("fin_prdt_cd")
                    kor_co_nm = pdt.get("kor_co_nm")
                    fin_prdt_nm = pdt.get("fin_prdt_nm")
                    join_deny = pdt.get("join_deny", None)
                    join_member = pdt.get("join_member", None)
                    mtrt_int = pdt.get("mtrt_int", None)
                    max_limit = pdt.get("max_limit", None)
                    join_way = pdt.get("join_way", None)
                    spcl_cnd = pdt.get("spcl_cnd", None)
                    saving_product = Deposit(
                        dcls_month=dcls_month,
                        fin_co_no=fin_co_no,
                        fin_prdt_cd=fin_prdt_cd,
                        kor_co_nm=kor_co_nm,
                        fin_prdt_nm=fin_prdt_nm,
                        join_deny=join_deny,
                        join_member=join_member,
                        mtrt_int=mtrt_int,
                        max_limit=max_limit,
                        join_way=join_way,
                        spcl_cnd=spcl_cnd,
                    )
                    saving_product.save()
                for opt in data["result"]["optionList"]:
                    product = Deposit.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
                    if product:
                        if opt["save_trm"] in [
                            "6",
                            "12",
                            "24",
                            "36",
                        ]:  # 해당 기간이 있는지 확인합니다.
                            month = opt["save_trm"]
                            # 해당 기간에 대한 필드를 업데이트합니다.
                            Deposit.objects.update_or_create(
                                fin_prdt_cd=opt["fin_prdt_cd"],
                                defaults={f"month_{month}": opt["intr_rate"]},
                            )

                return Response({"result": "데이터 저장 성공"})

    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def fetch_saving(request):
    # 적금 가져오기
    for page in range(1, 4):
        url = f"http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={PRODUCT_KEY}&topFinGrpNo=020000&pageNo={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:  # 비어 있지 않으면 데이터를 반환
                for pdt in data["result"]["baseList"]:
                    fin_prdt_cd = pdt["fin_prdt_cd"]
                    if Saving.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
                        continue
                    dcls_month = pdt.get("dcls_month")
                    fin_co_no = pdt.get("fin_co_no")
                    fin_prdt_cd = pdt.get("fin_prdt_cd")
                    kor_co_nm = pdt.get("kor_co_nm", None)
                    fin_prdt_nm = pdt.get("fin_prdt_nm")
                    join_deny = pdt.get("join_deny", None)
                    join_member = pdt.get("join_member", None)
                    mtrt_int = pdt.get("mtrt_int", None)
                    max_limit = pdt.get("max_limit", None)
                    join_way = pdt.get("join_way", None)
                    spcl_cnd = pdt.get("spcl_cnd", None)

                    deposit_product = Saving(
                        kor_co_nm=kor_co_nm,
                        join_member=join_member,
                        fin_prdt_nm=fin_prdt_nm,
                        join_deny=join_deny,
                        mtrt_int=mtrt_int,
                        max_limit=max_limit,
                        dcls_month=dcls_month,
                        join_way=join_way,
                        spcl_cnd=spcl_cnd,
                        fin_co_no=fin_co_no,
                        fin_prdt_cd=fin_prdt_cd,
                    )
                    deposit_product.save()

                for opt in data["result"]["optionList"]:
                    product = Saving.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
                    if product:
                        if opt["save_trm"] in [
                            "6",
                            "12",
                            "24",
                            "36",
                        ]:  # 해당 기간이 있는지 확인합니다.
                            month = opt["save_trm"]
                            # 해당 기간에 대한 필드를 업데이트합니다.
                            Saving.objects.update_or_create(
                                fin_prdt_cd=opt["fin_prdt_cd"],
                                defaults={f"month_{month}": opt["intr_rate"]},
                            )

                return Response({"result": "데이터 저장 성공"})

    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def fetch_annuity(request):
    # 연금 가져오기
    for page in range(1, 4):
        url = f"http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json?auth={PRODUCT_KEY}&topFinGrpNo=060000&pageNo={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:  # 비어 있지 않으면 데이터를 반환
                for pdt in data["result"]["baseList"]:
                    print(pdt)
                    fin_prdt_cd = pdt['fin_prdt_cd']
                    if Annuity.objects.filter(fin_prdt_cd = fin_prdt_cd).exists():
                        continue
                    dcls_month = pdt.get("dcls_month")
                    fin_co_no = pdt.get("fin_co_no")
                    fin_prdt_cd = pdt.get("fin_prdt_cd")
                    kor_co_nm = pdt.get("kor_co_nm", None)
                    fin_prdt_nm = pdt.get("fin_prdt_nm")
                    join_deny = pdt.get("join_deny", None)
                    join_member = pdt.get("join_member", None)
                    join_way = pdt.get("join_way", None)
                    pnsn_kind_nm = pdt.get("pnsn_kind_nm", None)
                    prdt_type_nm = pdt.get("prdt_type_nm", None)
                    avg_prft_rate = pdt.get("avg_prft_rate", None)
                    btrm_prft_rate_1 = pdt.get("btrm_prft_rate_1", None)
                    btrm_prft_rate_2 = pdt.get("btrm_prft_rate_2", None)
                    btrm_prft_rate_3 = pdt.get("btrm_prft_rate_3", None)
                    deposit_product = Annuity(
                        kor_co_nm=kor_co_nm,
                        prdt_type_nm=prdt_type_nm,
                        avg_prft_rate=avg_prft_rate,
                        join_deny=join_deny,
                        fin_prdt_nm=fin_prdt_nm,
                        join_member=join_member,
                        dcls_month=dcls_month,
                        join_way=join_way,
                        pnsn_kind_nm=pnsn_kind_nm,
                        btrm_prft_rate_1=btrm_prft_rate_1,
                        btrm_prft_rate_2=btrm_prft_rate_2,
                        btrm_prft_rate_3=btrm_prft_rate_3,
                        fin_co_no=fin_co_no,
                        fin_prdt_cd=fin_prdt_cd,
                    )
                    deposit_product.save()
                return Response({"result": "데이터 저장 성공"})

    # 모든 시도에서 데이터를 찾지 못한 경우
    return Response({"error": "데이터를 찾지 못 했습니다."}, status=404)


# 예금 리스트 출력
@api_view(["GET"])
def deposit_list(request):
    deposits = Deposit.objects.all()
    # JSON 으로 포장 -> return
    serializer = DepositListSerializer(deposits, many=True)
    return Response(serializer.data)


# 적금 리스트 출력
@api_view(["GET"])
def saving_list(request):
    savings = Saving.objects.all()
    # JSON 으로 포장 -> return
    serializer = SavingListSerializer(savings, many=True)
    return Response(serializer.data)


# 연금 리스트 출력
@api_view(["GET"])
def annuity_list(request):
    annuities = Annuity.objects.all()
    # JSON 으로 포장 -> return
    serializer = AnnuityListSerializer(annuities, many=True)
    return Response(serializer.data)


# 상세정보 출력
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminOrReadOnly])
def deposit_detail(req, code):
    deposit = get_object_or_404(Deposit, fin_prdt_cd=code)
    if req.method == "GET":
        serializer = DepositDetailSerializer(deposit)
        return Response(serializer.data)

    elif req.method == "PUT":
        serializer = DepositDetailSerializer(deposit, data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    elif req.method == "DELETE":
        deposit.delete()
        data = {"delete": f"예금 {code}이/가 삭제되었습니다."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminOrReadOnly])
def saving_detail(req, code):
    saving = get_object_or_404(Saving, fin_prdt_cd=code)
    if req.method == "GET":
        serializer = SavingDetailSerializer(saving)
        return Response(serializer.data)

    elif req.method == "PUT":
        serializer = SavingDetailSerializer(saving, data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    elif req.method == "DELETE":
        saving.delete()
        data = {"delete": f"적금 {code}이/가 삭제되었습니다."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated, IsAdminOrReadOnly])
def annuity_detail(req, code):
    annuity = get_object_or_404(Annuity, fin_prdt_cd=code)
    if req.method == "GET":
        serializer = AnnuityDetailSerializer(annuity)
        return Response(serializer.data)

    elif req.method == "PUT":
        serializer = AnnuityDetailSerializer(annuity, data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    elif req.method == "DELETE":
        annuity.delete()
        data = {"delete": f"적금 {code}이/가 삭제되었습니다."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 찜하기 기능
@api_view(["POST"])
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


@api_view(["POST"])
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


@api_view(["POST"])
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


# 상품 가입
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def annuity_joins(request, code):
    annuity = Annuity.objects.get(fin_prdt_cd=code)
    # 역참조
    if request.user in annuity.annuity_joined_users.all():
        annuity.annuity_joined_users.remove(request.user)
    else:
        annuity.annuity_joined_users.add(request.user)
    serializer = AnnuityDetailSerializer(annuity)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def saving_joins(request, code):
    saving = Saving.objects.get(fin_prdt_cd=code)
    # 역참조
    if request.user in saving.saving_joined_users.all():
        saving.saving_joined_users.remove(request.user)
    else:
        saving.saving_joined_users.add(request.user)
    serializer = SavingDetailSerializer(saving)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deposit_joins(request, code):
    deposit = Deposit.objects.get(fin_prdt_cd=code)
    # 역참조
    if request.user in deposit.deposit_joined_users.all():
        deposit.deposit_joined_users.remove(request.user)
    else:
        deposit.deposit_joined_users.add(request.user)
    serializer = DepositDetailSerializer(deposit)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def recommend_products(request):
    # 현재 유저의 자산 정보 가져오기
    current_asset = request.user.asset
    
    # 모든 적금 불러오기
    all_savings = list(Saving.objects.all())

    # 가입하지 못하는 상품 리스트
    cannot_join = []
    # 가입가능한 상품리스트
    can_join = []
    for saving in all_savings:
        age_filter = saving.age_filter
        gender_filter = saving.gender_filter
        internet_filter = saving.internet_filter
        # 나이제한에 걸리는경우 추가
        if age_filter != 0 and ((age_filter < 0 and request.user.age > abs(age_filter)) or (age_filter > 0 and request.user.age < age_filter)):
            cannot_join.append(saving.pk)
            continue
        # 인터넷 가입상품만 원하는데, 인터넷가입불가 상품인경우
        print(internet_filter, request.user.is_internet)
        if request.user.is_internet and not internet_filter:
            cannot_join.append(saving.pk)
            continue
        # 자유납입 상품만 추천받고싶은데 자유납입 불가일경우
        if request.user.is_free and gender_filter == 'N':
            cannot_join.append(saving.pk)
            continue
        can_join.append(saving)
    # 현재 유저와 나이 차이가 10살 미만인 유저 필터링
    similar_age_users = get_user_model().objects.filter(age__lte=request.user.age+10, age__gte=request.user.age-10).exclude(id=request.user.id)
    
    # 현재 유저와 자산 차이가 본인의 자산보다 덜 나는 유저 선택
    similar_salary_users = []
    for user in similar_age_users:
        user_asset = user.asset
        salary_difference = abs(current_asset - user_asset)
        if salary_difference / current_asset <= 2:
            similar_salary_users.append(user)
    print('자산 비슷한유저', similar_salary_users)
    # 가입한 상품이 많이 겹치는 상위 10명의 유저 선택 -> 상품 취향 비슷한 사람이 가입한 다른상품 추천
    similar_users_with_common_products = []
    for user in similar_salary_users:
        # 가입상품이 0개인 유저는 pass
        print(user.saving_join_products)
        if len(user.saving_join_products.all()) < 1:
            continue
        common_products_count = len(set(request.user.saving_join_products.all()) & set(user.saving_join_products.all()))
        similar_users_with_common_products.append((user, common_products_count))
    
    similar_users_with_common_products.sort(key=lambda x: x[1], reverse=True)
    top_similar_users = [user for user, _ in similar_users_with_common_products[:10]]
    
    # 선택된 유저들이 가입한 다른 상품 중에서 현재 유저가 아직 가입하지 않은 상위 10개의 상품 추천
    recommended_products_list = []
    for user in top_similar_users:
        similar_users_joined_products = user.saving_join_products.all()
        for product in similar_users_joined_products:
            # 가입하지 못하는 상품이면 pass
            if product.id in cannot_join:
                continue
            # 이미 가입한 상품이면 pass
            if product in request.user.saving_join_products.all():
                continue
            if len(recommended_products_list) >= 10:
                break
        if len(recommended_products_list) >= 10:
            break
    # 추천 상품의 개수가 0인경우 가입가능한 상품 출력
    if len(recommended_products_list) == 0:
        recommended_products_json = []
        # 연금 상품 추가
        annuity_exist = False
        if request.user.is_pension:
            all_annuities = list(Annuity.objects.all())
            for annuity in all_annuities:
                age_filter = annuity.age_filter
                internet_filter = annuity.internet_filter
                # 나이제한에 걸리는 경우
                if age_filter != 0 and ((age_filter < 0 and request.user.age > abs(age_filter)) or (age_filter > 0 and request.user.age < age_filter)):
                    continue
                # 인터넷 가입상품만 원하는데, 인터넷가입불가 상품인경우
                print('인터넷필터 연금', request.user.is_internet, internet_filter)
                if (request.user.is_internet ==True) and (internet_filter ==False):
                    continue
                # 수익률이 0이상인 상품만 추천
                r = max(annuity.avg_prft_rate, annuity.btrm_prft_rate_1, annuity.btrm_prft_rate_2, annuity.btrm_prft_rate_3)
                print('연금수익률', r)
                if r > 0:
                    recommended_products_json.append({'id': annuity.id, 'name': annuity.fin_prdt_nm, 'type': 'annuity', 'r': r, 'bank': annuity.kor_co_nm, 'code': annuity.fin_prdt_cd})
                    if not annuity_exist:
                        annuity_exist = True
            if not annuity_exist:
                recommended_products_json.append({'id': -1, 'name': '추천 가능한 연금 상품이 없습니다.', 'type': 'annuity', 'r': 0 , 'bank': '', 'code': ''})

        for product in can_join[:10]:
            # 상품 정보 담기
            values = [product.month_6, product.month_12, product.month_24, product.month_36]
            filtered_values = [v for v in values if v is not None]
            recommended_products_json.append({'id': product.id, 'name': product.fin_prdt_nm, 'type': 'saving', 'r': max(filtered_values), 'bank': product.kor_co_nm, 'code' : product.fin_prdt_cd})


        return JsonResponse(recommended_products_json[:10], safe=False)
    
    # JSON 형태로 변환하여 반환
    recommended_products_json = []
   # 연금 상품 추가
    annuity_exist = False
    if request.user.is_pension:
        all_annuities = list(Annuity.objects.all())
        for annuity in all_annuities:
            age_filter = annuity.age_filter
            internet_filter = annuity.internet_filter
            # 나이제한에 걸리는 경우
            if age_filter != 0 and ((age_filter < 0 and request.user.age > abs(age_filter)) or (age_filter > 0 and request.user.age < age_filter)):
                continue
            # 인터넷 가입상품만 원하는데, 인터넷가입불가 상품인경우
            if request.user.is_internet and not internet_filter:
                continue
            # 수익률이 0이상인 상품만 추천
            r = max(annuity.avg_prft_rate, annuity.btrm_prft_rate_1, annuity.btrm_prft_rate_2, annuity.btrm_prft_rate_3)
            if r > 0:
                recommended_products_json.append({'id': annuity.id, 'name': annuity.fin_prdt_nm, 'type': 'annuity', 'r': r})
                if not annuity_exist:
                    annuity_exist = True
                    
    for product in recommended_products_list:
        recommended_products_json.append({'id': product.id, 'name': product.fin_prdt_nm, 'type': 'saving', 'r': max(product.month_6, product.month_12, product.month_24, product.month_36), 'bank' : product.kor_co_nm, 'code': product.fin_prdt_cd })

 
        if not annuity_exist:
            recommended_products_json.append({'id': -1, 'name': '추천 가능한 연금 상품이 없습니다.', 'type': 'annuity', 'r': 0 })
    return JsonResponse(recommended_products_json[:10], safe=False)