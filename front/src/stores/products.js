import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductStore = defineStore(
  'product',
  () => {
    const deposits = ref();
    const savings = ref();
    const annuities = ref();
    const fetchDeposit = function () {
      axios({
        url: 'http://127.0.0.1:8000/products/depo/',
        method: 'get',
      })
        .then(res => {
          deposits.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };
    return {};
  },
  { persist: true },
);
