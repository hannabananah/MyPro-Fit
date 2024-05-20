<template>
  <div>
    <h1>예금리스트</h1>
    <DepositListItem
      v-for="deposit in store.deposits"
      :key="deposit.fin_prdt_nm"
      :deposit="deposit"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/products';
import DepositListItem from '@/components/DepositListItem.vue';
const store = useProductStore();
onMounted(() => {
  store.fetchDeposit();
});
</script>

<style scoped></style>
