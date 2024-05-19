<template>
  <div>
    <RouterLink v-if="!isLogin" :to="{ name: 'login' }" class="text-orange-600">Login</RouterLink>
    <button v-if="isLogin" @click="logOut">Log out</button>
    <h1 class="text-blue-600">Main</h1>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore();
const isLogin = store.isLogin;

const logOut = () => {
  store.logOut();
};
</script>
