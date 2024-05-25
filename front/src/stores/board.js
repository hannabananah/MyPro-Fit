import { ref } from 'vue';
import { defineStore } from 'pinia';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useUserStore } from '@/stores/user';

export const useBoardStore = defineStore(
  'board',
  () => {
    const router = useRouter();
    const articles = ref([]);
    const article = ref(null);
    const userStore = useUserStore();

    const fetchArticles = function () {
      axios({
        url: `${userStore.API_URL}/articles/`,
        method: 'get',
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then(res => {
          articles.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    const getDetailArticle = function (articleId) {
      axios({
        method: 'get',
        url: `${userStore.API_URL}/articles/${articleId}/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then(res => {
          article.value = res.data;
        })
        .catch(err => {
          console.log(err);
        });
    };

    const deleteArticle = function (articleId) {
      axios({
        url: `${userStore.API_URL}/articles/${articleId}/`,
        method: 'delete',
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
      })
        .then(res => {
          fetchArticles();
          router.push({ name: 'board' });
        })
        .catch(err => {
          console.log(err);
        });
    };

    const updateArticle = function (payload) {
      const { id, title, content } = payload;
      axios({
        method: 'put',
        url: `${userStore.API_URL}/articles/${id}/`,
        headers: {
          Authorization: `Token ${userStore.token}`,
        },
        data: {
          title: title,
          content: content,
        },
      })
        .then(res => {
          fetchArticles();
          router.push({ name: 'board-detail', params: { id: id } });
        })
        .catch(err => console.log(err));
    };
    return {
      articles,
      fetchArticles,
      getDetailArticle,
      article,
      deleteArticle,
      updateArticle,
    };
  },
  { persist: true },
);
