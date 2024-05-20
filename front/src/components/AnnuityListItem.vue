<template>
  <tr>
    <td>
      {{ props.annuity.dcls_month }} {{ props.annuity.kor_co_nm }}

      {{ props.annuity.prdt_type_nm }} {{ props.annuity.avg_prft_rate }}
      {{ props.annuity.btrm_prft_rate_1 }}
      {{ props.annuity.btrm_prft_rate_2 }}
      {{ props.annuity.btrm_prft_rate_3 }}
    </td>
  </tr>
</template>

<script setup>
const props = defineProps({
  annuity: Object,
});
</script>

<style scoped></style>
