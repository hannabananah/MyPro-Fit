<template>
  <button @click="$router.go(-1)">목록으로 돌아가기(버튼)</button>
  <!-- 예금적금 -->
  <div v-if="route.params.type !== 'annuity' && product">
    <p>공시기준월: {{ product.dcls_month }}</p>
    <p>상품명: {{ product.fin_prdt_nm }}</p>
    <p>기관명: {{ product.kor_co_nm }}</p>
    <p>
      만기 후 이자율: {{ product.mtrt_int !== null ? product.mtrt_int : '-' }}
    </p>
    <p>최고 한도: {{ product.max_limit !== null ? product.max_limit : '-' }}</p>
    <p>
      가입 조건: {{ product.join_member !== null ? product.join_member : '-' }}
    </p>
    <p>가입 방법: {{ product.join_way !== null ? product.join_way : '-' }}</p>
    <p>우대 조건: {{ product.spcl_cnd !== null ? product.spcl_cnd : '-' }}</p>

    <hr />
    <p>6개월 이자율: {{ product.month_6 !== null ? product.month_6 : '-' }}</p>
    <p>
      12개월 이자율: {{ product.month_12 !== null ? product.month_12 : '-' }}
    </p>
    <p>
      24개월 이자율: {{ product.month_24 !== null ? product.month_24 : '-' }}
    </p>
    <p>
      36개월 이자율: {{ product.month_36 !== null ? product.month_36 : '-' }}
    </p>
  </div>

  <!-- 연금 -->
  <div v-if="route.params.type === 'annuity' && product">
    <p>공시기준월: {{ product.dcls_month }}</p>
    <p>상품명: {{ product.fin_prdt_nm }}</p>
    <p>기관명: {{ product.kor_co_nm }}</p>
    <p>상품 유형: {{ product.prdt_type_nm }}</p>
    <p>가입 방법: {{ product.join_way !== null ? product.join_way : '-' }}</p>
    <hr />
    <p>평균 수익률: {{ product.avg_prft_rate }}</p>
    <p>전년도 수익률: {{ product.btrm_prft_rate_1 }}</p>
    <p>2년전 수익률: {{ product.btrm_prft_rate_2 }}</p>
    <p>3년전 수익률: {{ product.btrm_prft_rate_3 }}</p>
  </div>
  <button>상품 저장</button>
  <button>가입상품 목록에 추가</button>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';

const product = ref(null);

const route = useRoute();
console.log(route.params.type);
console.log(route.params.code);
onMounted(() => {
  axios({
    url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.code}/`,
    method: 'GET',
  })
    .then(res => {
      console.log(res.data);
      product.value = res.data;
      console.log(product.value);
    })
    .catch(err => {
      console.log(err, '에러메세지');
    });
});
</script>
