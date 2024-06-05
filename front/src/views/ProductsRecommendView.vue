<template>
  <div
    class="flex items-center justify-center h-[calc(100vh-64px)] bg-gray-100"
  >
    <div
      class="flex flex-col items-center w-3/5 p-8 mx-auto overflow-hidden bg-white shadow-lg rounded-3xl"
    >
      <img
        src="@/assets/images/bankproducts.png"
        alt="은행 상품 추천 페이지 이미지"
        class="w-full mb-4"
      />
      <h1 class="mb-8 text-2xl italic font-bold">
        "금융 상품을 추천해드려요 !"
      </h1>
      <p class="text-lg text-center">
        입력하신 정보를 바탕으로 <br />
        <span v-if="userStore.isLogin" class="font-bold">{{
          userStore.nickname
        }}</span>
        <span v-if="!userStore.isLogin">회원</span>님에게
        <span class="text-xl italic font-bold text-sky-700">Fit</span> 한 금융
        상품을 추천해드립니다.
      </p>
      <button
        v-if="userStore.isLogin"
        class="w-1/2 my-6 btn-active"
        @click="onClick"
      >
        상품 추천 받기
      </button>
      <button
        v-if="!userStore.isLogin"
        class="w-1/2 my-6 btn-active"
        @click="router.push({ name: 'login' })"
      >
        로그인 후 상품 추천 받기
      </button>
      <img class="mt-4" src="@/assets/images/logo.svg" alt="로고 이미지" />
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import { useRecommendStore } from '@/stores/recommend';
import { useRouter } from 'vue-router';

const router = useRouter();
const userStore = useUserStore();
const recommendStore = useRecommendStore();

const onClick = function () {
  recommendStore.fetchRecommendedProducts();
};
</script>
