import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeStore = defineStore(
  'exchange',
  () => {
    const today = ref([]);
    const lastWeek = ref([]);
    const lastMonth = ref([]);
    const fetchExchangeRate = function () {
      axios({
        url: 'http://127.0.0.1:8000/exchange-rate/api/v1/today/',
        method: 'get',
      })
        .then(res => {
          console.log(res.data);
          today.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
      axios({
        url: 'http://127.0.0.1:8000/exchange-rate/api/v1/last-week/',
        method: 'get',
      })
        .then(res => {
          console.log(res.data);
          lastWeek.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
      axios({
        url: 'http://127.0.0.1:8000/exchange-rate/api/v1/last-month/',
        method: 'get',
      })
        .then(res => {
          console.log(res.data);
          lastMonth.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    // 특정시간의 특정국가의 환율 객체를 뽑는다
    const getCountryEx = function (time, country) {
      console.log(time.value);
      // const obj = time.value.filter(exc => exc.cur_unit === country);
      // console.log('선택한 국가의 환율: ', obj);
    };

    return { fetchExchangeRate, lastWeek, today, lastMonth, getCountryEx };
  },
  { persist: true },
);
