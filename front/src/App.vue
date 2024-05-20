<template>
  <div>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
    <RouterLink :to="{ name: 'map' }">내주변 은행찾기</RouterLink>
    <RouterLink v-if="!isLogin" :to="{ name: 'profile' }"
      >마이 페이지</RouterLink
    >
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();
const isLogin = userStore.isLogin;
</script>
