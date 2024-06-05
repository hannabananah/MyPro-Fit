<template>
  <div class="h-[calc(100vh-64px)] py-12">
    <div class="flex flex-col w-3/5 h-full mx-auto gap-y-4">
      <h2 class="text-3xl font-bold">게시물 작성</h2>
      <form
        @submit.prevent="createArticle"
        :style="`background-color: ${randColor}`"
        class="flex flex-col justify-between h-full p-8 overflow-hidden rounded-lg shadow-md"
      >
        <div class="flex flex-col h-full mb-6 gap-y-5">
          <input
            class="w-full px-3 text-lg font-medium text-gray-900 placeholder-gray-400 bg-transparent border-b border-gray-300 outline-none caret-gray-500 hahmlet"
            type="text"
            id="title"
            v-model="title"
            placeholder="열 자 이내의 제목을 작성하세요."
            required
          />
          <textarea
            type="textarea"
            class="h-full p-3 font-light text-gray-900 placeholder-gray-400 bg-transparent border border-gray-300 rounded outline-none resize-none caret-gray-500 hahmlet"
            placeholder="내용을 작성하세요."
            id="content"
            v-model="content"
            required
          ></textarea>
        </div>
        <input
          class="w-1/2 mx-auto btn-active"
          type="submit"
          value="완료하기"
        />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useBoardStore } from '@/stores/board';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';
import axios from 'axios';

const boardStore = useBoardStore();
const userStore = useUserStore();
const router = useRouter();
const title = ref('');
const content = ref('');

const colors = [
  '#fff0f2',
  '#eaffea',
  '#eeffff',
  '#fcf3ff',
  '#fff1eb',
  '#d4f6ff',
  '#ffe4e8',
  '#fffce1',
  '#f9f2ff',
  '#d8fbff',
  '#ebebeb',
];
const randColor = ref(colors[Math.floor(Math.random() * colors.length)]);

const createArticle = function () {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/articles/`,
    data: {
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${userStore.token}`,
      'Content-Type': 'application/json',
    },
  })
    .then(res => {
      const nextId = res.data.id;
      router.push({ name: 'board-detail', params: { id: nextId } });
    })
    .catch(err => {
      console.log(err.response.data);
    });
};
</script>
