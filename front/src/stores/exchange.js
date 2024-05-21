import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeStore = defineStore(
  'exchange',
  () => {
    const today = ref([]);

    const fetchExchangeRate = function () {
      axios({
        url: 'http://127.0.0.1:8000/exchange-rate/api/v1/today/',
        method: 'get',
      })
        .then(res => {
          // console.log(res.data);
          today.value = res.data.filter(item => item.cur_unit !== 'KRW');
        })
        .catch(err => {
          console.log(err);
        });
    };

    return { fetchExchangeRate, today };
  },
  { persist: true },
);
