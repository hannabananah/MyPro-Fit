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
        @input="convertTokwr"
      />
      <input type="number" placeholder="원화" id="kor" /><label for="kor"
        >원</label
      >
    </form>
    <hr />
    <ExchangeList />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useExchangeStore } from '@/stores/exchange';
import ExchangeList from '@/components/ExchangeList.vue';

const store = useExchangeStore();
const selectedCur = ref(null); // 선택한 통화 저장
const selectedStd = ref('deal_bas_r'); // 선택한 기준 저장
const foreignAmount = ref(0); // 외화 입출력값

// 나중에 해당 코드가 서버 켜질때 자동으로 호출되게 바꿔야함
store.fetchExchangeRate();

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
</script>

<style scoped></style>
