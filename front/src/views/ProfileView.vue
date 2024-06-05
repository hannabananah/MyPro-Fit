<template>
  <div
    class="flex justify-center w-10/12 h-[calc(100vh-64px)] max-w-screen-lg m-auto"
  >
    <div class="w-full md:flex">
      <ul
        class="flex-col mb-4 space-y-2 text-sm border-r-2 rounded basis-1/4 border-slate-100 space-y md:me-4 md:mb-0"
        data-tabs="tabs"
        role="list"
      >
        <li class="z-30 flex-auto text-center">
          <a
            class="inline-flex items-center w-full px-5 py-2 text-gray-600 rounded cursor-pointer"
            @click="activeTab = 'basicInfo'"
            :class="{ 'bg-slate-100 text-gray-900': activeTab === 'basicInfo' }"
            role="tab"
            :aria-selected="activeTab === 'basicInfo'"
            aria-controls="basicInfo"
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

      <div
        class="flex flex-col items-end justify-between w-full pb-10 text-gray-500 rounded-lg basis-3/4 text-medium min-h-72"
      >
        <div class="w-full">
          <div
            class="flex flex-col gap-10"
            v-show="activeTab === 'basicInfo'"
            id="profile"
            role="tabpanel"
          >
            <div>
              <h2 class="mb-2 text-2xl font-bold text-gray-900">프로필</h2>
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
              <label class="font-bold" for="username">아이디</label>
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

              <label class="font-bold" for="nickname">닉네임</label>

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
            <div id="joinedProduct" v-if="userStore.joinedProdudcts">
              <h1 class="mb-1 font-bold">가입한 상품</h1>
              <div v-if="userStore.joinedProdudcts">
                <div
                  class="hover:cursor-pointer"
                  v-for="deposit in userStore.joinedProdudcts
                    .deposit_join_products"
                  :key="deposit.fin_prdt_cd"
                  @click="
                    router.push({
                      name: 'product-detail',
                      params: { type: 'deposit', code: deposit.fin_prdt_cd },
                    })
                  "
                >
                  <p>{{ deposit.fin_prdt_nm }}</p>
                </div>
                <div
                  class="hover:cursor-pointer"
                  v-for="saving in userStore.joinedProdudcts
                    .saving_join_products"
                  :key="saving.fin_prdt_cd"
                  @click="
                    router.push({
                      name: 'product-detail',
                      params: { type: 'saving', code: saving.fin_prdt_cd },
                    })
                  "
                >
                  <p>{{ saving.fin_prdt_nm }}</p>
                </div>
              </div>
            </div>

            <div v-if="userStore.joinedProdudcts">
              <h1 class="font-bold">가입한 상품 금리</h1>
              <BarChart class="mb-8" />
            </div>
          </div>
          <div
            class="flex flex-col gap-10"
            v-show="activeTab === 'moreInfo'"
            id="moreInfo"
            role="tabpanel"
          >
            <div>
              <h2 class="mb-2 text-2xl font-bold text-gray-900">추가 정보</h2>
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
              <label class="font-bold" for="gender">성별</label>
              <div class="flex space-x-4">
                <label
                  v-for="(option, index) in genderOptions"
                  :key="index"
                  class="flex items-center justify-center w-10 p-2 border cursor-pointer rounded-xl"
                  :class="{
                    [option.bgColor]: userStore.gender === option.mapping,
                    [option.defaultBgColor]:
                      userStore.gender !== option.mapping,
                  }"
                >
                  <component
                    :is="option.icon"
                    :fillColor="
                      userStore.gender === option.mapping
                        ? '#fff'
                        : option.defaultIconColor
                    "
                    :size="24"
                  />
                  <input
                    type="radio"
                    :id="option.value"
                    :value="option.mapping"
                    v-model="userStore.gender"
                    class="hidden form-radio"
                  />
                </label>
              </div>

              <label class="font-bold" for="age">나이</label>

              <div class="relative">
                <input
                  type="number"
                  id="age"
                  :min="0"
                  :max="99"
                  class="w-20 px-6 -mt-[6px] text-right text-input box-sizing"
                  v-model="userStore.age"
                  value="userStore.age"
                />
                <span class="absolute text-sm left-[55px] top-1">세</span>
              </div>

              <label class="font-bold" for="asset">보유 자산</label>

              <div class="relative">
                <input
                  type="text"
                  id="asset"
                  class="w-40 pl-3 pr-10 -mt-[6px] text-right text-input box-sizing"
                  v-model="formattedAsset"
                  @input="handleAssetInput"
                />
                <span class="absolute text-sm left-[130px] top-1">원</span>
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
                    class="flex items-center justify-between w-full h-12 font-bold cursor-pointer"
                  >
                    <p>
                      {{ option.label }}<br /><span
                        class="text-[0.8rem] text-gray-600 font-light"
                        v-if="option.subLabel"
                        >{{ option.subLabel }}</span
                      >
                    </p>
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
        <div class="flex w-1/2 mt-14 md:w-full md:mt-0">
          <button
            v-if="activeTab === 'basicInfo'"
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
    :modalTitle="'계정 정보를 등록 또는 수정하시겠습니까?'"
    :confirmText="'확인'"
    :cancelText="'취소'"
    >확인을 누르면 계정에 대한 정보가 변경됩니다.</CustomModal
  >
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import Profile from 'vue-material-design-icons/AccountCog.vue';
import Wallet from 'vue-material-design-icons/WalletPlus.vue';
import Email from 'vue-material-design-icons/EmailOutline.vue';
import Account from 'vue-material-design-icons/AccountOutline.vue';
import Female from 'vue-material-design-icons/GenderFemale.vue';
import Male from 'vue-material-design-icons/GenderMale.vue';
import CheckboxBlank from 'vue-material-design-icons/CheckboxBlankOutline.vue';
import Checkbox from 'vue-material-design-icons/CheckboxOutline.vue';
import BarChart from '@/components/BarChart.vue';
import axios from 'axios';
import CustomModal from '@/components/Modal.vue';
import { useUserStore } from '@/stores/user';
import {
  formatNumberWithCommas,
  parseNumberWithCommas,
} from '@/utils/formatNumber';
import { useRoute, useRouter } from 'vue-router';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js';
ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
);
const route = useRoute();
const router = useRouter();
const userStore = useUserStore();

