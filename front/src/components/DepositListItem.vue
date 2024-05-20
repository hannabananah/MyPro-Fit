<template>
  <div>
    <p>
      {{ props.deposit.dcls_month }} {{ props.deposit.kor_co_nm }}
      {{ props.deposit.fin_prdt_nm }} {{ props.deposit.month_6 }}
      {{ props.deposit.month_12 }}
      {{ props.deposit.month_24 }}
      {{ props.deposit.month_36 }}
    </p>
  </div>
</template>

<script setup>
const props = defineProps({
  deposit: Object,
});
</script>
