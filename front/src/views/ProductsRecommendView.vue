<template>
  <div class="py-12">
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="flex flex-col items-center w-3/5 mx-auto"
    >
      <img src="@/assets/images/bankproducts.png" alt="" />

      <h1 class="-mt-8 text-2xl italic font-bold mb-8">
        "금융 상품을 추천해드려요 !"
      </h1>

      <p class="text-l text-center">
        입력하신 정보를 바탕으로 <br />
        <span v-if="userStore.isLogin" class="font-bold">{{
          userStore.nickname
        }}</span>
        <span v-if="!userStore.isLogin">회원</span>님에게
        <span class="font-bold text-sky-700 text-xl italic">Fit</span> 한 금융
        상품을 추천해드립니다.
      </p>
      <button
        v-if="userStore.isLogin"
        class="btn-active w-[50%] my-6"
        @click="onClick"
      >
        상품 추천 받기
      </button>
      <button
        v-if="!userStore.isLogin"
        class="btn-active w-[50%] my-6"
        @click="router.push({ name: 'login' })"
      >
        로그인 후 상품 추천 받기
      </button>

      <img class="mb-4" src="@/assets/images/logo.svg" alt="" />
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import { useRecommendStore } from '@/stores/recommend';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const userStore = useUserStore();
const recommendStore = useRecommendStore();

const onClick = function () {
  recommendStore.fetchRecommendedProducts();
  console.log('클릭!');
};
</script>
