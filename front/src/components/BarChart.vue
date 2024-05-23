<template>
  <Bar
    v-if="chartDataReady"
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
    class="max-w-[40rem]"
  />
</template>
<script setup>
import { ref, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import { useUserStore } from '@/stores/user';
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
const chartDataReady = ref(false);
const store = useUserStore();
const chartData = ref({
  labels: [],
  datasets: [
    {
      label: '상품 금리',
      backgroundColor: [],
      data: [],
    },
  ],
});
const chartOptions = {
  responsive: true,
};
onMounted(() => {
  const products = store.joinedProdudcts.deposit_join_products;
  const colors = ['#7BB4E3', '#90B1DB', '#C5D4EB', '#A3CEEF', '#3E77B6'];
  for (const product of products) {
    const randomIndex = Math.floor(Math.random() * colors.length);
    const maxVal = Math.max(
      product.month_6,
      product.month_12,
      product.month_24,
      product.month_36,
    );
    chartData.value.labels.push(product.fin_prdt_nm);
    chartData.value.datasets[0].data.push(maxVal);
    chartData.value.datasets[0].backgroundColor.push(colors[randomIndex]);
    chartDataReady.value = true;
  }

  const productsSaving = store.joinedProdudcts.saving_join_products;
  for (const product of productsSaving) {
    const randomIndex = Math.floor(Math.random() * colors.length);
    const maxVal = Math.max(
      product.month_6,
      product.month_12,
      product.month_24,
      product.month_36,
    );
    chartData.value.labels.push(product.fin_prdt_nm);
    chartData.value.datasets[0].data.push(maxVal);
    chartData.value.datasets[0].backgroundColor.push(colors[randomIndex]);
    chartDataReady.value = true;
  }
});
</script>

<style scoped></style>
