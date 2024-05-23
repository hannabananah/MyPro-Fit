<template>
  <div>
    <h1>상품 추천 페이지</h1>
    <div>
      <p>
        입력하신 정보를 바탕으로 {{ userStore.nickname }}님에게 Fit 한 금융
        상품을 추천해드려요 !
      </p>
    </div>
    <button @click="onClick">상품 추천 받기</button>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import { useRecommendStore } from '@/stores/recommend';
import { ref } from 'vue';

const userStore = useUserStore();
const recommendStore = useRecommendStore();

const onClick = function () {
  recommendStore.fetchRecommendedProducts();
  console.log('클릭!');
};
</script>
