<template>
  <div>
    <h1>환율계산기 페이지</h1>
  </div>
</template>

<script setup>
import { useExchangeStore } from '@/stores/exchange';
const store = useExchangeStore();
store.fetchExchangeRate();
</script>

<style scoped></style>
