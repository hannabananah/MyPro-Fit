<template>
  <div>
    <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    <RouterLink :to="{ name: 'deposit' }">예적금 금리 비교</RouterLink>
    <RouterLink :to="{ name: 'exchange' }">환율 계산기</RouterLink>
    <RouterLink :to="{ name: 'map' }">은행 지점찾기</RouterLink>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>
