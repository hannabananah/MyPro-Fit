<template>
  <div class="h-screen py-12">
    <div class="flex flex-col w-3/5 h-full mx-auto gap-y-4">
      <h2 class="text-3xl font-bold">게시물 수정</h2>
      <form
        @submit.prevent="edit"
        :style="`background-color: ${randColor}`"
        class="flex flex-col justify-between h-full p-8 overflow-hidden rounded-lg shadow-md"
      >
        <div class="flex flex-col h-full mb-6 gap-y-5">
          <input
            class="w-full px-3 text-lg font-medium text-gray-900 placeholder-gray-400 bg-transparent border-b border-gray-300 outline-none caret-gray-500 hahmlet"
            type="text"
            id="title"
            v-model="title"
            required
          />
          <textarea
            type="textarea"
            class="h-full p-3 font-light text-gray-900 placeholder-gray-400 bg-transparent border border-gray-300 rounded outline-none resize-none caret-gray-500 hahmlet"
            id="content"
            v-model="content"
            required
          ></textarea>
        </div>
        <input
          class="w-1/2 mx-auto btn-active"
          type="submit"
          value="수정하기"
        />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useBoardStore } from '@/stores/board';
import { useRouter, useRoute } from 'vue-router';
import { useUserStore } from '@/stores/user';

const boardStore = useBoardStore();
const router = useRouter();
const route = useRoute();
const userStore = useUserStore();

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

const title = ref('');
const content = ref('');

onMounted(async () => {
  await boardStore.getDetailArticle(route.params.id);
  if (boardStore.article) {
    title.value = boardStore.article.title || '';
    content.value = boardStore.article.content || '';
  }
});

watch(
  () => boardStore.article,
  newArticle => {
    if (newArticle) {
      title.value = newArticle.title || '';
      content.value = newArticle.content || '';
    }
  },
);

const edit = function () {
  const payload = {
    id: route.params.id,
    title: title.value,
    content: content.value,
  };
  boardStore.updateArticle(payload);
};
</script>
