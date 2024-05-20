<template>
  <div>
    <h1>적금 리스트</h1>
    <div>
      <div @click="onClick">
        <span>공시기준월 </span> <span>금융 회사명</span> <span>상품명</span>
        <button value="month_6">6개월</button>
        <button value="month_12">12개월</button>
        <button value="month_24">24개월</button>
        <button value="month_36">36개월</button>
      </div>
      <p v-for="saving in sortedSavings" :key="saving.fin_prdt_nm">
        {{ saving }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProductStore } from '@/stores/products';

const isSorted = ref(true);
const sortedBy = ref('month_12');
const selectedBank = ref(null);
const selectedDuration = ref(null);
const store = useProductStore();

// 마운트될때 연금 불러오는 함수 실행
onMounted(() => {
  store.fetchAnnuity();
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
const sortedSavings = computed(() => {
  const savings = store.savings;
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
    return [...savings].sort(compare);
  } else if (selectedBank.value !== null && selectedDuration.value === null) {
    const filteredSavings = savings.filter(
      obj => obj.kor_co_nm === selectedBank.value,
    );
    return [...filteredSavings].sort(compare);
  } else if (selectedBank.value === null && selectedDuration.value !== null) {
    const filteredSavings = savings.filter(
      obj => obj.selectedDuration !== null,
    );
    return [...filteredSavings].sort(compare);
  } else {
    // 필요에 따라 모든 조건을 처리하는 추가 로직
    const filteredSavings = savings.filter(
      obj =>
        obj.kor_co_nm === selectedBank.value && obj.selectedDuration !== null,
    );
    return [...filteredSavings].sort(compare);
  }
});
</script>

<style scoped></style>
