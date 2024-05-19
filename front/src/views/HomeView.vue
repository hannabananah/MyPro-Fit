<template>
  <div>
    <RouterLink v-if="!isLogin" :to="{ name: 'login' }" class="text-orange-600">Login</RouterLink>
    <button v-if="isLogin" @click="logOut">Log out</button>
    <h1 class="text-blue-600">Main</h1>
    <button v-if="isLogin" @click="deleteAccount">회원탈퇴</button>
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

const deleteAccount = () => {
  userStore.deleteAccount();
};

const store = useExchangeStore();
store.fetchExchangeRate();
</script>
