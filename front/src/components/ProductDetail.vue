<template>
  <div class="bg-sky-50 h-screen flex flex-col items-center">
    <h1 class="text-center text-2xl font-bold pt-6">상품 상세 정보</h1>
    <div class="flex justify-between w-[35%] mb-3">
      <button
        class="border border-solid border-sky-600 px-2 rounded-[8px] bg-slate-50 hover:shadow-inner hover:bg-slate-100"
        @click="$router.go(-1)"
      >
        <undo fillColor="#4682B4"></undo>
      </button>
      <div>
        <button v-show="isLiked" @click="doLike">
          <heart
            fillColor="#FF6666"
            class="inline-block h-[20px] ml-auto"
          ></heart>
        </button>
        <button v-show="!isLiked" @click="doLike">
          <heartOutline
            fillColor="#FF6666"
            class="inline-block h-[20px] ml-auto"
          ></heartOutline></button
        >{{ numberOfLikes }}
      </div>
    </div>
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="container mx-auto w-2/5 flex items-center flex-col bg-slate-50 p-6 py-8"
    >
      <!-- 예금적금 -->
      <table v-if="route.params.type !== 'annuity' && product" class="flex">
        <thead>
          <tr>
            <td>공시기준월</td>
            <td>상품명</td>
            <td>기관명</td>
            <td>만기 후 이자율</td>
            <td>최고 한도</td>
            <td>가입 조건</td>
            <td>가입 방법</td>
            <td>우대 조건</td>
          </tr>
        </thead>
        <tbody class="flex">
          <tr>
            <td>
              {{ product.dcls_month }}
            </td>
            <td>{{ product.fin_prdt_nm }}</td>
            <td>{{ product.kor_co_nm }}</td>
            <td>
              {{ product.mtrt_int !== null ? product.mtrt_int : '-' }}
            </td>
            <td>
              {{ product.max_limit !== null ? product.max_limit : '-' }}
            </td>
            <td>
              {{ product.join_member !== null ? product.join_member : '-' }}
            </td>
            <td>
              {{ product.join_way !== null ? product.join_way : '-' }}
            </td>
            <td>
              {{ product.spcl_cnd !== null ? product.spcl_cnd : '-' }}
            </td>
          </tr>
        </tbody>
      </table>

      <!-- 연금 -->
      <div v-if="route.params.type === 'annuity' && product">
        <p>공시기준월: {{ product.dcls_month }}</p>
        <p>상품명: {{ product.fin_prdt_nm }}</p>
        <p>기관명: {{ product.kor_co_nm }}</p>
        <button v-show="isLiked" @click="doLike">
          <heart class="inline-block h-[20px]"></heart>
        </button>
        <button v-show="!isLiked" @click="doLike">
          <heartOutline class="inline-block h-[20px]"></heartOutline></button
        >{{ numberOfLikes }}
        <hr />
        <p>상품 유형: {{ product.prdt_type_nm }}</p>
        <p>
          가입 방법: {{ product.join_way !== null ? product.join_way : '-' }}
        </p>
        <hr />
        <p>평균 수익률: {{ product.avg_prft_rate }}</p>
        <p>전년도 수익률: {{ product.btrm_prft_rate_1 }}</p>
        <p>2년전 수익률: {{ product.btrm_prft_rate_2 }}</p>
        <p>3년전 수익률: {{ product.btrm_prft_rate_3 }}</p>
      </div>
      <p>가입 여부: {{ isJoined }}</p>
      <button @click="doLike">즐겨찾기 등록</button> |
      <button @click="doJoin">가입상품 목록에 추가</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import undo from 'vue-material-design-icons/undo.vue';
import heart from 'vue-material-design-icons/heart.vue';
import heartOutline from 'vue-material-design-icons/heartOutline.vue';

const product = ref(null);
const userStore = useUserStore();
const route = useRoute();
const router = useRouter();

onMounted(() => {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/`,
    method: 'GET',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      product.value = res.data;
      console.log(product.value);
    })
    .catch(err => {
      router.go(-1);
      alert('로그인 한 사용자만 이용 가능합니다.');
    });
});

// 상품 찜하기
const doLike = function () {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/likes/`,
    method: 'POST',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      console.log('찜하기 성공');
      location.reload();
    })
    .catch(err => {
      console.log('찜하기 실패');
    });
};

// 상품 찜한 사람 수 계산
const numberOfLikes = computed(() => {
  if (product.value === null) return 0;
  return product.value[`${route.params.type}_like_users`].length;
});

// 현재 유저가 좋아요 했는지 확인
const isLiked = computed(() => {
  if (product.value === null) return false;
  const likeUsers = product.value
    ? product.value[`${route.params.type}_like_users`]
    : [];
  return likeUsers.includes(userStore.userPk);
});

// 현재 유저가 가입 했는지 확인
const isJoined = computed(() => {
  if (product.value === null) return false;
  const joinUsers = product.value
    ? product.value[`${route.params.type}_joined_users`]
    : [];
  return joinUsers.includes(userStore.userPk);
});

// 상품 가입하기
const doJoin = function () {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/joins/`,
    method: 'POST',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      console.log('가입 성공');
      location.reload();
    })
    .catch(err => {
      console.log('가입 실패');
    });
};
</script>
<style scoped></style>
