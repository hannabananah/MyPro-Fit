<template>
  <div class="flex flex-col items-center h-screen pb-10 bg-sky-50">
    <h1 class="py-8 text-2xl font-bold text-center">상품 상세 정보</h1>

    <div class="flex justify-between w-[35%] mb-3">
      <button
        class="border border-solid border-sky-600 px-2 rounded-[8px] bg-slate-50 hover:shadow-inner hover:bg-slate-100"
        @click="$router.go(-1)"
      >
        <undo fillColor="#4682B4"></undo>
      </button>
      <div>
        <button v-show="isLiked" @click="doLike">
          <heart
            fillColor="#FF6666"
            class="inline-block h-[20px] ml-auto"
          ></heart>
        </button>
        <button v-show="!isLiked" @click="doLike">
          <heartOutline
            fillColor="#FF6666"
            class="inline-block h-[20px] ml-auto"
          ></heartOutline></button
        >{{ numberOfLikes }}
      </div>
    </div>
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="container flex flex-col items-center justify-between w-2/5 h-full p-6 py-8 mx-auto bg-slate-50"
    >
      <div class="w-full mx-auto">
        <img
          v-if="route.params.type !== 'annuity' && product"
          :src="getImageUrl(product.kor_co_nm)"
          :alt="product.kor_co_nm"
          class="mb-2 max-w-[110px] block mx-auto"
        />
        <h1
          v-if="product"
          class="flex items-center justify-center mb-3 text-xl font-bold"
        >
          {{ product.fin_prdt_nm }}
        </h1>
        <!-- 예금적금 -->
        <table
          v-if="route.params.type !== 'annuity' && product"
          class="flex border border-slate-300 rounded-[16px] w-full shadow"
        >
          <thead class="w-full divide-y text-start">
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                공시기준월
              </th>
              <td class="pl-3 border-slate-300 text-start">
                {{ product.dcls_month }}
              </td>
            </tr>
            <!-- <tr>
              <th
                class="border-r  border-slate-300 w-[30%] text-start pl-3"
              >
                상품명
              </th>
              <td class=" border-slate-300 w-[70%] text-start pl-3">
                {{ product.fin_prdt_nm }}
              </td>
            </tr> -->
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                기관명
              </th>
              <td class="pl-3 border-slate-300 text-start">
                {{ product.kor_co_nm }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                만기 후 이자율
              </th>
              <td
                class="pl-3 border-slate-300 text-start"
                v-html="
                  product.mtrt_int !== null
                    ? product.mtrt_int.replace(/(.*?-.*?)-/, '$1<br>')
                    : '-'
                "
              ></td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                최고 한도
              </th>
              <td class="pl-3 whitespace-pre-line border-slate-300 text-start">
                {{ product.max_limit !== '' ? product.max_limit : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                가입 조건
              </th>
              <td class="pl-3 border-slate-300 text-start">
                {{ product.join_member !== null ? product.join_member : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                가입 방법
              </th>
              <td class="pl-3 border-slate-300 text-start">
                {{ product.join_way !== null ? product.join_way : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                우대 조건
              </th>
              <td class="w-full pl-3 text-start">
                {{ product.spcl_cnd !== null ? product.spcl_cnd : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                6개월 금리
              </th>
              <td class="w-full pl-3 text-start">
                {{ product.month_6 !== null ? product.month_6 + ' %' : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                12개월 금리
              </th>
              <td class="w-full pl-3 text-start">
                {{ product.month_12 !== null ? product.month_12 + ' %' : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                24개월 금리
              </th>
              <td class="w-full pl-3 text-start">
                {{ product.month_24 !== null ? product.month_24 + ' %' : '-' }}
              </td>
            </tr>
            <tr class="w-full">
              <th class="border-r border-slate-300 w-[30%] text-start pl-3">
                36개월 금리
              </th>
              <td class="w-full pl-3 text-start">
                {{ product.month_36 !== null ? product.month_36 + ' %' : '-' }}
              </td>
            </tr>
          </thead>
        </table>
      </div>

      <!-- 연금 -->

      <div
        v-if="route.params.type === 'annuity' && product"
        class="border border-slate-300 rounded-[16px] w-full shadow"
      >
        <table class="w-full">
          <tr class="w-full">
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              공시기준월
            </th>
            <td class="pl-3 border-b border-slate-300 text-start">
              {{ product.dcls_month }}
            </td>
          </tr>
          <!-- <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              상품명
            </th>
            <td class="pl-3 border-b border-slate-300 text-start">
              {{ product.fin_prdt_nm }}
            </td>
          </tr> -->
          <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              기관명
            </th>
            <td class="pl-3 border-b border-slate-300 text-start">
              {{ product.kor_co_nm }}
            </td>
          </tr>
          <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              상품 유형
            </th>
            <td class="pl-3 border-b border-slate-300 text-start">
              {{ product.prdt_type_nm }}
            </td>
          </tr>
          <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              가입 방법
            </th>
            <td class="pl-3 border-b text-start border-slate-300">
              {{ product.join_way !== null ? product.join_way : '-' }}
            </td>
          </tr>
          <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              평균 수익률
            </th>
            <td class="pl-3 border-b text-start border-slate-300">
              {{
                product.avg_prft_rate !== null
                  ? product.avg_prft_rate + ' %'
                  : '-'
              }}
            </td>
          </tr>
          <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              1년 전 수익률
            </th>
            <td class="pl-3 border-b text-start border-slate-300">
              {{
                product.btrm_prft_rate_1 !== null
                  ? product.btrm_prft_rate_1 + ' %'
                  : '-'
              }}
            </td>
          </tr>
          <tr>
            <th
              class="border-r border-b border-slate-300 w-[30%] text-start pl-3"
            >
              2년 전 수익률
            </th>
            <td class="pl-3 border-b text-start border-slate-300">
              {{
                product.btrm_prft_rate_2 !== null
                  ? product.btrm_prft_rate_2 + ' %'
                  : '-'
              }}
            </td>
          </tr>
          <tr>
            <th class="border-r border-slate-300 w-[30%] text-start pl-3">
              3년 전 수익률
            </th>
            <td class="pl-3 text-start">
              {{
                product.btrm_prft_rate_3 !== null
                  ? product.btrm_prft_rate_3 + ' %'
                  : '-'
              }}
            </td>
          </tr>
        </table>
      </div>
      <div class="w-full text-center">
        <p class="my-4 mt-6 italic text-gray-400" v-if="isJoined">
          이미 가입 중인 상품입니다.
        </p>
        <button v-show="!isJoined" class="mt-6 btn-active" @click="doJoin">
          가입중인 상품 목록에 추가
        </button>
        <button
          v-show="isJoined"
          class="text-white bg-gray-500 border-gray-500 btn-inactive hover:bg-gray-400 hover:border-gray-400"
          @click="doJoin"
        >
          가입중인 상품 목록에서 제거
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import undo from 'vue-material-design-icons/undo.vue';
import heart from 'vue-material-design-icons/heart.vue';
import heartOutline from 'vue-material-design-icons/heartOutline.vue';

const product = ref(null);
const userStore = useUserStore();
const route = useRoute();
const router = useRouter();

onMounted(() => {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/`,
    method: 'GET',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      product.value = res.data;
    })
    .catch(err => {
      router.go(-1);
      alert('로그인 한 사용자만 이용 가능합니다.');
    });
});

// 상품 찜하기
const doLike = function () {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/likes/`,
    method: 'POST',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      location.reload();
    })
    .catch(err => {
      console.log('찜하기 실패');
    });
};

// 상품 찜한 사람 수 계산
const numberOfLikes = computed(() => {
  if (product.value === null) return 0;
  return product.value[`${route.params.type}_like_users`].length;
});

// 현재 유저가 좋아요 했는지 확인
const isLiked = computed(() => {
  if (product.value === null) return false;
  const likeUsers = product.value
    ? product.value[`${route.params.type}_like_users`]
    : [];
  return likeUsers.includes(userStore.userPk);
});

// 현재 유저가 가입 했는지 확인
const isJoined = computed(() => {
  if (product.value === null) return false;
  const joinUsers = product.value
    ? product.value[`${route.params.type}_joined_users`]
    : [];
  return joinUsers.includes(userStore.userPk);
});

// 상품 가입하기
const doJoin = function () {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/joins/`,
    method: 'POST',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      location.reload();
    })
    .catch(err => {
      console.log('가입 실패');
    });
};

// 이미지 동적으로 불러오는 함수
function getImageUrl(name) {
  return new URL(`/src/assets/bankIcons/${name}.png`, import.meta.url).href;
}
</script>
<style scoped></style>
