<template>
  <div class="flex flex-col">
    <h1 class="text-xl font-bold">정기 적금</h1>
    <div class="ml-auto">
      <form class="inline-block mr-3" id="select-bank">
        <select
          class="px-2 bg-white btn-inactive hover:bg-white text-start"
          name="bank"
          id="bank"
          v-model="selectedBank"
        >
          <option value="all">전체 목록</option>
          <option v-for="bank in banks" :value="bank">
            {{ bank }}
          </option>
        </select>
      </form>
      <form class="inline-block" id="select-duration">
        <select
          class="px-2 py-0 bg-white btn-inactive hover:bg-white text-start"
          name="duration"
          id="duration"
          v-model="selectedDuration"
        >
          <option value="all">전체 기간</option>
          <option v-for="duration in durations" :value="duration.value">
            {{ duration.name }}
          </option>
        </select>
      </form>
    </div>
    <hr class="mt-4" />
    <div class="h-[600px] overflow-y-auto pb-6">
      <table class="w-full border border-slate-400">
        <tr @click="onClick">
          <th class="border border-slate-300 w-[10%]">공시기준월</th>
          <th class="border border-slate-300 w-[10%]">금융 회사명</th>
          <th class="border border-slate-300 w-[30%]">상품명</th>
          <th class="border border-slate-300 w-[8%]">
            <button
              value="month_6"
              class="flex items-center justify-center w-full"
            >
              <span>6개월</span>
              <upDown
                class="inline-block"
                v-show="sortedBy !== 'month_6'"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'month_6' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'month_6' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[8%]">
            <button
              value="month_12"
              class="flex items-center justify-center w-full"
            >
              <span>12개월</span>
              <upDown
                class="inline-block"
                v-show="sortedBy !== 'month_12'"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'month_12' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'month_12' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[8%]">
            <button
              value="month_24"
              class="flex items-center justify-center w-full"
            >
              <span>24개월</span>
              <upDown
                class="inline-block"
                v-show="'month_24' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'month_24' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'month_24' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[8%]">
            <button
              value="month_36"
              class="flex items-center justify-center w-full"
            >
              <span>36개월</span>
              <upDown
                class="inline-block"
                v-show="'month_36' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'month_36' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'month_36' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[8%]">
            <button
              value="saving_like_users.length"
              class="flex items-center justify-center w-full"
            >
              <span>인기순</span>
              <upDown
                class="inline-block"
                v-show="'saving_like_users.length' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'saving_like_users.length' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'saving_like_users.length' && !isSorted"
              ></down>
            </button>
          </th>
        </tr>

        <tr
          class="w-full hover:cursor-pointer"
          @click="goDetail"
          v-for="saving in sortedSavings"
          :key="saving.fin_prdt_cd"
          :data-saving="saving.fin_prdt_cd"
        >
          <td class="p-2 border border-slate-300">
            {{ saving.dcls_month }}
          </td>
          <td class="p-2 border border-slate-300">{{ saving.kor_co_nm }}</td>
          <td class="p-2 border border-slate-300">{{ saving.fin_prdt_nm }}</td>
          <td class="text-center border border-slate-300">
            {{ saving.month_6 !== null ? saving.month_6 : '-' }}
          </td>
          <td class="text-center border border-slate-300">
            {{ saving.month_12 !== null ? saving.month_12 : '-' }}
          </td>
          <td class="text-center border border-slate-300">
            {{ saving.month_24 !== null ? saving.month_24 : '-' }}
          </td>
          <td class="text-center border border-slate-300">
            {{ saving.month_36 !== null ? saving.month_36 : '-' }}
          </td>
          <td class="text-center border border-slate-300">
            {{
              saving.saving_like_users.length !== null
                ? saving.saving_like_users.length
                : '-'
            }}
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProductStore } from '@/stores/products';
import { useRouter } from 'vue-router';
import upDown from 'vue-material-design-icons/menuSwapOutline.vue';
import up from 'vue-material-design-icons/menuUp.vue';
import down from 'vue-material-design-icons/menuDown.vue';

const isSorted = ref(true);
const sortedBy = ref('month_12');
const selectedBank = ref('all');
const selectedDuration = ref('all');
const router = useRouter();
const store = useProductStore();
const banks = [
  '경남은행',
  '국민은행',
  '광주은행',
  '농협은행주식회사',
  '대구은행',
  '부산은행',
  '수협은행',
  '신한은행',
  '우리은행',
  '전북은행',
  '제주은행',
  '중소기업은행',
  '주식회사 카카오뱅크',
  '주식회사 케이뱅크',
  '토스뱅크 주식회사',
  '하나은행',
  '한국산업은행',
  '한국스탠다드차타드은행',
];
const durations = [
  { value: 'month_6', name: '6개월' },
  { value: 'month_12', name: '12개월' },
  { value: 'month_24', name: '24개월' },
  { value: 'month_36', name: '36개월' },
];

// 마운트될때 연금 불러오는 함수 실행
onMounted(() => {
  store.fetchAnnuity();
});

// 정렬버튼 클릭 시 오름차순, 비오름차순 토글
const onClick = function (event) {
  if (event.target.closest('button').value !== sortedBy.value) {
    isSorted.value = true;
    sortedBy.value = event.target.closest('button').value;
  } else {
    isSorted.value = !isSorted.value;
  }
};

// 정렬하는 computed 속성
const sortedSavings = computed(() => {
  const savings = store.savings;
  const field = sortedBy.value;
  const compare = (a, b) => {
    if (field === 'saving_like_users.length') {
      const valueA = a['saving_like_users'].length;
      const valueB = b['saving_like_users'].length;

      if (valueA === null) return 1;
      if (valueB === null) return -1;

      if (isSorted.value) {
        return valueA > valueB ? 1 : -1;
      } else {
        return valueA < valueB ? 1 : -1;
      }
    } else {
      const valueA = a[field];
      const valueB = b[field];
      if (valueA === null) return 1;
      if (valueB === null) return -1;

      if (isSorted.value) {
        return valueA > valueB ? 1 : -1;
      } else {
        return valueA < valueB ? 1 : -1;
      }
    }
    // null 값을 뒤로 보내기 위한 비교 로직
  };

  // 선택한 은행이나 기간이 있으면 필터링 후 정렬
  if (savings) {
    if (selectedBank.value === 'all' && selectedDuration.value === 'all') {
      return [...savings].sort(compare);
    } else if (
      selectedBank.value !== 'all' &&
      selectedDuration.value === 'all'
    ) {
      const filteredSavings = savings.filter(
        obj => obj.kor_co_nm === selectedBank.value,
      );
      return [...filteredSavings].sort(compare);
    } else if (
      selectedBank.value === 'all' &&
      selectedDuration.value !== 'all'
    ) {
      sortedBy.value = selectedDuration.value;
      const filteredSavings = savings.filter(
        obj => obj[selectedDuration.value] !== null,
      );
      return [...filteredSavings].sort(compare);
    } else {
      // 필요에 따라 모든 조건을 처리하는 추가 로직
      sortedBy.value = selectedDuration.value;
      const filteredSavings = savings.filter(
        obj =>
          obj.kor_co_nm === selectedBank.value &&
          obj[selectedDuration.value] !== null,
      );
      return [...filteredSavings].sort(compare);
    }
  }
});

// 클릭 시 디테일 페이지로 이동
const goDetail = function (event) {
  // data-deposit 속성을 읽어옴
  const savingId = event.currentTarget.dataset.saving;
  router.push({
    name: 'product-detail',
    params: { type: 'saving', code: `${savingId}` },
  });
  //
};
</script>

<style scoped></style>
