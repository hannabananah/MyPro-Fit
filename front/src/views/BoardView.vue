<template>
  <div class="py-12">
    <div
      class="container flex flex-col items-center w-4/5 mx-auto overflow-hidden rounded-lg shadow-md"
    >
      <img
        class="object-cover w-full overflow-hidden max-h-56"
        src="@/assets/images/board.jpg"
        alt="게시판 페이지 헤더 이미지"
      />
      <div class="flex flex-col w-3/5 my-8">
        <h2 class="my-8 text-2xl font-bold text-center">게시판</h2>
        <button
          class="flex items-center self-end px-4 btn-active w-min"
          @click="handleClickCreate"
        >
          Create
        </button>
        <BoardArticleList :articles="articles" />
      </div>
    </div>
  </div>
</template>

<script setup>
import BoardArticleList from '@/components/BoardArticleList.vue';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import axios from 'axios';

const userStore = useUserStore();
const router = useRouter();

const articles = ref([]);

const fetchArticles = () => {
  axios({
    method: 'get',
    url: `${userStore.API_URL}/articles/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(res => {
      console.log('전체게시글', res.data);
      articles.value = res.data;
    })
    .catch(err => {
      console.log('userStore.API_URL', userStore.API_URL);
      console.log(err);
    });
};

onMounted(() => {
  fetchArticles();
});

const handleClickCreate = () => {
  router.push({ name: 'create-article' });
};
</script>
