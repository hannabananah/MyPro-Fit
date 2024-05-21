<template>
  <div>
    <RouterLink
      v-if="!userStore.isLogin"
      :to="{ name: 'login' }"
      class="text-orange-600"
      >Login</RouterLink
    >
    <button v-if="userStore.isLogin" @click="logOut">Log out</button>
    <h1 class="text-blue-600">Main</h1>
    <p>
      <strong>{{ userStore.nickname }}</strong
      >님 안녕하세요!
    </p>
    <button v-if="userStore.isLogin" @click="openModal">회원탈퇴</button>
  </div>
  <CustomModal
    v-model="isModalOpen"
    @confirm="handleConfirm"
    @cancel="handleCancel"
    :modalTitle="'회원탈퇴를 하시겠습니까?'"
    :confirmText="'확인'"
    :cancelText="'취소'"
    >확인을 누르면 계정에 대한 모든 정보가 삭제됩니다.</CustomModal
  >
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';
import { useExchangeStore } from '@/stores/exchange';
import CustomModal from '@/components/Modal.vue';
import { onMounted } from 'vue';

const userStore = useUserStore();
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

onMounted(() => {
  if (userStore.isLogin) {
    console.log(userStore.getUserInfo());
    userStore.getUserInfo();
  }
});
</script>
