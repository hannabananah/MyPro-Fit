<template>
  <div>
    <div
      class="container relative flex flex-col items-center w-4/5 mx-auto overflow-hidden rounded-t-[80px] shadow-md bg-slate-100"
    >
      <div class="relative w-full">
        <img
          class="object-cover w-full overflow-hidden grayscale-[40%] h-56 blur-[3px]"
          src="@/assets/images/chatbot.jpg"
          alt="챗봇 페이지 헤더 이미지"
        />
        <img
          src="@/assets/icons/bot.svg"
          class="absolute w-32 transition-all -translate-x-1/2 -translate-y-1/2 sm:w-52 left-1/2 top-1/2"
        />
      </div>
      <div class="flex flex-col justify-between w-full h-[600px]">
        <div class="p-6 pl-3 overflow-y-auto">
          <div
            v-for="(message, index) in chatHistory"
            :key="index"
            class="relative"
            :class="message.role === 'user' ? 'text-right mb-2' : 'mb-2 pl-12'"
          >
            <img
              v-if="message.role === 'assistant'"
              src="@/assets/icons/bot.svg"
              class="absolute -left-2 -top-1"
            />
            <div class="relative group">
              <div
                class="relative p-2 text-xs text-gray-900 rounded-lg shadow pr-7 sm:text-sm"
                :class="
                  message.role === 'user'
                    ? 'inline-block bg-slate-50'
                    : 'inline-block bg-violet-100'
                "
              >
                {{ message.content }}
                <button
                  class="absolute right-2 bottom-[6px] hover:scale-110 opacity-0 group-hover:opacity-100 transition-opacity"
                  @click="handleClickCopy(message)"
                >
                  <Copy :size="15" fillColor="#666" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <form
          @submit.prevent="sendMessage"
          class="relative h-20 px-6 py-4 pr-12 bg-gradient-to-t from-slate-300"
        >
          <label for="chat" class="absolute top-6 left-9"
            ><Chat fillColor="#6B7280" :size="25"
          /></label>
          <input
            id="chat"
            name="chat"
            v-model="userInput"
            type="text"
            class="truncate text-input"
            placeholder="추천받고 싶은 금융상품에 대해서 검색해보세요."
          />
          <button
            type="submit"
            class="absolute flex items-center justify-center top-6 right-4 hover:scale-110"
          >
            <Send />
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chat from 'vue-material-design-icons/ChatOutline.vue';
import Send from 'vue-material-design-icons/Send.vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import Copy from 'vue-material-design-icons/ContentCopy.vue';
import { useRouter } from 'vue-router';

const userStore = useUserStore();

const chatHistory = ref([]);
const userInput = ref('');

const handleClickCopy = message => {
  navigator.clipboard.writeText(message.content);
};
const router = useRouter();

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
      alert('프롱이와의 통신에 문제가 발생했습니다🫠 다시 시도해주세요.');
      router.push({ name: 'login' });
      console.error('Error:', error);
    });
});

const sendMessage = () => {
  if (userInput.value.trim() === '') {
    alert('메시지를 입력해주세요.');
    return;
  }

  chatHistory.value.push({
    role: 'user',
    content: userInput.value.trim(),
  });

  axios({
    method: 'post',
    url: `${userStore.API_URL}/chatbot/commend/`,
    headers: { Authorization: `Token ${userStore.token}` },
    data: {
      commend: userInput.value.trim(),
    },
  })
    .then(response => {
      chatHistory.value.push({
        role: 'assistant',
        content: response.data.response,
      });
    })
    .catch(error => {
      alert('프롱이와의 통신에 문제가 발생했습니다🫠 다시 시도해주세요.');
      console.error('Error:', error);
    });

  userInput.value = '';
};
</script>

<style scoped>
.group:hover .group-hover\\:opacity-100 {
  opacity: 1;
}
</style>
