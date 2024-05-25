<template>
  <section
    class="flex flex-col w-10/12 px-4 mx-auto elect-none max-w-7xl sm:px-6 lg:px-8 gap-y-2"
  >
    <h2 class="mb-4 text-lg font-bold">주요 서비스</h2>
    <div class="flex gap-x-4">
      <div
        v-for="service in services"
        :key="service.name"
        class="flex flex-col items-center justify-center w-24 h-32"
      >
        <router-link :to="{ name: service.name }">
          <img :src="service.iconSrc" :alt="service.label + ' 이미지'" />
          <p class="mt-3 text-sm text-center cursor-pointer">
            {{ service.label }}
          </p>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
const services = [
  {
    iconSrc: 'images/icons/service-section1-icon.svg',
    label: '예금 상품',
    name: 'deposit',
  },
  {
    iconSrc: 'images/icons/service-section2-icon.svg',
    label: '적금 상품',
    name: 'saving',
  },
  {
    iconSrc: 'images/icons/service-section3-icon.svg',
    label: '연금 상품',
    name: 'annuity',
  },
  {
    iconSrc: 'images/icons/service-section4-icon.svg',
    label: '환율 계산',
    name: 'exchange',
  },
  {
    iconSrc: 'images/icons/service-section5-icon.svg',
    label: '근처 은행 찾기',
    name: 'map',
  },
];
</script>
