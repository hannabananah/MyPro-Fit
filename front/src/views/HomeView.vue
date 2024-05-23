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

    <!-- 예금 베스트 상품 -->
    <div
      v-if="productstore.bestDeposit"
      @click="
        router.push({
          name: 'product-detail',
          params: {
            type: 'deposit',
            code: productstore.bestDeposit.fin_prdt_cd,
          },
        })
      "
    >
      {{ productstore.bestDeposit.fin_prdt_nm }}
    </div>
    <!-- 적금 베스트 상품 -->
    <div
      v-if="productstore.bestSaving"
      @click="
        router.push({
          name: 'product-detail',
          params: {
            type: 'saving',
            code: productstore.bestSaving.fin_prdt_cd,
          },
        })
      "
    >
      {{ productstore.bestSaving.fin_prdt_nm }}
    </div>
    <!-- 연금 베스트 상품 -->
    <div
      v-if="productstore.bestAnnuity"
      @click="
        router.push({
          name: 'product-detail',
          params: {
            type: 'annuity',
            code: productstore.bestAnnuity.fin_prdt_cd,
          },
        })
      "
    >
      {{ productstore.bestAnnuity.fin_prdt_nm }}
    </div>
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
import { useProductStore } from '@/stores/products';
import CustomModal from '@/components/Modal.vue';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore();
const productstore = useProductStore();
const router = useRouter();
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
    userStore.getUserInfo();
  }
  productstore.fetchDeposit();
  productstore.fetchAnnuity();
  productstore.fetchSaving();
});
</script>
