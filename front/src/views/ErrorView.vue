<template>
  <div
    class="w-full h-screen bg-error-page bg-[#07203c] flex justify-center items-center flex-col bg-zinc-900 relative"
  >
    <img
      class="animate-glitch"
      src="@/assets/images/error-img.svg"
      alt="404 에러 이미지"
    />
    <h1 class="text-4xl font-black text-center text-gray-400">
      PAGE NOT FOUND
    </h1>
    <RouterLink
      :to="{ name: 'home' }"
      class="text-2xl font-bold text-center text-gray-400 underline"
      >메인페이지로 돌아가기</RouterLink
    >
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
