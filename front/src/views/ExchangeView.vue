<template>
  <div>
    <h1>환율계산기 페이지</h1>
    <form>
      <select id="standard" v-model="selectedStd">
        <option value="deal_bas_r">매매기준율</option>
        <option value="tts">보내실때</option>
        <option value="ttb">받으실때</option>
      </select>
    </form>
    <form>
      <label for="cur">송금할 외화 : </label>
      <select name="exchange" id="cur" v-model="selectedCur">
        <option disabled value="">외화 선택</option>
        <option
          v-for="cur in store.today"
          :key="cur.cur_unit"
          :value="cur.cur_unit"
        >
          {{ cur.cur_unit }} {{ cur.cur_nm }}
        </option>
      </select>
    </form>
    <form>
      <input
        type="number"
        placeholder="외화"
        v-model.number="foreignAmount"
        @input="convertToKrw"
      />
      <input
        type="number"
        placeholder="원화"
        id="kor"
        v-model="krwAmount"
        @input="convertToForeign"
      /><label for="kor">원</label>
    </form>
    <hr />
    <ExchangeList />
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useExchangeStore } from '@/stores/exchange';
import ExchangeList from '@/components/ExchangeList.vue';

const store = useExchangeStore();
const selectedCur = ref(null); // 선택한 통화 저장
const selectedStd = ref('deal_bas_r'); // 선택한 기준 저장
const foreignAmount = ref(0); // 외화 입출력값
const krwAmount = ref(0); // 원화 입출력값

// 환율불러오는거

// 해당 국가의 환율 계산
const thisCountryRate = computed(() => {
  const result = {
    today: null,
    lastWeek: null,
    lastMonth: null,
  };

  if (selectedCur.value && selectedStd.value) {
    const filteredToday = store.today.filter(
      obj => obj.cur_unit === selectedCur.value,
    );
    const filteredLastWeek = store.lastWeek.filter(
      obj => obj.cur_unit === selectedCur.value,
    );
    const filteredLastMonth = store.lastMonth.filter(
      obj => obj.cur_unit === selectedCur.value,
    );

    if (filteredToday.length > 0) {
      result.today = filteredToday[0][selectedStd.value];
    }
    if (filteredLastWeek.length > 0) {
      result.lastWeek = filteredLastWeek[0][selectedStd.value];
    }
    if (filteredLastMonth.length > 0) {
      result.lastMonth = filteredLastMonth[0][selectedStd.value];
    }
  }

  return result;
});
// 외화를 원화로 변환하는 함수
const convertToKrw = function () {
  const exchangeRateString = thisCountryRate.value.today;
  const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
  if (!isNaN(foreignAmount.value) && !isNaN(exchangeRate)) {
    krwAmount.value = parseFloat(
      (foreignAmount.value * exchangeRate).toFixed(2),
    );
  } else {
    krwAmount.value = null;
    console.error('Invalid input value or exchange rate');
  }
};

// 원화를 외화로 변환하는 함수
const convertToForeign = function () {
  const exchangeRateString = thisCountryRate.value.today;
  const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
  if (!isNaN(krwAmount.value) && !isNaN(exchangeRate)) {
    foreignAmount.value = parseFloat(
      (krwAmount.value / exchangeRate).toFixed(2),
    );
  } else {
    foreignAmount.value = null;
    console.error('Invalid input value or exchange rate');
  }
};

// Watchers to handle the changes
watch([foreignAmount, thisCountryRate], () => {
  const exchangeRateString = thisCountryRate.value.today;
  const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
  if (!isNaN(foreignAmount.value) && !isNaN(exchangeRate)) {
    krwAmount.value = (foreignAmount.value * exchangeRate).toFixed(2);
  }
});

watch([krwAmount, thisCountryRate], () => {
  const exchangeRateString = thisCountryRate.value.today;
  const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
  if (!isNaN(krwAmount.value) && !isNaN(exchangeRate)) {
    foreignAmount.value = (krwAmount.value / exchangeRate).toFixed(2);
  }
});
</script>

<style scoped></style>
