<template>
  <div>
    <h1>연금리스트</h1>
    <div>
      <div @click="onClick">
        <span>공시제출월</span>
        <span>금융 회사명</span>
        <span>상품명</span> <span>상품 유형</span>
        <button value="avg_prft_rate">평균 수익률</button>
        <button value="btrm_prft_rate_1">작년 수익률</button>
        <button value="btrm_prft_rate_2">2년 전 수익률</button>
        <button value="btrm_prft_rate_3">3년 전 수익률</button>
        <p v-for="annuity in sortedAnnuities" :key="annuity.fin_prdt_nm">
          {{ annuity }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProductStore } from '@/stores/products';

const isSorted = ref(true);
const sortedBy = ref('avg_prft_rate');
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
const sortedAnnuities = computed(() => {
  const annuities = store.annuities;
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
    return [...annuities].sort(compare);
  } else if (selectedBank.value !== null && selectedDuration.value === null) {
    const filteredAnnuities = annuities.filter(
      obj => obj.kor_co_nm === selectedBank.value,
    );
    return [...filteredAnnuities].sort(compare);
  } else if (selectedBank.value === null && selectedDuration.value !== null) {
    const filteredAnnuities = annuities.filter(
      obj => obj.selectedDuration !== null,
    );
    return [...filteredAnnuities].sort(compare);
  } else {
    // 필요에 따라 모든 조건을 처리하는 추가 로직
    const filteredAnnuities = annuities.filter(
      obj =>
        obj.kor_co_nm === selectedBank.value && obj.selectedDuration !== null,
    );
    return [...filteredAnnuities].sort(compare);
  }
});
</script>

<style scoped></style>
