<template>
  <div class="h-[calc(100vh-64px)] py-12">
    <div
    class="h-full container relative flex flex-col items-center w-4/5 mx-auto overflow-hidden rounded-[80px] shadow-md bg-slate-100 flex-1"
    >
      <img width="100%" src="@/assets/images/exchange.svg" alt="환율계산 페이지 헤더 이미지"   class="object-cover w-full overflow-hidden grayscale-[40%] h-56 blur-[3px]"/>
      <h1
        class="absolute text-5xl font-bold tracking-widest text-center text-white top-24"
      >
        환율 계산기
      </h1>
      <div style="width: 50%" class="flex flex-col items-center justify-center h-full">
        <div style="width: 60%" class="flex justify-between">
          <div
            class="flex items-center justify-center border border-solid border-sky-700 min-h-10"
            style="border-radius: 16px;
            width:40%;"
          >
            <form>
              <select
                style="background-color:transparent;"
                id="standard" v-model="selectedStd">
                <option value="deal_bas_r">매매기준율</option>
                <option value="tts">보내실때</option>
                <option value="ttb">받으실때</option>
              </select>
            </form>
          </div>
          <div
            class="flex items-center justify-center px-5 border border-solid border-sky-700 min-h-10"
            style="border-radius: 16px; width:60%; margin-left:1px;"
          >
            <form>
              <select
                style="text-align-last: center; margin-right: 10px; background-color:transparent;"
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
            class="flex items-center justify-between w-full p-3 mt-6 border border-solid border-sky-700"
            style="border-radius: 16px"
          >
            <input
              type="text"
              placeholder="원화"
              id="kor"
              :value="formatNumberWithCommas(krwAmount)"
              @input="e => { krwAmount = e.target.value.replace(/,/g, ''); inputForeignToKwr(); }"
              style="width: 70%; padding-left: 10%"
              class="bg-transparent"
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
            class="flex items-center justify-between w-full p-3 mt-4 border border-solid border-sky-700"
            style="border-radius: 16px"
          >
          <input
              id="foreign"
              type="text"
              placeholder="외화"
              :value="formatNumberWithCommas(inputForeignAmount)"
              @input.prevent="e => { inputForeignAmount = e.target.value.replace(/,/g, ''); convertToKrw(); }"
              style="width: 70%; padding-left: 10%"
              class="bg-transparent"
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
            class="flex items-center justify-between w-full p-3 mt-6 border border-solid border-sky-700"
            style="border-radius: 16px"
          >
            <input
              type="text"
              placeholder="원화"
              id="kor"
              :value="formatNumberWithCommas(inputKrwAmount)"
              @input="e => { inputKrwAmount = e.target.value.replace(/,/g, ''); convertToForeign(); }"
              style="width: 70%; padding-left: 10%"
              class="bg-transparent"
            /><label style="padding-right: 10%" for="kor">원</label>
          </div>
          <p style="margin-top: 1rem" class="text-center text-gray-500">
            1 KOR = {{ krwExchangeRate }} {{ selectedCur }}
            <div class="flex justify-center mt-4">
              <img src="@/assets/icons/exchange-icon.svg" alt="" />
            </div>
          </p>
          <div
            class="flex items-center justify-between w-full p-3 mt-4 border border-solid border-sky-700"
            style="border-radius: 16px"
          >
          <input
              id="foreign"
              type="text"
              placeholder="외화"
              class="bg-transparent"
              :value="formatNumberWithCommas(foreignAmount)"
              @input="e => { foreignAmount = e.target.value.replace(/,/g, ''); inputKwrToForeign(); }"
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
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';
import { useExchangeStore } from '@/stores/exchange';
import { formatNumberWithCommas, parseNumberWithCommas } from '@/utils/formatNumber';

const store = useExchangeStore();
const selectedCur = ref(null);
const selectedCurName = ref(null);
const selectedStd = ref('deal_bas_r');
const inputForeignAmount = ref('');
const foreignAmount = ref('');
const inputKrwAmount = ref('');
const krwAmount = ref('');
const isKwrToFor = ref(false);

const krwExchangeRate = computed(() => {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    return formatNumberWithCommas((1000 / exchangeRate).toFixed(2));
  }
});

const thisCountryRate = computed(() => {
  const result = {
    today: null,
  };
  if (selectedCur.value && selectedStd.value) {
    const filteredToday = store.today.filter(
      obj => obj.cur_unit === selectedCur.value,
    );
    if (filteredToday.length > 0) {
      result.today = filteredToday[0][selectedStd.value];
    }
  }

  return result;
});

const convertToKrw = function () {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(parseNumberWithCommas(inputForeignAmount.value)) && !isNaN(exchangeRate)) {
      krwAmount.value = formatNumberWithCommas(
        (parseNumberWithCommas(inputForeignAmount.value) * exchangeRate).toFixed(2)
      );
    } else {
      krwAmount.value = null;
      console.error('Invalid input value or exchange rate');
    }
  }
};

const convertToForeign = function () {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(parseNumberWithCommas(inputKrwAmount.value)) && !isNaN(exchangeRate)) {
      foreignAmount.value = formatNumberWithCommas(
        (parseNumberWithCommas(inputKrwAmount.value) / exchangeRate).toFixed(2)
      );
    } else {
      foreignAmount.value = null;
      console.error('Invalid input value or exchange rate');
    }
  }
};

// 외화가 바뀌었을 때 동작 -> 한화 변경
watch([foreignAmount, thisCountryRate, isKwrToFor], () => {
  if (isKwrToFor.value === false){
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(parseNumberWithCommas(foreignAmount.value)) && !isNaN(exchangeRate)) {
      krwAmount.value = formatNumberWithCommas(
        (parseNumberWithCommas(inputForeignAmount.value) * exchangeRate).toFixed(2)
      );
    }
  }}
});

// 한화가 바뀌었을 때 동작 -> 외화 변경
watch([krwAmount, thisCountryRate, isKwrToFor], () => {
  if (isKwrToFor.value === true) {
  const exchangeRateString = thisCountryRate.value.today;
  if (exchangeRateString) {
    const exchangeRate = parseFloat(exchangeRateString.replace(/,/g, ''));
    if (!isNaN(parseNumberWithCommas(krwAmount.value)) && !isNaN(exchangeRate)) {
      foreignAmount.value = formatNumberWithCommas(
        (parseNumberWithCommas(inputKrwAmount.value) / exchangeRate).toFixed(2)
      );
    }
  }}
});

const inputForeignToKwr = function () {
  isKwrToFor.value = true;
  inputKrwAmount.value = krwAmount.value;
};

const inputKwrToForeign = function () {
  isKwrToFor.value = false;
  inputForeignAmount.value = foreignAmount.value;
};

watch(selectedCur, newVal => {
  const thisCountry = store.today.find(obj => obj.cur_unit == newVal);
  if (thisCountry) {
    console.log(thisCountry.cur_nm.split(' ').length) 
    if (thisCountry.cur_nm.split(' ').length > 1) {
    const parts = thisCountry.cur_nm.split(' ');
    selectedCurName.value = parts.slice(1).join(' ');
  } else {selectedCurName.value = thisCountry.cur_nm;}
  } else {
    selectedCurName.value = 'Unknown Currency';
  }
});
</script>