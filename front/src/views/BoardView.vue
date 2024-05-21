<template>
  <div class="py-12">
    <div
      class="container relative flex flex-col items-center w-4/5 mx-auto overflow-hidden rounded-lg shadow-md bg-slate-100"
    >
      <img
        class="object-cover w-full overflow-hidden grayscale-[40%] h-56 blur-[3px]"
        src="@/assets/images/board.jpg"
        alt="게시판 페이지 헤더 이미지"
      />
      <h1
        class="absolute text-5xl font-bold tracking-widest text-center text-white top-24"
      >
        <span class="hidden text-white sm:inline-block">커뮤니티</span> 게시판
      </h1>
      <div class="flex flex-col w-3/5 my-8">
        <button
          class="flex items-center self-end px-4 my-2 btn-active w-min"
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
