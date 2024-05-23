<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    <div class="relative flex-grow bg-blue-100">
      <RouterView />
      <ChatbotFloatingBtn class="fixed bottom-4 right-4" />
    </div>
  </div>
</template>

<script setup>
import ChatbotFloatingBtn from '@/components/ChatbotFloatingBtn.vue';
import { RouterView } from 'vue-router';
import Navbar from '@/components/Navbar.vue';
</script>
