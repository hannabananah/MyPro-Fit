<template>
  <div class="py-12">
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="flex flex-col items-center w-3/5 mx-auto"
    >
      <h1 class="text-2xl pt-6 font-bold">추천 상품 목록 출력</h1>
      <p class="text-sm text-gray-600">
        {{ userStore.nickname }}님의 자산 상태와 가입 상품을 바탕으로 추천도가
        높은 상품을 추천해드립니다.
      </p>
      <div
        v-if="recommendStore.recommendedProducts"
        class="w-full grid grid-cols-3 gap-5 px-12 pt-8"
      >
        <div
          v-for="(product, index) in recommendStore.recommendedProducts"
          :key="product.code"
          class="border border-slate-200 bg-slate-50 rounded-[8px] shadow p-4 text-sm pb-12 relative"
        >
          <div
            v-if="product.id < 0"
            class="border border-slate-200 bg-slate-50 rounded-[8px] shadow p-4 text-sm pb-12 relative"
          >
            <p>{{ index + 1 }}</p>
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
            <p class="text-lg font-bold text-gray-600">{{ index + 1 }}</p>
            <p>{{ product.bank }} - {{ product.name }}</p>
            <p
              class="text-lg text-end font-bold text-sky-600 absolute bottom-3 right-4"
              v-if="product.type !== 'annuity'"
            >
              최고 {{ product.r }}%
            </p>
            <p
              v-if="product.type == 'annuity'"
              class="text-lg text-end font-bold text-sky-600 absolute bottom-3 right-4"
            >
              최고 {{ product.r }}
            </p>
          </div>
        </div>
      </div>

      <div v-if="recommendStore.recommendedProducts.length == 0">
        <p>추천 상품이 없습니다.</p>
        <button
          class="btn-active w-[50%] my-6"
          @click="router.push({ name: 'login' })"
        >
          <router-link :to="{ name: 'saving-list' }"
            >상품 목록 보기</router-link
          >
        </button>
      </div>
      <img class="mb-4 mt-6" src="@/assets/images/logo.svg" alt="" />
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
