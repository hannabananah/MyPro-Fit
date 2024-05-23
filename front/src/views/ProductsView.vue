<template>
  <h1 class="ml-[14%] text-2xl mb-3 font-bold mt-1">예적금 금리 비교</h1>
  <div
    class="flex flex-col w-4/5 px-6 mx-auto overflow-y-auto border shadow-lg rounded-3xl border-slate-200 border-box"
  >
    <fieldset class="h-full my-2 text-lg">
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
</template>

<script setup>
import { onMounted } from 'vue';
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
