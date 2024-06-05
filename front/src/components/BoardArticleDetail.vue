<template>
  <div class="h-[calc(100vh-64px)] py-12">
    <div
      v-if="boardStore.article"
      :style="`background-color: ${randColor}`"
      class="container relative flex flex-col items-center w-3/5 h-full mx-auto overflow-hidden rounded-lg shadow-md bg-slate-100"
    >
      <article
        class="relative flex flex-col justify-between w-full h-full px-10 pb-4 pt-14 gap-y-3"
      >
        <div>
          <div
            class="absolute flex right-4 top-4 gap-x-2"
            v-if="boardStore.article.nickname === userStore.nickname"
          >
            <button
              class="px-2 rounded-[8px]"
              @click="router.push({ name: 'board' })"
            >
              <undo></undo>
            </button>
            <button
              class="hover:drop-shadow transform-gpu hover:scale-110"
              @click="handleClickEdit"
            >
              <Edit />
            </button>
            <button
              class="hover:drop-shadow transform-gpu hover:scale-110"
              @click="handleClickDelete"
            >
              <Delete />
            </button>
          </div>
          <div class="flex justify-between w-full">
            <i class="text-gray-900">No.{{ boardStore.article.id }}</i>
            <div class="flex gap-4">
              <span class="inline-block text-sm text-right">
                {{ formattedCreatedAt }}
              </span>
              <span class="text-sm tracking-wide text-gray-500">
                {{ boardStore.article.nickname }}
              </span>
            </div>
          </div>
          <h2 class="text-xl font-bold text-gray-900 hahmlet">
            {{ boardStore.article.title }}
          </h2>
          <p class="my-5 overflow-y-auto font-light h-[200px] hahmlet">
            {{ boardStore.article.content }}
          </p>
        </div>
        <div v-if="comments">
          <ul class="py-2 mt-2 list-none border-t border-slate-300">
            <CommentsList
              v-for="comment in comments"
              :key="comment.id"
              :comment="comment"
            />
          </ul>
          <form
            @submit.prevent="createComment"
            class="relative flex items-center gap-x-2"
          >
            <label
              for="comment"
              class="box-border flex items-center justify-center w-10 h-10 rounded-full bg-slate-50 aspect-square"
              ><Chat fillColor="#6B7280" :size="25"
            /></label>
            <textarea
              class="flex h-auto pl-3 resize-none pr-9 text-input m-h-40"
              type="text"
              id="comment"
              v-model="comment"
            />
            <button
              type="submit"
              class="absolute flex items-center justify-center right-3 hover:scale-110"
            >
              <Send />
            </button>
          </form>
        </div>
      </article>
    </div>
  </div>
</template>

<script setup>
import { useBoardStore } from '@/stores/board';
import { onMounted, computed, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import CommentsList from '@/components/CommentsList.vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user';
import Edit from 'vue-material-design-icons/SquareEditOutline.vue';
import Delete from 'vue-material-design-icons/TrashCanOutline.vue';
import Chat from 'vue-material-design-icons/ChatOutline.vue';
import Send from 'vue-material-design-icons/Send.vue';
import undo from 'vue-material-design-icons/undo.vue';

const boardStore = useBoardStore();
const userStore = useUserStore();
const router = useRouter();
const route = useRoute();
const comments = ref([]);
const comment = ref(null);

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

const articleId = route.params.id;
const fetchComments = () => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/articles/${articleId}/comments/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      comments.value = res.data;
    })
    .catch(err => {
      console.log('Error fetching comments:', err);
    });
};

onMounted(() => {
  boardStore.getDetailArticle(route.params.id);
  fetchComments();
});

const formattedCreatedAt = computed(() => {
  const createdAt = new Date(boardStore.article.created_at);
  return `${createdAt.getFullYear()}/${
    createdAt.getMonth() + 1
  }/${createdAt.getDate()}`;
});

const handleClickDelete = function () {
  boardStore.deleteArticle(boardStore.article.id);
};

const handleClickEdit = function () {
  router.push({
    name: 'update-article',
    params: { id: boardStore.articleId },
  });
};

const createComment = function () {
  const articleId = route.params.id;
  const nextId = comments.value.length + 1;
  axios({
    method: 'post',
    url: `${userStore.API_URL}/articles/${articleId}/comments/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      id: nextId,
      comment_content: comment.value,
    },
  }).then(res => {
    fetchComments(nextId);
    comment.value = '';
  });
};
</script>
