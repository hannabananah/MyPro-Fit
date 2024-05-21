<template>
  <div class="py-12">
    <h1 class="ml-[15%] text-2xl mb-4 font-bold">예적금 금리 비교</h1>
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="container flex flex-col w-4/5 pl-6 mx-auto"
    >
      <fieldset class="mt-12 mb-8 text-l">
        <legend class="my-1">조회하실 상품을 선택하세요.</legend>
        <router-link
          :class="{
            'btn-active': route.name === 'deposit',
            'btn-inactive': route.name !== 'deposit',
          }"
          class="px-4 mr-2"
          :to="{ name: 'deposit' }"
          >예금 조회</router-link
        >

        <router-link
          :class="{
            'btn-active': route.name === 'saving',
            'btn-inactive': route.name !== 'saving',
          }"
          class="px-4"
          :to="{ name: 'saving' }"
          >적금 조회</router-link
        >

        <!-- <router-link :to="{ name: 'annuity' }">연금 비교</router-link> -->
      </fieldset>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useRoute } from 'vue-router';
import { useProductStore } from '@/stores/products';

const route = useRoute();
const store = useProductStore();
onMounted(() => {
  store.fetchDeposit();
  store.fetchSaving();
});
</script>

<style scoped></style>
