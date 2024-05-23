<template>
  <RouterLink :to="{ name: 'home' }">Home</RouterLink>
  <RouterLink :to="{ name: 'deposit' }">예적금 금리 비교</RouterLink>
  <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
  <RouterLink :to="{ name: 'map' }">은행 지점찾기</RouterLink>
  <RouterLink v-if="isLogin" :to="{ name: 'profile' }">마이 페이지</RouterLink>
  <div class="relative w-full">
    <RouterView />
    <ChatbotFloatingBtn class="sticky bottom-0 right-0" />
  </div>
</template>

<script setup>
import ChatbotFloatingBtn from '@/components/ChatbotFloatingBtn.vue';
import { RouterLink, RouterView } from 'vue-router';
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();
const isLogin = userStore.isLogin;
</script>
