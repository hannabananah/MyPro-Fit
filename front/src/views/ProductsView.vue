<template>
  <div>
    <p>예적금 금리 비교</p>
    <router-link :to="{ name: 'deposit' }">예금 비교</router-link>
    <router-link :to="{ name: 'saving' }">적금 비교</router-link>
    <router-link :to="{ name: 'annuity' }">연금 비교</router-link>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped></style>
