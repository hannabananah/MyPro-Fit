<template>
  <div class="flex flex-col gap-y-3">
    <!-- <p>
      <strong>{{ userStore.nickname }}</strong
      >님 안녕하세요!
    </p>

    <!-- 캐러셀 -->
    <Banner />
    <!-- 인트로 섹션 -->
    <Intro />
    <!-- 주요 서비스 -->
    <Service />
    <!-- 예적금, 연금 추천 서비스 -->
    <BestSeller />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';
import { useExchangeStore } from '@/stores/exchange';
import { useProductStore } from '@/stores/products';
import { onMounted } from 'vue';
import Intro from '@/components/Intro.vue';
import Banner from '@/components/Banner.vue';
import Service from '@/components/MainService.vue';
import BestSeller from '@/components/BestSeller.vue';

const userStore = useUserStore();
const productstore = useProductStore();

const store = useExchangeStore();
store.fetchExchangeRate();

onMounted(() => {
  if (userStore.isLogin) {
    userStore.getUserInfo();
  }
  productstore.fetchDeposit();
  productstore.fetchAnnuity();
  productstore.fetchSaving();
});
</script>
