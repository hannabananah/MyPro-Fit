<template>
  <div class="py-12">
    <div
      style="border-radius: 60px; overflow: hidden"
      class="container mx-auto w-4/5 flex items-center flex-col"
    >
      <img width="100%" src="@/assets/images/exchange.svg" alt="" />
      <div style="width: 50%" class="my-8 flex flex-col items-center">
        <p class="text-2xl text-center my-8">환율 계산기</p>
        <div style="width: 60%" class="flex justify-between">
          <div
            class="border border-solid border-sky-700 min-w-40 min-h-10 flex items-center justify-center"
            style="border-radius: 16px"
          >
            <form>
              <select id="standard" v-model="selectedStd">
                <option value="deal_bas_r">매매기준율</option>
                <option value="tts">보내실때</option>
                <option value="ttb">받으실때</option>
              </select>
            </form>
          </div>
          <div
            class="border border-solid border-sky-700 min-w-40 min-h-10 flex items-center justify-center px-5"
            style="border-radius: 16px"
          >
            <form>
              <select
                style="text-align-last: center; margin-right: 10px"
                name="exchange"
                id="cur"
                v-model="selectedCur"
              >
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
          </div>
        </div>

        <!-- 사용자가 외화를 입력할 때 -->

        <form v-show="!isKwrToFor" style="width: 60%; margin-top: 1rem">
          <div
            class="border border-solid border-sky-700 p-3 w-full flex justify-between itmes-center mt-6"
            style="border-radius: 16px"
          >
            <input
              type="number"
              placeholder="원화"
              id="kor"
              v-model="krwAmount"
              @click="inputForeignToKwr"
              @keydown.tab="inputForeignToKwr"
              style="width: 70%; padding-left: 10%"
            />
            <label style="padding-right: 10%" for="kor">원</label>
          </div>
          <p style="margin-top: 1rem" class="text-center text-gray-500">
            1 KOR = {{ krwExchangeRate }} {{ selectedCur }}
            <div class="flex justify-center mt-4">
            <img src="@/assets/icons/exchange-icon.svg" alt="" />
          </div>
          </p>
          <div
            class="border border-solid border-sky-700 p-3 w-full flex justify-between itmes-center mt-4"
            style="border-radius: 16px"
          >
            <input
              id="foreign"
              type="number"
              placeholder="외화"
              v-model.number="inputForeignAmount"
              @input="convertToKrw"
              style="width: 70%; padding-left: 10%"
            />
            <label style="padding-right: 10%" for="foreign">{{
              selectedCurName
            }}</label>
          </div>
          <p style="margin-top: 1rem" class="text-center text-gray-500">
            1 {{ selectedCur }} = {{ thisCountryRate.today }} KOR
          </p>
        </form>

        <!-- 사용자가 원화를 입력할 때 -->
        <form v-show="isKwrToFor" style="width: 60%; margin-top: 1rem">
          <div
            class="border border-solid border-sky-700 p-3 w-full flex justify-between itmes-center mt-6"
            style="border-radius: 16px"
          >
            <input
              type="number"
              placeholder="원화"
              id="kor"
              v-model="inputKrwAmount"
              @input="convertToForeign"
              style="width: 70%; padding-left: 10%"
            /><label style="padding-right: 10%" for="kor">원</label>
          </div>
          <p style="margin-top: 1rem" class="text-center text-gray-500">
            1 KOR = {{ krwExchangeRate }} {{ selectedCur }}
            <div class="flex justify-center mt-4">
            <img src="@/assets/icons/exchange-icon.svg" alt="" />
          </div>
          </p>
          <div
            class="border border-solid border-sky-700 p-3 w-full flex justify-between itmes-center mt-4"
            style="border-radius: 16px"
          >
            <input
              type="number"
              placeholder="외화"
              v-model.number="foreignAmount"
              @click="inputKwrToForeign"
              @keydown.tab="inputKwrToForeign"
              style="width: 70%; padding-left: 10%"
            />
            <label style="padding-right: 10%" for="foreign">{{
              selectedCurName
            }}</label>
          </div>
          <p style="margin-top: 1rem" class="text-center text-gray-500">
            1 {{ selectedCur }} = {{ thisCountryRate.today }} KOR
          </p>
        </form>
      </div>
    </div>

    <ExchangeList />
  </div>
</template>
<style scoped></style>
<script setup>
import { ref, computed, watch } from 'vue';
import { useExchangeStore } from '@/stores/exchange';
import ExchangeList from '@/components/ExchangeList.vue';

const store = useExchangeStore();
const selectedCur = ref(null); // 선택한 통화 저장
const selectedCurName = ref(null); // 선택한 통화의 이름
const selectedStd = ref('deal_bas_r'); // 선택한 기준 저장
const inputForeignAmount = ref(0);
const foreignAmount = ref(0); // 외화 입출력값
const inputKrwAmount = ref(0); // 사용자 입력 원화값
const krwAmount = ref(0); // 원화
const isKwrToFor = ref(false); // 사용자가 원화를 입력했을 때
const krwExchangeRate = computed(() => {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    return (1000 / exchangeRate).toFixed(2);
  }
});

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
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(inputForeignAmount.value) && !isNaN(exchangeRate)) {
      krwAmount.value = parseFloat(
        (inputForeignAmount.value * exchangeRate).toFixed(2),
      );
    } else {
      krwAmount.value = null;
      console.error('Invalid input value or exchange rate');
    }
  }
};

// 원화를 외화로 변환하는 함수
const convertToForeign = function () {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(inputKrwAmount.value) && !isNaN(exchangeRate)) {
      foreignAmount.value = parseFloat(
        (inputKrwAmount.value / exchangeRate).toFixed(2),
      );
    } else {
      foreignAmount.value = null;
      console.error('Invalid input value or exchange rate');
    }
  }
};

// 양방향 데이터 바인딩: 두 개의 watch 함수가 상호 작용하여 한쪽 값이 변경될 때 다른 쪽 값이 자동으로 업데이트
// 원화 업데이트
watch([foreignAmount, thisCountryRate], () => {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(foreignAmount.value) && !isNaN(exchangeRate)) {
      // 원화 업데이트
      krwAmount.value = (foreignAmount.value * exchangeRate).toFixed(2);
    }
  }
});

// 외화 업데이트
watch([krwAmount, thisCountryRate], () => {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(krwAmount.value) && !isNaN(exchangeRate)) {
      foreignAmount.value = (krwAmount.value / exchangeRate).toFixed(2);
    }
  }
});

// 외화입력 -> 원화입력 전환
const inputForeignToKwr = function () {
  isKwrToFor.value = true;
  inputKrwAmount.value = krwAmount.value;
};

// 원화입력 -> 외화입력 전환
const inputKwrToForeign = function () {
  isKwrToFor.value = false;
  inputForeignAmount.value = foreignAmount.value;
};

// 외화 변경할 때마다 그에 맞는 화폐 단위 출력
watch(selectedCur, newVal => {
  const thisCountry = store.today.find(obj => obj.cur_unit === newVal);
  if (thisCountry) {
    const parts = thisCountry.cur_nm.split(' ');
    selectedCurName.value = parts.slice(1).join(' ');
  } else {
    selectedCurName.value = 'Unknown Currency';
  }
});
</script>
