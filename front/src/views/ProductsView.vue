<template>
  <div>
    <p>예적금 금리 비교 페이지</p>
    <router-link :to="{ name: 'deposit' }">예금 비교</router-link> |
    <router-link :to="{ name: 'saving' }">적금 비교</router-link> |
    <router-link :to="{ name: 'annuity' }">연금 비교</router-link>
    <RouterView />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useProductStore } from '@/stores/products';
const store = useProductStore();
onMounted(() => {
  store.fetchDeposit();
  store.fetchSaving();
});
</script>

<style scoped></style>
