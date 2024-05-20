<template>
  <div
    :class="{
      'flex flex-col w-full h-screen lg:flex-row': true,
      'bg-sky-100 items-center justify-center p-4': !isLg,
    }"
  >
    <div
      :class="{
        'flex flex-col items-center justify-center w-full gap-10 py-10 bg-sky-100 lg:w-3/5': true,
        hidden: !isLg,
      }"
    >
      <img :src="LogoSvg" alt="Logo Icon" class="w-1/5 h-auto lg:w-64" />
      <img :src="LoginSvg" alt="Login Icon" class="w-1/5 h-auto lg:w-[30rem]" />
    </div>
    <div
      class="flex flex-col items-center justify-center w-full h-screen lg:w-2/5 lg:items-start lg:justify-center lg:px-16"
    >
      <h2 class="mb-6 text-2xl font-bold text-center lg:text-left">
        Log in to your Account
      </h2>
      <form
        @submit.prevent="logIn"
        class="flex flex-col w-full max-w-md gap-12"
      >
        <div class="flex flex-col gap-2 lg:gap-4">
          <div class="relative h-14">
            <Email
              class="absolute top-2.5 left-3"
              fillColor="#6B7280"
              :size="20"
            />
            <input
              type="text"
              v-model.trim="email"
              placeholder="이메일 형식의 아이디를 입력해주세요."
              class="text-input"
            />
            <div class="h-4">
              <p
                class="pt-[1.5px] pl-2 text-xs text-red-500"
                v-if="store.shouldShowError('email')"
              >
                {{ store.errorFields.email }}
              </p>
            </div>
          </div>
          <div class="relative h-14">
            <Lock
              class="absolute top-2.5 left-3"
              fillColor="#6B7280"
              :size="20"
            />
            <input
              :type="passwordVisible ? 'text' : 'password'"
              v-model.trim="password"
              placeholder="비밀번호를 입력해주세요."
              maxLength="20"
              class="text-input"
            />
            <EyeOff
              v-if="!passwordVisible"
              @click="passwordVisible = true"
              class="absolute top-2.5 right-3.5 cursor-pointer"
              fillColor="#6B7280"
              :size="20"
            />
            <Eye
              v-else
              @click="passwordVisible = false"
              class="absolute top-2.5 right-3.5 cursor-pointer"
              fillColor="#111827"
              :size="20"
            />
            <div class="h-4">
              <p
                class="pt-[1.5px] pl-2 text-xs text-red-500"
                v-if="store.shouldShowError('password')"
              >
                {{ store.errorFields.password }}
              </p>
            </div>
          </div>
          <button
            @click="openModal"
            class="text-xs underline text-sky-700 text-end"
          >
            비밀번호를 잊어버리셨습니까?
          </button>
        </div>
        <div class="flex flex-col gap-2">
          <input type="submit" class="btn-active" value="Log in" />
          <div class="h-4">
            <p
              v-if="store.shouldShowError('general')"
              class="text-xs text-red-500"
            >
              {{ store.errorFields.general }}
            </p>
          </div>
        </div>
      </form>
      <div class="flex justify-center w-full gap-2 mt-4 text-xs">
        <p class="text-gary-900">아직 회원이 아니신가요?</p>
        <RouterLink :to="{ name: 'signup' }" class="font-bold text-sky-700"
          >회원가입하기</RouterLink
        >
      </div>
    </div>
    <div
      :class="{
        hidden: isLg,
        'flex items-center justify-center w-full h-20 bg-sky-100': !isLg,
      }"
    >
      <img :src="LogoSvg" alt="Logo Icon" />
    </div>
  </div>
  <CustomModal
    v-model="isModalOpen"
    @confirm="handleConfirm"
    @cancel="handleCancel"
    :modalTitle="'비밀번호 초기화를 하시겠습니까?'"
    :confirmText="'확인'"
    :cancelText="'취소'"
  >
    <div>
      <p>
        이메일로 비밀번호 초기화 링크를 보내드립니다. <br />이메일을
        확인해주세요.
      </p>
      <input
        v-model="pwdEmail"
        type="email"
        placeholder="이메일을 입력하세요"
        class="px-4 mt-2 text-input"
        maxlength="50"
      /></div
  ></CustomModal>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useUserStore } from '@/stores/user';
import LoginSvg from '@/assets/images/login.svg';
import LogoSvg from '@/assets/images/logo.svg';
import Email from 'vue-material-design-icons/EmailOutline.vue';
import Lock from 'vue-material-design-icons/LockOutline.vue';
import Eye from 'vue-material-design-icons/EyeOutline.vue';
import EyeOff from 'vue-material-design-icons/EyeOffOutline.vue';
import axios from 'axios';
import CustomModal from '@/components/Modal.vue';

const email = ref(null);
const password = ref(null);
const passwordVisible = ref(false);
const isLg = ref(window.innerWidth >= 1024);
const store = useUserStore();
const isModalOpen = ref(false);

const updateWidth = () => {
  isLg.value = window.innerWidth >= 1024;
};

onMounted(() => {
  store.errorMessage = null;
  store.errorFields = {};
  window.addEventListener('resize', updateWidth);
  updateWidth();
});

onUnmounted(() => {
  window.removeEventListener('resize', updateWidth);
});

const logIn = () => {
  const payload = {
    email: email.value,
    password: password.value,
  };
  store.logIn(payload);
};

const pwdEmail = ref('');

const resetPwd = () => {
  axios({
    method: 'post',
    url: `${store.API_URL}/accounts/password/reset/`,
    data: {
      email: pwdEmail.value,
    },
  })
    .then(response => {
      console.log('이메일 발송 성공', response);
    })
    .catch(error => {
      console.log('이메일 발송 실패', error);
    });
};

const openModal = () => {
  isModalOpen.value = true;
};

const handleConfirm = () => {
  resetPwd();
  isModalOpen.value = false;
};

const handleCancel = () => {
  isModalOpen.value = false;
};
</script>
