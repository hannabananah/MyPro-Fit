<template>
  <div>
    <p>
      {{ props.saving.dcls_month }}
      {{ props.saving.kor_co_nm }}
      {{ props.saving.fin_prdt_nm }}
      {{ props.saving.month_6 }}
      {{ props.saving.month_12 }}
      {{ props.saving.month_24 }}
      {{ props.saving.month_36 }}
    </p>
  </div>
</template>

<script setup>
const props = defineProps({
  saving: Object,
});
</script>
