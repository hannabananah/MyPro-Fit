<template>
  <div>
    <h1>추천 상품 목록 출력</h1>
    <hr />
    <div v-if="recommendStore.recommendedProducts">
      <div
        v-for="product in recommendStore.recommendedProducts"
        :key="product.code"
      >
        <div v-if="product.id < 0">
          <p>추천 가능한 연금 상품이 없습니다.</p>
        </div>
        <div
          class="hover:cursor-pointer"
          v-if="product.id > 0"
          @click="
            router.push({
              name: 'product-detail',
              params: { type: product.type, code: product.code },
            })
          "
        >
          <p>{{ product.bank }} - {{ product.name }}</p>
          <p v-if="product.type !== 'annuity'">최고 금리 : {{ product.r }}</p>
          <p v-if="product.type == 'annuity'">최고 수익률 : {{ product.r }}</p>
        </div>
        <hr />
      </div>
    </div>

    <div v-if="recommendStore.recommendedProducts.length == 0">
      <p>추천 상품이 없습니다.</p>
      <button>
        <router-link :to="{ name: 'saving-list' }">상품 목록 보기</router-link>
      </button>
    </div>
  </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend';
import { useUserStore } from '@/stores/user';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const recommendStore = useRecommendStore();
const router = useRouter();
</script>