const activeTab = ref(route.params.tab);
const isModalOpen = ref(false);

const genderOptions = [
  {
    value: 'female',
    mapping: 'F',
    icon: Female,
    bgColor: 'bg-custom-pink shadow-inner',
    defaultBgColor: 'bg-slate-50',
    defaultIconColor: '#F8ACFF',
  },
  {
    value: 'male',
    mapping: 'M',
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
  userStore.getJoinedProducts();
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
  if (!userStore.token) {
    console.error('Token is not set');
    return;
  }
  axios({
    method: 'patch',
    url: `${userStore.API_URL}/accounts/user/`,
    data: {
      gender: userStore.gender,
      age: userStore.age,
      asset: parseNumberWithCommas(userStore.asset),
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
      console.log('More info 업데이트 성공');
    })
    .catch(error => {
      console.error('More info 업데이트 실패', error);
    });
};

const handleConfirm = () => {
  isModalOpen.value = false;
  activeTab.value === 'basicInfo' ? updateProfile() : updateMoreInfo();
};

const handleCancel = () => {
  isModalOpen.value = false;
};

const formattedAsset = computed({
  get() {
    return formatNumberWithCommas(userStore.asset);
  },
  set(value) {
    userStore.asset = parseNumberWithCommas(value);
  },
});

const handleAssetInput = event => {
  const value = event.target.value;
  userStore.asset = parseNumberWithCommas(value);
  event.target.value = formatNumberWithCommas(userStore.asset);
};
</script>
