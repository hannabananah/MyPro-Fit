<template>
  <div
    class="flex flex-col w-10/12 px-4 py-10 mx-auto elect-none max-w-7xl sm:px-6 lg:px-8 gap-y-2"
  >
    <h2 class="mb-4 text-lg font-bold">당신을 위한 BEST PICK!</h2>
    <div
      class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
    >
      <div
        v-if="productStore.bestDeposit"
        v-for="product in products"
        :key="product.type"
        class="border rounded cursor-pointer border-sky-100"
        style="width: 250px; height: 330px"
        @click="goToProductDetail(product.type)"
      >
        <img
          :src="product.iconSrc"
          :alt="product.label + ' 이미지'"
          class="object-cover w-full h-30"
        />
        <div class="p-3">
          <p class="text-lg font-bold text-gray-900 truncate">
            {{ product.label }}
          </p>
          <p class="mt-2 text-xs text-gray-500 truncate text-wrap">
            {{ product.detail }}
          </p>
          <h5 class="mt-3 font-semibold truncate text-md">
            {{ product.firm }}
          </h5>
          <p class="text-sm font-extralight line-clamp-2">
            {{ product.title }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { useProductStore } from '@/stores/products';
import { onMounted } from 'vue';

const router = useRouter();
const productStore = useProductStore();

const products = [
  {
    type: 'deposit',
    label: '예금',
    title: productStore.bestDeposit ? productStore.bestDeposit.fin_prdt_nm : '',
    firm: productStore.bestDeposit ? productStore.bestDeposit.kor_co_nm : '',
    detail: '안전하게 키우는 든든한 자산 ',
    iconSrc: 'public/images/icons/recom-section1-img.svg',
  },
  {
    type: 'saving',
    label: '적금',
    title: productStore.bestSaving ? productStore.bestSaving.fin_prdt_nm : '',
    firm: productStore.bestSaving ? productStore.bestSaving.kor_co_nm : '',
    detail: '차곡차곡 쌓는 나의 미래 자산',
    iconSrc: 'public/images/icons/recom-section2-img.svg',
  },
  {
    type: 'annuity',
    label: '연금',
    title: productStore.bestAnnuity ? productStore.bestAnnuity.fin_prdt_nm : '',
    firm: productStore.bestAnnuity ? productStore.bestAnnuity.kor_co_nm : '',
    detail: '안정적으로 준비하는 행복한 노후',
    iconSrc: 'public/images/icons/recom-section3-img.svg',
  },
  {
    type: 'pring',
    label: 'AI 상담',
    title: '최첨단 AI 프링이와 대화하며 더 많은 상품을 추천받아보세요',
    firm: '프링이',
    detail: '...더 많은 상품 추천받기',
    iconSrc: 'public/images/icons/recom-section4-img.svg',
  },
];

const goToProductDetail = type => {
  if (type === 'pring') {
    router.push({ name: 'chatbot' });
  } else {
    const product =
      productStore[`best${type.charAt(0).toUpperCase() + type.slice(1)}`];
    if (product) {
      router.push({
        name: 'product-detail',
        params: {
          type,
          code: product.fin_prdt_cd,
        },
      });
    }
  }
};

onMounted(() => {
  productStore.fetchDeposit();
  productStore.fetchAnnuity();
  productStore.fetchSaving();
});
</script>
