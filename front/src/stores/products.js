import { ref } from 'vue';
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
        url: 'http://127.0.0.1:8000/products/deposit-list/',
        method: 'get',
      })
        .then(res => {
          deposits.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };
    const fetchSaving = function () {
      axios({
        url: 'http://127.0.0.1:8000/products/saving-list/',
        method: 'get',
      })
        .then(res => {
          savings.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    const fetchAnnuity = function () {
      axios({
        url: 'http://127.0.0.1:8000/products/annuity-list/',
        method: 'get',
      })
        .then(res => {
          annuities.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };
    return {
      deposits,
      savings,
      annuities,
      fetchDeposit,
      fetchAnnuity,
      fetchSaving,
    };
  },
  { persist: true },
);
