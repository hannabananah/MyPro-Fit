<template>
  <div>
    <h1 class="text-blue-600">Main</h1>
  </div>
</template>

<script setup>
import { useExchangeStore } from '@/stores/exchange';
const store = useExchangeStore();
store.fetchExchangeRate();
</script>
