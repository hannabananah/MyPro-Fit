# 금융 상품 추천 웹사이트 만들기

팀장 - 강한나

팀원 - 김민채

기간: 2024.05.16 ~ 2024.05.23

---
### 업무 분담

1. 강한나
   - openai API 를 활용한 챗봇 
   - Figma 를 활용한 frontend 설계
   - 회원 커스터마이징 (+ 프로필 페이지 )
   - 게시판 backend 
   - 메인페이지 / 헤더 / 게시판 css
  
2. 김민채
   - 예적금 금리비교 / 상세페이지
   - 게시판 frontend 
   - db 설계
   - 상품 추천 알고리즘 
   - 환율계산기 
   - 은행 지점찾기 
   - 가입한 상품 비교 
   - 인기상품 출력 

- backend 와 frontend 로 나누는 것 보다 웬만하면 기능별로 업무 분담을 하고자 했음
- 본인이 맡은 기능이라면 back, front 전부 구현하기로 함
- 현업에 가면 front를 하더라도 back 을 알아야하고 back 을 하더라도 front 를 알아야하기 때문에 둘다 경험해보는 것이 좋다고 생각했고, 본격적으로 2학기에 가서 프로젝트를 하기 전에 항상 하던것 보다는 생소한 분야더라도 직접 맞닥뜨리고 해결해내는 경험을 해보고 싶었다.

## 설계 내용


1. 메인 페이지
   - 금융상품 비교 애플리케이션 소개
   - 사용자가 편리하게 주요 서비스를 확인하고, 해당 페이지로 이동할 수 있음
   - best 상품 출력
   (각 상품 유형별 인기순 1위인 상품을 메인페이지에 출력한다)
2. 회원 커스터마이징
   - django 의 기본 user 를 상속받아 구현
   - 적절한 Serializer 구성
   - 유저이름, 이메일, 가입 상품 저장 필드 (M:N 으로 구성)
   - 유저 이름을 email 필드로 대체하고 nickname 을 활용
   - 비밀번호 찾기 기능 추가 => 이메일 인증
3. 예적금 금리 비교
   - 데이터 저장 : 금융상품통합비교공시 API
     - 이미 존재하는 데이터는 새로저장하지 않도록 구현
   - 전체조회
     - 상품 목록을 볼 수 있도록
     - 은행 선택, 가입 기간 선택기능
     - 가입 기간별 금리 비교 출력
     - 특정 상품 선택시 상세정보 페이지로 이동
     - 좋아요 기반으로 인기순 정렬 기능
   - 상세조회
     - 해당 금융상품에 대한 자세한 정보 출력
     - 가입하기 버튼 추가
     - 이미 가입한 상품일 경우 이미 가입한 상품입니다 문구 출력 + 가입 해제 버튼 추가
     - 로그인 하지 않은 회원은 이용 불가
4. 환율계산기
   - 한국수출입은행 API
   - 국가선택
   - 입력 2가지 받기
     - 원화 입력 : 선택한 국가의 통화로 변환된 값 출력
     - 외화 입력 : 해당 통화를 원화로 변환한 값 출력
   - 입출력시 3자리 단위로 ',' 삽입
   - 입력 후 외화 또는 기준환율을 변경하면 그에 맞게 값이 자동으로 바뀌도록 구현
5. 은행 지점 검색
   - kakao map API
   - 위치 입력 (Ex. 강남역) -> 해당 위치 근처 은행정보 출력
   - 강남역 국민 으로 입력시 국민은행만 출력되게 함
6. 게시판
   - 게시글 CRUD
   - 댓글 CRUD
   - 본인이 작성한 게시글, 댓글만 삭제 수정
   - 로그인 하지 않은 유저 게시글 목록만 접근 가능
   - 간단한 금융상품 후기 페이지 -> 포스트잇 컨셉으로 구현
   - 게시글 목록페이지에서 게시글 내용 미리보기 가능
     - 게시글 내용이 길다면 말줄임표로 일부만 미리보기 가능
   - 새로고침시 랜덤으로 색깔 변경
7. 프로필 페이지
   - 회원 정보 수정화면 구성
   - 내가 가입한 금융상품 리스트 출력
   - 차트라이브러리 활용 => 가입 상품 금리정보 그래프로 출력
   - 회원 추가정보 수집
     - 회원이 원하는 금융상품을 추천하기 위한 정보
     - 예시 : 기초생활수급자 여부, 성별, 자산, 연금저축 관심여부, 자유납입상품 선호여부 등
