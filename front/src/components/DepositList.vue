<template>
  <div>
    <h1>예금리스트</h1>
    <div @click="onClick">
      <span>공시기준월 </span> <span>금융 회사명</span> <span>상품명</span>
      <button value="month_6">6개월</button>
      <button value="month_12">12개월</button>
      <button value="month_24">24개월</button>
      <button value="month_36">36개월</button>
    </div>
    <p v-for="deposit in sortedDeposits" :key="deposit.fin_prdt_nm">
      {{ deposit }}
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProductStore } from '@/stores/products';

const store = useProductStore();
const isSorted = ref(true);
const selectedBank = ref(null);
const selectedDuration = ref(null);
const sortedBy = ref('month_12');

onMounted(() => {
  store.fetchDeposit();
});

// 정렬버튼 클릭 시 오름차순, 비오름차순 토글
const onClick = function (event) {
  if (event.target.value !== sortedBy.value) {
    isSorted.value = true;
    sortedBy.value = event.target.value;
  } else {
    isSorted.value = !isSorted.value;
  }
};

// 정렬하는 computed 속성
const sortedDeposits = computed(() => {
  const deposits = store.deposits;
  const field = sortedBy.value;
  const compare = (a, b) => {
    const valueA = a[field];
    const valueB = b[field];

    // null 값을 뒤로 보내기 위한 비교 로직
    if (valueA === null) return 1;
    if (valueB === null) return -1;

    if (isSorted.value) {
      return valueA > valueB ? 1 : -1;
    } else {
      return valueA < valueB ? 1 : -1;
    }
  };

  // 선택한 은행이나 기간이 있으면 필터링 후 정렬
  if (selectedBank.value === null && selectedDuration.value === null) {
    return [...deposits].sort(compare);
  } else if (selectedBank.value !== null && selectedDuration.value === null) {
    const filteredDeposits = deposits.filter(
      obj => obj.kor_co_nm === selectedBank.value,
    );
    return [...filteredDeposits].sort(compare);
  } else if (selectedBank.value === null && selectedDuration.value !== null) {
    const filteredDeposits = deposits.filter(
      obj => obj.selectedDuration !== null,
    );
    return [...filteredDeposits].sort(compare);
  } else {
    // 필요에 따라 모든 조건을 처리하는 추가 로직
    const filteredDeposits = deposits.filter(
      obj =>
        obj.kor_co_nm === selectedBank.value && obj.selectedDuration !== null,
    );
    return [...filteredDeposits].sort(compare);
  }
});
</script>

<style scoped></style>
