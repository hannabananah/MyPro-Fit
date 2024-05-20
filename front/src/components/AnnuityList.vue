<template>
  <div>
    <h1>연금리스트</h1>
    <div>
      <AnnuityListItem
        v-for="annuity in store.annuities"
        :key="annuity.fin_prdt_nm"
        :annuity="annuity"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProductStore } from '@/stores/products';
import AnnuityListItem from '@/components/AnnuityListItem.vue';
const store = useProductStore();
onMounted(() => {
  store.fetchAnnuity();
});
</script>

<style scoped></style>