8. 금융상품 추천 알고리즘
   - 유저 더미데이터 활용 (Django seed 라이브러리와 파이썬 faker 라이브러리 활용)
   - 애플리케이션을 이용하는 다른 유저의 정보와, 회원이 직접 입력한 회원 정보를 바탕으로 상품 추천
   - 회원이 입력한 정보를 바탕으로 1차 상품 필터링
   - 해당 회원과 자산, 연령이 유사하고 가입한 상품이 비슷한 유저를 찾아냄 (이하, 유사 회원)
   - 유사회원이 가입한 상품 중에서 해당회원이 가입하지 않은 상품들 추천
   - 로그인 하지 않았을 경우 이용불가 -> 로그인 페이지로 routing
   - 상세 정보를 입력하지 않았을 경우 이용 불가 -> 상세정보 입력 페이지로 routing
  
9. AI를 활용한 챗봇 구현
   - openai api를 통해 구현
   - 프롬프트 작성을 통해 ai 학습
   - 말투 및 질문 방식부터 시작해서 상품 내용까지 작성했다.
   - 사용자가 원하는 상품을 추천할 수 있도록 질문을 유도한다.

## 데이터베이스 모델링
  ![alt text](image.png)
   - 회원 필드에 상품 필터링을 위한 추가 정보를 저장하고
   - 연금저축, 예금, 적금 상품별로 테이블을 만들었다.
   - 또한 유저와의 외래키로 설정해서 유저가 좋아요 누른 상품 필드와 유저가 가입한 상품 필드를 만들었다.
   - 필드명은 활용한 api에서 제공되는 필드명을 그대로 사용하여 api 이용을 보다 편리하게 했다. 
   - 또한 주석을 활용하여 해당 필드가 어떤 내용을 담고있는지 표현해두었다.

## 금융상품 추천 알고리즘에 대한 기술적 설명
   ```python
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
    # 가입한 상품이 많이 겹치는 상위 10명의 유저 선택 -> 상품 취향 비슷한 사람이 가입한 다른상품 추천
    similar_users_with_common_products = []
    for user in similar_salary_users:
        # 가입상품이 0개인 유저는 pass
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
    # 더미데이터가 부족한 경우 결과 출력이 안되는 경우 배제
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
                if (request.user.is_internet ==True) and (internet_filter ==False):
                    continue
                # 수익률이 0이상인 상품만 추천
                r = max(annuity.avg_prft_rate, annuity.btrm_prft_rate_1, annuity.btrm_prft_rate_2, annuity.btrm_prft_rate_3)
                if r > 0:
                    recommended_products_json.append({'id': annuity.id, 'name': annuity.fin_prdt_nm, 'type': 'annuity', 'r': r, 'bank': annuity.kor_co_nm, 'code': annuity.fin_prdt_cd})
                    if not annuity_exist:
                        annuity_exist = True
            if not annuity_exist:
               # id 값에 음수를 넣어두고 vue 에서 id 값이 음수라면 추천X
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
   ```
   - 가입 가능한 상품과 가입 불가능한 상품을 나눈다
     - 미리 입력받은 유저 정보를 활용
   - 전체 유저중에서 현재유저와 유사한 유저들 필터링 (나이, 자산)
   - 유사 유저들이 가입한 상품 순회 -> 리스트에 추가 -> 현재 유저와 가입한 상품이 얼마나 겹치는지를 기준으로 내림차순 정렬 (가장 많이 유사한 유저부터 고려하기 위함)
   - 해당 유사 유저들이 가입한 다른상품 (현재유저가 아직 가입하지 않은 상품중에서) 을 빈 리스트에 추가 -> 상품의 개수가 10개가 되었다면 탐색 중단
   - 아직 더미데이터가 부족하여 상품 추천에 문제가 생길경우 추천되지 않는 오류 수정

## 서비스 대표 기능 설명
1. 상품 추천 기능
   - 위에서 설명한 알고리즘을 바탕으로 유저에게 가장 적합한 상품 최대 10개 추천 -> 
   - 최대 금리 기준으로 내림차순 정렬하여 금리가 높은 상품부터 출력함
   - 해당 상품을 클릭하면 상품 상세페이지로 이동 가능 
   - 로그인 하지 않았다면 로그인페이지로 라우팅
   - 상세정보를 입력하지 않았다면 상세정보 페이지로 라우팅
  
