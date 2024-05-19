<template>
  <div>
    <RouterLink v-if="!isLogin" :to="{ name: 'login' }" class="text-orange-600">Login</RouterLink>
    <button v-if="isLogin" @click="logOut">Log out</button>
    <h1 class="text-blue-600">Main</h1>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user';
import { useExchangeStore } from '@/stores/exchange';
const userStore = useUserStore();
const isLogin = userStore.isLogin;

const logOut = () => {
  userStore.logOut();
};

const store = useExchangeStore();
store.fetchExchangeRate();
</script>
