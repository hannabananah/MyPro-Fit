<template>
  <div>
    <h1>환율계산기 페이지</h1>
    <form @submit.prevent="getToday">
      <label for="cur">송금할 외화 : </label>
      <select name="exchange" id="cur" v-model="selectedCur">
        <option value="AED">아랍에미리트 디르함</option>
        <option value="AUD">호주 달러</option>
        <option value="BHD">바레인 디나르</option>
        <option value="BND">브루나이 달러</option>
        <option value="CAD">캐나다 달러</option>
        <option value="CHF">스위스 프랑</option>
        <option value="CNH">위안화</option>
        <option value="EUR">유로</option>
        <option value="GBP">영국 파운드</option>
        <option value="HKD">홍콩 달러</option>
        <option value="IDR(100)">인도네시아 루피아</option>
        <option value="JPY(100)">일본 옌</option>
        <option value="KRW">한국 원</option>
        <option value="KWD">쿠웨이트 디나르</option>
        <option value="MYR">말레이지아 링기트</option>
        <option value="NOK">노르웨이 크로네</option>
        <option value="NZD">뉴질랜드 달러</option>
        <option value="SAR">사우디 리얄</option>
        <option value="SEK">스웨덴 크로나</option>
        <option value="SGD">싱가포르 달러</option>
        <option value="THB">태국 바트</option>
        <option value="USD">미국 달러</option>
      </select>
      <input type="submit" value="Submit" />
    </form>
    <hr />
    <ExchangeList />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useExchangeStore } from '@/stores/exchange';
import ExchangeList from '@/components/ExchangeList.vue';

const store = useExchangeStore();

// 나중에 해당 코드가 서버 켜질때 자동으로 호출되게 바꿔야함
store.fetchExchangeRate();

// 선택한 통화 저장
const selectedCur = ref(null);

// 오늘 환율 불러오는 함수
const getToday = function () {
  console.log(store.today.filter(obj => obj.cur_unit === selectedCur.value));
};
// 지난주 환율 불러오는 함수
const getLastWeek = function () {
  console.log(store.lastWeek.filter(obj => obj.cur_unit === selectedCur.value));
};
// 저번 달 환율 불러오는 함수
const getLastMonth = function () {
  console.log(
    store.lastMonth.filter(obj => obj.cur_unit === selectedCur.value),
  );
};
</script>

<style scoped></style>
