<template>
  <div
    @click="handleClickDetail"
    :style="`background-color: ${randColor}`"
    class="p-4 transition-transform bg-white rounded-lg shadow-md cursor-pointer masonry-item hover:drop-shadow transform-gpu hover:scale-105"
  >
    <span class="text-xs text-gray-500 select-none">{{
      article.nickname
    }}</span>
    <h2 class="text-xl font-bold text-gray-900 hahmlet">
      {{ article.title }}
    </h2>
    <p class="mt-2 text-sm font-light text-gray-900 hahmlet line-clamp-5">
      {{ article.content }}
    </p>
    <p class="mt-2 text-xs text-gray-400 text-end">{{ formattedCreatedAt }}</p>
  </div>
</template>

<script setup>
import { useBoardStore } from '@/stores/board';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';
import { computed, ref } from 'vue';

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

const router = useRouter();
const boardStore = useBoardStore();
const randColor = ref(colors[Math.floor(Math.random() * colors.length)]);

const props = defineProps({
  article: Object,
});

const handleClickDetail = () => {
  boardStore.getDetailArticle(props.article.id);
  router.push({ name: 'board-detail', params: { id: props.article.id } });
};

const formattedCreatedAt = computed(() => {
  const createdAt = new Date(props.article.created_at);
  return `${createdAt.getFullYear()}/${
    createdAt.getMonth() + 1
  }/${createdAt.getDate()}`;
});
</script>
