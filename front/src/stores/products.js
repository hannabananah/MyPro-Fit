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
      if (!deposits.value || deposits.value.length === 0) {
        return null; // deposits.value가 비어있을 때 null 반환
      }

      return deposits.value
        .filter(
          deposit =>
            deposit.deposit_like_users && deposit.deposit_like_users.length > 0,
        ) // deposit_like_users가 존재하고 길이가 0보다 큰 요소만 필터링
        .reduce(
          (max, deposit) =>
            deposit.deposit_like_users.length > max.deposit_like_users.length
              ? deposit
              : max,
          { deposit_like_users: [] }, // 초기값 설정
        );
    });

    const bestSaving = computed(() => {
      if (!savings.value || savings.value.length === 0) {
        return null; // savings.value가 비어있을 때 null 반환
      }

      return savings.value
        .filter(
          saving =>
            saving.saving_like_users && saving.saving_like_users.length > 0,
        ) // saving_like_users가 존재하고 길이가 0보다 큰 요소만 필터링
        .reduce(
          (max, saving) =>
            saving.saving_like_users.length > max.saving_like_users.length
              ? saving
              : max,
          { saving_like_users: [] }, // 초기값 설정
        );
    });

    const bestAnnuity = computed(() => {
      if (!annuities.value || annuities.value.length === 0) {
        return null; // annuities.value가 비어있을 때 null 반환
      }

      return annuities.value
        .filter(
          annuity =>
            annuity.annuity_like_users && annuity.annuity_like_users.length > 0,
        ) // annuity_like_users가 존재하고 길이가 0보다 큰 요소만 필터링
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
