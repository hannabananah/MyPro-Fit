<template>
  <footer class="px-4 py-8 bg-gray-800">
    <div
      class="container flex flex-col items-center justify-between mx-auto md:flex-row"
    >
      <div class="mb-4 text-center md:text-left md:mb-0">
        <h3 class="mb-2 text-lg font-semibold text-white">MyPro-Fit</h3>
        <p class="text-sm text-gray-400">
          서울 강남구 테헤란로 212, 멀티캠퍼스 204
        </p>
        <p class="text-sm text-gray-400">myprofit@service.app</p>
      </div>
      <div class="flex justify-center md:justify-start">
        <ul class="flex space-x-6">
          <li>
            <RouterLink
              :to="{ name: 'home' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >Home</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'deposit' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >Compare Deposit Rates</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'exchange' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >Currency Exchange Calculator</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'map' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >Find Bank Branches</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'recommend' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >Product Recommendation Service</RouterLink
            >
          </li>
          <li>
            <RouterLink
              :to="{ name: 'board' }"
              class="text-xs text-gray-400 transition duration-300 md:text-sm hover:text-white"
              >Community</RouterLink
            >
          </li>
        </ul>
      </div>
    </div>
    <div class="pt-4 mt-8 border-t border-gray-700">
      <p class="text-sm text-center text-gray-400">
        &copy; 2024 MyPro-Fit. All rights reserved.
      </p>
    </div>
  </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
