<template>
  <section
    class="flex flex-col w-10/12 px-4 mx-auto my-16 text-center select-none max-w-7xl sm:px-6 lg:px-8 gap-y-2"
  >
    <p>내게 Fit한 금융상품, 비교하기 힘드시죠?</p>
    <h2 class="text-2xl font-bold hahmlet">
      MyPro-Fit은 쉽고 정확하게 비교합니다.
    </h2>
    <div class="flex justify-between gap-5 mt-5">
      <div
        v-for="item in items"
        :key="item.index"
        class="flex flex-col items-center text-center gap-y-3"
      >
        <img
          :src="getIconPath(item.index)"
          :alt="'인트로 섹션 이미지' + item.index"
          class="w-[130px]"
        />
        <h4 class="font-medium">{{ item.title }}</h4>
        <p class="px-4 font-thin break-words text-balance">
          {{ item.description }}
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
const items = [
  {
    index: 1,
    title: '국내 최대 금융상품 데이터',
    description:
      '금융 상품 데이터뿐만 아니라, 환율 계산, 나에게 가까운 은행지점 찾기까지 다양한 서비스를 모두 챙겼습니다.',
  },
  {
    index: 2,
    title: '나만을 위한 금융매칭',
    description:
      '간단한 테스트를 통해서 빅데이터에 기반한 알고리즘을 매칭되는 나에게 딱맞는 금융상품을 추천해줍니다.',
  },
  {
    index: 3,
    title: '광고나 홍보 없음',
    description:
      'MyPro-Fit의 추천에는 광고도, 홍보도 없습니다. 오직 객관적인 데이터만을 활용합니다.',
  },
];

const getIconPath = index => {
  return `public/images/icons/desc-section${index}-icon.svg`;
};
</script>
