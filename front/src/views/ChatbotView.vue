<template>
  <div class="flex flex-col justify-between min-h-screen pt-12 bg-gray-100">
    <div class="p-6 bg-red-200">
      <div
        v-for="(message, index) in chatHistory"
        :key="index"
        :class="message.role === 'user' ? 'text-right mb-2' : 'mb-2'"
      >
        <div
          :class="
            message.role === 'user'
              ? 'inline-block bg-blue-500 text-white rounded-lg p-2'
              : message.role === 'assistant'
                ? 'inline-block bg-gray-300 text-gray-800 rounded-lg p-2'
                : 'inline-block bg-gray-300 text-gray-800 rounded-lg p-2'
          "
        >
          {{ message.content }}
        </div>
      </div>
    </div>

    <form @submit.prevent="sendMessage" class="relative px-10 py-6 bg-gray-200">
      <label for="chat" class="absolute top-8 left-12"
        ><Chat fillColor="#6B7280" :size="25"
      /></label>
      <input
        id="chat"
        name="chat"
        v-model="userInput"
        type="text"
        class="text-input"
        placeholder="메시지를 입력하세요."
      />
      <button
        type="submit"
        class="absolute flex items-center justify-center top-8 right-2 hover:scale-110"
      >
        <Send />
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chat from 'vue-material-design-icons/ChatOutline.vue';
import Send from 'vue-material-design-icons/Send.vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
const userStore = useUserStore();

const chatHistory = ref([]);
const userInput = ref('');

onMounted(() => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/chatbot/`,
    headers: { Authorization: `Token ${userStore.token}` },
  })
    .then(response => {
      chatHistory.value.push({
        role: 'assistant',
        content:
          '안녕하세요. 최첨단 AI 챗봇 프롱이입니다. 무엇을 도와드릴까요?',
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

const sendMessage = () => {
  chatHistory.value.push({
    role: 'user',
    content: userInput.value,
  });

  axios({
    method: 'post',
    url: `${userStore.API_URL}/chatbot/commend/`,
    headers: { Authorization: `Token ${userStore.token}` },
    data: {
      commend: userInput.value,
    },
  })
    .then(response => {
      chatHistory.value.push({
        role: 'assistant',
        content: response.data.response,
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });

  userInput.value = '';
};
</script>
