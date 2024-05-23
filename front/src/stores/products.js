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

    const bestDeposit = computed(() => {
      return deposits.value
        .filter(deposit => deposit.deposit_like_users.length > 0) // 조건에 맞는 요소 필터링
        .reduce(
          (max, deposit) =>
            deposit.deposit_like_users.length > max.deposit_like_users.length
              ? deposit
              : max,
          { deposit_like_users: [] }, // 초기값 설정
        );
    });

    const bestSaving = computed(() => {
      return savings.value
        .filter(saving => saving.saving_like_users.length > 0) // 조건에 맞는 요소 필터링
        .reduce(
          (max, saving) =>
            saving.saving_like_users.length > max.saving_like_users.length
              ? saving
              : max,
          { saving_like_users: [] }, // 초기값 설정
        );
    });

    const bestAnnuity = computed(() => {
      return annuities.value
        .filter(annuity => annuity.annuity_like_users.length > 0) // 조건에 맞는 요소 필터링
        .reduce(
          (max, annuity) =>
            annuity.annuity_like_users.length > max.annuity_like_users.length
              ? annuity
              : max,
          { annuity_like_users: [] }, // 초기값 설정
        );
    });

    return {
      deposits,
      savings,
      annuities,
      fetchDeposit,
      fetchAnnuity,
      fetchSaving,
      bestDeposit,
      bestAnnuity,
      bestSaving,
    };
  },
  { persist: true },
);
