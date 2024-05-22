<template>
  <div>
    <h1>추천페이지</h1>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const store = useUserStore();
onMounted(() => {
  axios({
    url: 'http://127.0.0.1:8000/products/recommend-products/',
    method: 'get',
    headers: {
      Authorization: `Token ${store.token}`,
    },
  }).then(res => {
    console.log(res.data);
  });
});
</script>

<style scoped></style>
