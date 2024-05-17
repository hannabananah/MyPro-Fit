import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useExchangeStore = defineStore(
  'exchange',
  () => {
    const fetchExchangeRate = function () {
      axios({
        url: 'http://127.0.0.1:8000/api/v1/exchange_rate/',
        method: 'get',
      })
        .then(res => {
          console.log(res.data);
        })
        .catch(err => {
          console.log(err);
        });
    };

    return { fetchExchangeRate };
  },
  { persist: true },
);
