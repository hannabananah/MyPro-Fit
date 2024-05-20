<template>
  <div>
    <h1>연금리스트</h1>
    <div>
      <div @click="onClick">
        <button>공시제출월</button>
        <button>금융 회사</button>
        <button>상품명</button> <button>공시제출월</button
        ><button>상품 유형</button>
        <button value="avg_prft_rate">평균 수익률</button>
        <button value="btrm_prft_rate_1">작년 수익률</button>
        <button value="btrm_prft_rate_2">2년 전 수익률</button>
        <button value="btrm_prft_rate_3">3년 전 수익률</button>
        {{ sortedAnnuities }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProductStore } from '@/stores/products';
import AnnuityListItem from '@/components/AnnuityListItem.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const isSorted = ref(true);
const sortedBy = ref('avg_prft_rate');

const store = useProductStore();
onMounted(() => {
  store.fetchAnnuity();
});

const onClick = function (event) {
  if (event.target.value !== sortedBy.value) {
    isSorted.value = true;
    sortedBy.value = event.target.value;
  } else {
    isSorted.value = !isSorted.value;
  }
};

// 정렬하기
const sortedAnnuities = computed(() => {
  const annuities = store.annuities; // store에 있는 annuities 데이터 가져오기
  const field = sortedBy.value;
  const sorted = [...annuities].sort((a, b) => {
    if (isSorted.value) {
      return a[field] > b[field] ? 1 : -1;
    } else {
      return a[field] < b[field] ? 1 : -1;
    }
  });
  return sorted;
});
</script>

<style scoped></style>
