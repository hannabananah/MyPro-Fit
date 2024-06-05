<template>
  <div class="flex flex-col">
    <h1 class="text-xl font-bold">연금 저축</h1>
    <div class="ml-auto">
      <form class="inline-block" id="select-bank">
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
    </div>
    <hr class="mt-4" />
    <div class="h-[600px] overflow-y-auto pb-6">
      <table class="w-full border border-slate-400">
        <tr @click="onClick">
          <th class="border border-slate-300 w-[7%]">공시기준월</th>
          <th class="border border-slate-300 w-[10%]">금융 회사명</th>
          <th class="border border-slate-300 w-[20%]">상품명</th>
          <th class="border border-slate-300 w-[5%]">상품 유형</th>
          <th class="border border-slate-300 w-[5%]">
            <button
              value="avg_prft_rate"
              class="flex items-center justify-center w-full"
            >
              <span>평균 수익률</span>
              <upDown
                class="inline-block"
                v-show="'avg_prft_rate' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'avg_prft_rate' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'avg_prft_rate' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[5%]">
            <button
              value="btrm_prft_rate_1"
              class="flex items-center justify-center w-full"
            >
              <span>작년 수익률</span>
              <upDown
                class="inline-block"
                v-show="'btrm_prft_rate_1' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'btrm_prft_rate_1' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'btrm_prft_rate_1' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[5%]">
            <button
              value="btrm_prft_rate_2"
              class="flex items-center justify-center w-full"
            >
              <span>2년전 수익률</span>
              <upDown
                class="inline-block"
                v-show="'btrm_prft_rate_2' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'btrm_prft_rate_2' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'btrm_prft_rate_2' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[5%]">
            <button
              value="btrm_prft_rate_3"
              class="flex items-center justify-center w-full"
            >
              <span>3년전 수익률</span>
              <upDown
                class="inline-block"
                v-show="'btrm_prft_rate_3' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'btrm_prft_rate_3' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'btrm_prft_rate_3' && !isSorted"
              ></down>
            </button>
          </th>
          <th class="border border-slate-300 w-[5%]">
            <button
              value="annuity_like_users.length"
              class="flex items-center justify-center w-full"
            >
              <span>인기순</span>
              <upDown
                class="inline-block"
                v-show="'annuity_like_users.length' !== sortedBy"
              ></upDown>
              <up
                class="inline-block"
                v-show="sortedBy === 'annuity_like_users.length' && isSorted"
              ></up>
              <down
                class="inline-block"
                v-show="sortedBy === 'annuity_like_users.length' && !isSorted"
              ></down>
            </button>
          </th>
        </tr>
        <tr
          @click="goDetail"
          v-for="annuity in sortedAnnuities"
          :key="annuity.fin_prdt_cd"
          :data-annuity="annuity.fin_prdt_cd"
          class="w-full hover:cursor-pointer"
        >
          <td class="p-2 border border-slate-300">
            {{ annuity.dcls_month }}
          </td>
          <td class="p-2 border border-slate-300">{{ annuity.kor_co_nm }}</td>
          <td class="p-2 border border-slate-300">{{ annuity.fin_prdt_nm }}</td>
          <td class="p-2 text-center border border-slate-300">
            {{ annuity.prdt_type_nm }}
          </td>
          <td class="text-center border border-slate-300">
            {{ annuity.avg_prft_rate !== null ? annuity.avg_prft_rate : '-' }}
          </td>
          <td class="text-center border border-slate-300">
            {{
              annuity.btrm_prft_rate_1 !== null ? annuity.btrm_prft_rate_1 : '-'
            }}
          </td>
          <td class="text-center border border-slate-300">
            {{
              annuity.btrm_prft_rate_2 !== null ? annuity.btrm_prft_rate_2 : '-'
            }}
          </td>
          <td class="text-center border border-slate-300">
            {{
              annuity.btrm_prft_rate_3 !== null ? annuity.btrm_prft_rate_3 : '-'
            }}
          </td>
          <td class="text-center border border-slate-300">
            {{
              annuity.annuity_like_users.length !== null
                ? annuity.annuity_like_users.length
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

const router = useRouter();
const isSorted = ref(true);
const sortedBy = ref('avg_prft_rate');
const selectedBank = ref('all');
const selectedDuration = ref('all');
const store = useProductStore();
const banks = [
  '미래에셋자산운용',
  '케이씨지아이자산운용 주식회사',
  '엔에이치아문디자산운용주식회사',
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
const sortedAnnuities = computed(() => {
  const annuities = store.annuities;
  const field = sortedBy.value;
  const compare = (a, b) => {
    if (field === 'annuity_like_users.length') {
      const valueA = a['annuity_like_users'].length;
      const valueB = b['annuity_like_users'].length;

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
  };

  // 선택한 은행이나 기간이 있으면 필터링 후 정렬
  if (selectedBank.value === 'all' && selectedDuration.value === 'all') {
    return [...annuities].sort(compare);
  } else if (selectedBank.value !== 'all' && selectedDuration.value === 'all') {
    const filteredAnnuities = annuities.filter(
      obj => obj.kor_co_nm === selectedBank.value,
    );
    return [...filteredAnnuities].sort(compare);
  } else if (selectedBank.value === 'all' && selectedDuration.value !== 'all') {
    const filteredAnnuities = annuities.filter(
      obj => obj[selectedDuration.value] !== null,
    );
    return [...filteredAnnuities].sort(compare);
  } else {
    // 필요에 따라 모든 조건을 처리하는 추가 로직
    const filteredAnnuities = annuities.filter(
      obj =>
        obj.kor_co_nm === selectedBank.value &&
        obj[selectedDuration.value] !== null,
    );
    return [...filteredAnnuities].sort(compare);
  }
});

// 클릭 시 디테일 페이지로 이동
const goDetail = function (event) {
  // data-deposit 속성을 읽어옴
  const annuityId = event.currentTarget.dataset.annuity;
  router.push({
    name: 'product-detail',
    params: { type: 'annuity', code: `${annuityId}` },
  });
  //
};
</script>

<style scoped></style>
