<template>
  <div class="py-12">
    <div
      :style="`background-color: ${randColor}`"
      class="container relative flex flex-col items-center w-3/5 mx-auto overflow-hidden rounded-lg shadow-md bg-slate-100"
    >
      <article class="flex flex-col w-full p-10 gap-y-3">
        <div class="flex justify-between w-full">
          <i class="text-gray-900">No.{{ boardStore.article.id }}</i>
          <span class="text-sm tracking-wide text-gray-500">
            {{ boardStore.article.username }}
          </span>
        </div>
        <h2 class="text-xl font-bold text-gray-900 hahmlet">
          {{ boardStore.article.title }}
        </h2>
        <p class="my-5 font-light hahmlet">{{ boardStore.article.content }}</p>
        <span class="inline-block text-sm text-right">
          {{ formattedCreatedAt }}
        </span>
        <div
          class="flex self-end w-1/3 gap-x-2"
          v-if="boardStore.article.username === userStore.username"
        >
          <button class="btn-active" @click="handleClickEdit">UPDATE</button>
          <button class="btn-inactive" @click="handleClickDelete">
            DELETE
          </button>
        </div>
        <div>
          <form @submit.prevent="createComment">
            <label for="comment" class="mr-2">댓글 :</label>
            <input
              class="w-3/5 px-1 bg-transparent border-b border-gray-500 outline-none caret-gray-500"
              type="text"
              id="comment"
              v-model="comment"
            />
          </form>
          <ul class="list-none">
            <CommentsList
              v-for="comment in comments"
              :key="comment.id"
              :comment="comment"
            />
          </ul>
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

const fetchComments = () => {
  const articleId = route.params.id;
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
    params: { id: boardStore.article.id },
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
    fetchComments(articleId);
    comment.value = '';
  });
};
</script>
