<template>
  <div>
    <RouterLink v-if="!isLogin" :to="{ name: 'login' }" class="text-orange-600"
      >Login</RouterLink
    >
    <button v-if="isLogin" @click="logOut">Log out</button>
    <h1 class="text-blue-600">Main</h1>
    <button v-if="isLogin" @click="openModal">회원탈퇴</button>
  </div>
  <CustomModal
    v-model="isModalOpen"
    @confirm="handleConfirm"
    @cancel="handleCancel"
    :modalTitle="'회원탈퇴를 하시겠습니까'"
    :modalContent="'확인을 누르면 계정에 대한 모든 정보가 삭제됩니다.'"
    :confirmText="'확인'"
    :cancelText="'취소'"
  ></CustomModal>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';
import { useExchangeStore } from '@/stores/exchange';
import CustomModal from '@/components/Modal.vue';

const userStore = useUserStore();
const isLogin = userStore.isLogin;

const isModalOpen = ref(false);

const logOut = () => {
  userStore.logOut();
};

const deleteAccount = () => {
  userStore.deleteAccount();
};

const openModal = () => {
  isModalOpen.value = true;
};

const handleConfirm = () => {
  deleteAccount();
  isModalOpen.value = false;
};

const handleCancel = () => {
  isModalOpen.value = false;
};

const store = useExchangeStore();
store.fetchExchangeRate();
</script>
