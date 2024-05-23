<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    <div class="flex-grow">
      <div class="relative px-4 py-8 mx-auto max-w-7xl sm:px-6 lg:px-8">
        <RouterView />
        <ChatbotFloatingBtn class="fixed bottom-4 right-4" />
      </div>
    </div>
  </div>
</template>

<script setup>
import ChatbotFloatingBtn from '@/components/ChatbotFloatingBtn.vue';
import { RouterView } from 'vue-router';
import Navbar from '@/components/Navbar.vue';
</script>
