import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { defineStore } from 'pinia';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

export const useRecommendStore = defineStore(
  'recommend',
  () => {
    const recommendedProducts = ref();
    const userStore = useUserStore();
    const router = useRouter();

    const fetchRecommendedProducts = function () {
      axios({
        url: 'http://127.0.0.1:8000/products/recommend-products/',
        method: 'get',
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then(res => {
          console.log('상품 추천 가져오기 성공');
          recommendedProducts.value = res.data;
          router.push({ name: 'recommend-list' });
        })
        .catch(err => {
          console.log('상품가져오기 실패');
          console.log(err);
        });
    };
    return { recommendedProducts, fetchRecommendedProducts };
  },
  { persist: true },
);
