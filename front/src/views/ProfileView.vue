<template>
  <div
    class="flex justify-center w-10/12 h-screen max-w-screen-lg py-12 m-auto"
  >
    <div class="w-full md:flex">
      <!-- 사이드 메뉴 -->
      <ul
        class="flex-col mb-4 space-y-2 text-sm border-r-2 rounded basis-1/4 border-slate-100 space-y md:me-4 md:mb-0"
        data-tabs="tabs"
        role="list"
      >
        <li class="z-30 flex-auto text-center">
          <a
            class="inline-flex items-center w-full px-5 py-2 text-gray-600 rounded cursor-pointer"
            @click="activeTab = 'profile'"
            :class="{ 'bg-slate-100 text-gray-900': activeTab === 'profile' }"
            role="tab"
            :aria-selected="activeTab === 'profile'"
            aria-controls="profile"
          >
            <Profile fillColor="#6B7280" :size="20" class="mr-3" />
            <span class="mt-1 tracking-wider">프로필</span>
          </a>
        </li>
        <li>
          <a
            class="inline-flex items-center w-full px-5 py-2 text-gray-600 rounded cursor-pointer"
            @click="activeTab = 'moreInfo'"
            :class="{ 'bg-slate-100 text-gray-900': activeTab === 'moreInfo' }"
            data-tab-target="updateProfile"
            role="tab"
            :aria-selected="activeTab === 'moreInfo'"
            aria-controls="moreInfo"
          >
            <Wallet fillColor="#6B7280" :size="20" class="mr-3" />
            <span class="tracking-wider">추가 정보</span>
          </a>
        </li>
      </ul>
      <!-- 패널 -->
      <div
        class="flex flex-col items-end justify-between w-full text-gray-500 rounded-lg basis-3/4 text-medium min-h-72"
      >
        <div class="w-full">
          <div
            class="flex flex-col gap-10"
            v-show="activeTab === 'profile'"
            id="profile"
            role="tabpanel"
          >
            <div>
              <h2 class="mb-2 text-lg font-bold text-gray-900">프로필</h2>
              <small
                class="font-light leading-relaxed tracking-wide text-gray-900"
              >
                회원가입 시에 입력한 정보를 확인하거나 수정할 수 있습니다.
              </small>
            </div>
            <form
              class="flex flex-col h-full gap-y-4"
              @submit.prevent="handleSubmit"
            >
              <label for="username">아이디</label>
              <div class="relative h-14">
                <Email
                  class="absolute top-1 left-3"
                  fillColor="#6B7280"
                  :size="20"
                />
                <input
                  type="text"
                  id="username"
                  v-model="userStore.username"
                  class="-mt-2 text-gray-500 bg-gray-100 border-gray-300 md:w-2/3 text-input"
                  disabled
                />
                <!-- <p
                class="pt-[1.5px] pl-2 text-xs text-red-500"
                v-if="store.shouldShowError('username')"
              >
                {{ store.errorFields.username }}
              </p> -->
              </div>

              <label for="nickname">닉네임</label>

              <div class="relative h-14">
                <Account
                  class="absolute top-1 left-3"
                  fillColor="#6B7280"
                  :size="20"
                />
                <input
                  type="text"
                  id="nickname"
                  v-model="userStore.nickname"
                  class="-mt-2 md:w-2/3 text-input"
                />
                <!-- <p
                  class="pt-[1.5px] pl-2 text-xs text-red-500"
                  v-if="store.shouldShowError('nickname')"
                >
                  {{ store.errorFields.nickname }}
                </p> -->
              </div>
            </form>
          </div>
          <div
            class="flex flex-col gap-4"
            v-show="activeTab === 'moreInfo'"
            id="moreInfo"
            role="tabpanel"
          >
            <div>
              <h2 class="mb-2 text-lg font-bold text-gray-900">추가 정보</h2>
              <small
                class="font-light leading-relaxed tracking-wide text-gray-900"
              >
                내게 가장 적합한 금융 상품을 추천받기 위한 추가 정보를
                입력해주세요.
              </small>
            </div>

            <div class=""></div>
          </div>
          <!--      <h2 class="mb-2 text-lg font-bold text-gray-900">Profile Tab</h2>
          <p class="mb-2">
            This is some placeholder content the Profile tab's associated
            content, clicking another tab will toggle the visibility of this one
            for the next.
          </p> -->
        </div>
        <div class="flex w-1/2 md:w-full">
          <button
            v-if="activeTab === 'profile'"
            class="btn-active"
            @click="openModal"
          >
            수정하기
          </button>
          <button
            v-if="activeTab === 'moreInfo'"
            class="btn-active"
            @click="openModal"
          >
            등록하기
          </button>
        </div>
      </div>
    </div>
  </div>
  <CustomModal
    v-model="isModalOpen"
    @confirm="handleConfirm"
    @cancel="handleCancel"
    :modalTitle="'계정 정보를 수정하시겠습니까?'"
    :confirmText="'확인'"
    :cancelText="'취소'"
    >확인을 누르면 계정에 대한 정보가 변경됩니다.</CustomModal
  >
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import Profile from 'vue-material-design-icons/AccountCog.vue';
import Wallet from 'vue-material-design-icons/WalletPlus.vue';
import Email from 'vue-material-design-icons/EmailOutline.vue';
import Account from 'vue-material-design-icons/AccountOutline.vue';
import axios from 'axios';
import CustomModal from '@/components/Modal.vue';
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();
const activeTab = ref('profile');
const isModalOpen = ref(false);

onMounted(() => {
  userStore.getUserInfo();
});

watch(
  () => ({
    username: userStore.username,
    nickname: userStore.nickname,
  }),
  newValues => {
    userStore.username = newValues.username;
    userStore.nickname = newValues.nickname;
  },
  { immediate: true },
);

const openModal = () => {
  isModalOpen.value = true;
};

const updateProfile = () => {
  if (!userStore.token) {
    console.error('Token is not set');
    return;
  }
  axios({
    method: 'patch',
    url: `${userStore.API_URL}/accounts/user/`,
    data: {
      username: userStore.username,
      nickname: userStore.nickname,
    },
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(response => {
      console.log('Profile updated', response);
    })
    .catch(error => {
      console.error('Profile update failed', error);
    });
};

const handleConfirm = () => {
  isModalOpen.value = false;
  updateProfile();
};

const handleCancel = () => {
  isModalOpen.value = false;
};
</script>
