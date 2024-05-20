<template>
  <div>
    <h1>적금 리스트</h1>
    <div>
      <SavingListItem
        v-for="saving in store.savings"
        :key="saving.fin_prdt_nm"
        :saving="saving"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/products';
import SavingListItem from '@/components/SavingListItem.vue';
const store = useProductStore();
onMounted(() => {
  store.fetchSaving();
});
</script>

<style scoped></style>
