<template>
  <button
    @click="openChatbot"
    class="flex items-center justify-center w-12 h-12 rounded-full shadow-lg bg-slate-100 aspect-square"
  >
    <img :src="ChatbotIcon" alt="챗봇 프롱이 아이콘" />
  </button>
</template>

<script setup>
import { useRouter } from 'vue-router';
import ChatbotIcon from '@/assets/icons/bot.svg';

const router = useRouter();

const openChatbot = () => {
  router.push({ name: 'chatbot' });
};
</script>
