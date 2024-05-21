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
                회원가입 시에 입력받은 아이디와 닉네임에 대한 정보를 확인할 수
                있습니다.
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
              </div>
            </form>
          </div>
          <div
            class="flex flex-col gap-10"
            v-show="activeTab === 'moreInfo'"
            id="moreInfo"
            role="tabpanel"
          >
            <div>
              <h2 class="mb-2 text-lg font-bold text-gray-900">추가 정보</h2>
              <p
                class="text-sm font-light leading-relaxed tracking-wide text-gray-900"
              >
                예적금과 연금 상품을 추천 서비스를 이용하기 위해 필요한 추가적인
                정보입니다.
                <br />
                <small class="tracking-tighter text-gray-600">
                  입력하신 정보는 상품 추천 서비스에만 사용되며 해당 목적 이외의
                  다른 어떠한 용도로도 사용되지 않습니다.
                </small>
              </p>
            </div>
            <form
              class="flex flex-col h-full gap-y-4"
              @submit.prevent="handleSubmit"
            >
              <label for="gender">성별</label>
              <div class="flex space-x-4">
                <label
                  v-for="(option, index) in genderOptions"
                  :key="index"
                  class="flex items-center justify-center w-10 p-2 border cursor-pointer rounded-xl"
                  :class="{
                    [option.bgColor]: userStore.gender === option.value,
                    [option.defaultBgColor]: userStore.gender !== option.value,
                  }"
                  @click="userStore.gender = option.value"
                >
                  <component
                    :is="option.icon"
                    :fillColor="
                      userStore.gender === option.value
                        ? '#fff'
                        : option.defaultIconColor
                    "
                    :size="24"
                  />
                  <input
                    type="radio"
                    :id="option.value"
                    :value="option.value"
                    v-model="userStore.gender"
                    class="hidden form-radio"
                  />
                </label>
              </div>

              <label for="age">나이</label>

              <div class="relative h-14">
                <input
                  type="number"
                  id="age"
                  class="w-20 px-6 -mt-2 text-right text-input box-sizing"
                  v-model="userStore.age"
                />
                <span class="absolute text-sm left-14 top-1">세</span>
              </div>
              <div class="flex flex-col w-4/5">
                <div
                  class="flex justify-between w-full mt-4"
                  v-for="option in checkboxOptions"
                  :key="option.id"
                >
                  <input
                    type="checkbox"
                    :name="option.id"
                    :id="option.id"
                    class="sr-only peer"
                    v-model="userStore[option.model]"
                  />
                  <label
                    :for="option.id"
                    class="flex items-center justify-between w-full font-bold cursor-pointer"
                  >
                    <span>{{ option.label }}</span>
                    <div class="w-6 h-6 mr-2">
                      <CheckboxBlank
                        v-if="!userStore[option.model]"
                        class="text-gray-600"
                      />
                      <Checkbox v-else class="text-gray-900" />
                    </div>
                  </label>
                </div>
              </div>
            </form>
          </div>
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
import Female from 'vue-material-design-icons/GenderFemale.vue';
import Male from 'vue-material-design-icons/GenderMale.vue';
import CheckboxBlank from 'vue-material-design-icons/CheckboxBlankOutline.vue';
import Checkbox from 'vue-material-design-icons/CheckboxOutline.vue';
import axios from 'axios';
import CustomModal from '@/components/Modal.vue';
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();
const activeTab = ref('profile');
const isModalOpen = ref(false);

const genderOptions = [
  {
    value: 'female',
    icon: Female,
    bgColor: 'bg-custom-pink shadow-inner',
    defaultBgColor: 'bg-slate-50',
    defaultIconColor: '#F8ACFF',
  },
  {
    value: 'male',
    icon: Male,
    bgColor: 'bg-custom-blue shadow-inner',
    defaultBgColor: 'bg-slate-50',
    defaultIconColor: '#7DD3FC',
  },
];

const checkboxOptions = [
  {
    id: 'is_pension',
    model: 'is_pension',
    label: '연금 저축 상품을 추천받으시겠습니까?',
  },
  {
    id: 'is_internet',
    model: 'is_internet',
    label: '온라인 가입가능한 상품을 추천받으시겠습니까?',
  },
  {
    id: 'is_BLSR',
    model: 'is_BLSR',
    label: '기초생활수급자이십니까?',
    subLabel:
      '*국민기초생활보장제도를 통해 지원받을 수 있는 상품을 추천해드리기 위한 질문입니다.',
  },
  {
    id: 'is_free',
    model: 'is_free',
    label: '자유납입상품을 추천받으시겠습니까?',
  },
];

onMounted(() => {
  userStore.getUserInfo();
});

watch(
  () => ({
    username: userStore.username,
    nickname: userStore.nickname,
    gender: userStore.gender,
    age: userStore.age,
  }),
  newValues => {
    userStore.username = newValues.username;
    userStore.nickname = newValues.nickname;
    userStore.gender = newValues.gender;
    userStore.age = newValues.age;
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

const updateMoreInfo = () => {
  const genderMap = {
    female: 'F',
    male: 'M',
  };
  const genderValue = genderMap[userStore.gender];

  if (!userStore.token) {
    console.error('Token is not set');
    return;
  }
  axios({
    method: 'patch',
    url: `${userStore.API_URL}/accounts/user/`,
    data: {
      gender: genderValue,
      age: userStore.age,
      is_pension: userStore.is_pension,
      is_internet: userStore.is_internet,
      is_BLSR: userStore.is_BLSR,
      is_free: userStore.is_free,
    },
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(response => {
      console.log('More info 업데이트 성공', response);
    })
    .catch(error => {
      console.error('More info 업데이트 실패', error);
    });
};

const handleConfirm = () => {
  isModalOpen.value = false;
  activeTab.value === 'profile' ? updateProfile() : updateMoreInfo();
};

const handleCancel = () => {
  isModalOpen.value = false;
};
</script>
