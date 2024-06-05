<template>
  <div class="flex flex-col gap-y-3">
    <Banner />
    <Intro />
    <Service />
    <BestSeller />
    <Footer />
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user';
import { useExchangeStore } from '@/stores/exchange';
import { useProductStore } from '@/stores/products';
import { onMounted } from 'vue';
import Intro from '@/components/Intro.vue';
import Banner from '@/components/Banner.vue';
import Service from '@/components/MainService.vue';
import BestSeller from '@/components/BestSeller.vue';
import Footer from '@/components/Footer.vue';

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