2. 유저 및 프로필
   - 회원 커스터마이징 : email 을 username 으로 설정하고 변경 불가능하게 함
   - 비밀번호 분실시 해당 email 로 비밀번호 초기화 폼 전달
   - 프로필 페이지에서 유저 닉네임 / 상세정보 입력 수정 가능
   - 프로필 페이지에서 본인이 가입한 상품 목록 출력 + 금리기준으로 차트 비교 가능

3. 은행 지점 찾기
   - 예시 이미지에는 시, 군, 구 등을 사용자가 직접 select box 에서 고른뒤 출력하게 되어있지만, 사용자 입장에서 생각했을 때 일일히 select box 에서 선택하는 것 보다는 간단하게 원하는 지명을 검색하여 이용하는 것이 더 편리하다고 생각했음.
   - 키워드 끝에 '은행' 을 기본값으로 설정해두어서 지역명만 입력해도 은행 결과만 출력받을 수 있게 구현
  
4. 환율 계산기
   - watch 를 활용해서 선택국가나 기준환율이 바뀌더라도 즉시 결과값에 반영될수 있도록 함
   - computed 를 쓰려고했으나 v-model 로 바인딩했을 때 오류가 발생하여 watch 이용
   - ',' 를 붙여주는 formatting 함수와 ',' 를 떼고 flaot 값으로 전환해주는 parsing 함수 두개를 미리 만들어두고, 사용자가 입력할때마다 formatting 함수에 전달하는 방식으로 input box 에 바인딩했다.
   - input 이벤트가 발생될때마다 parsing 함수도 함께 작동시켜서 formatting 된 값을 다시 float 값으로 변환하여 watch에 전달하는 방식으로 구현하였다.
   - 사용자가 외화를 입력할 때는 원화값이 계산되고
   - 원화를 입력할 때는 외화값이 계산될 수 있도록 form 을 2개를 만들어서 변수를 통해 관리했다.
   - 사용자는 폼 전환을 눈치채지 못하도록 v-show 를 활용했다.

5. 예적금 금리비교
   - 기간별 금리비교를 쉽게 하기 위해 table 형식으로 나타냈다.
   - 맨 위 header 에 적힌 기간을 누르면 해당 기간 기준으로 정렬된다
   - null 값일 경우 가장 맨 뒤로 가도록 함
   - 또한, select 박스로 특정 기간을 선택할 경우 해당 기간 기준으로 금리순 정렬 + null 값인 결과 제외 되도록 함
   - 인기준 정렬 필드를 추가하여 좋아요 기반으로 인기도를 측정하고 인기상품 정렬기능을 만들었다. -> 홈에 유형별로 인기 상품 1위인 상품이 출력되도록 했다.
   - 해당 상품을 클릭시 상세페이지로 이동되며, 로그인하지 않은 사용자일 경우 로그인 페이지로 routing
  
6. 상품 추천 챗봇
   - openai api를 통해 구현
   - 프롬프트 작성을 통해 ai 학습
   - 말투 및 질문 방식부터 시작해서 상품 내용까지 작성했다.
   - 사용자가 원하는 상품을 추천할 수 있도록 질문을 유도한다.


## 느낀점
1. 민채
   
   항상 혼자만 쓰던 git 레포지토리를 페어와 함께 사용하니깐 처음엔 충돌도 많이 나고 버전관리도 힘들었는데 후반 가니 충돌도 해결할 수 있게 되고, 페어가 branch 전략을 많이 설명해줘서 효율적이게 branch 관리를 할 수 있게 되었습니다.
   또한, 컨벤션을 미리 정해두고 해당 컨벤션을 활용하여 commit 을 하니깐 현재 상대방이 어떤걸 작업하고 있는지 한 눈에 볼 수 있어서 유용했습니다. 2학기 프로젝트를 할 때 어떻게 팀원과 협업해야 할 지를 많이 배울 수 있는 기회였습니다.

   그리고 다양한 api 키를 많이 사용해보고 데이터베이스 모델링도 직접 해볼 수 있어서 좋은 기회였다. 현재 우리가 만든 웹 애플리케이션은 조회가 많이 필요한 서비스이기 때문에 조회에 효율적인 db구성을 하고자 노력했다. 

   기간이 너무 짧다보니 일단 기능이 돌아 가기만 하면 다음 기능을 구현하는데에 급급했는데 ... 그러다보니 지금 생각했을 때 비효율적인 코드가 너무 많아서 아쉬웠다. 다음 프로젝트 부터는 서비스에 대해 좀더 고민해보고 효율적인 코드를 짜려고 노력해보고 싶다는 생각이 들었다. 서로 코드리뷰를 하고 피드백해주는 시간도 좀 있었으면..!
   
2. 한나
      
