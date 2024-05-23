import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import SignupView from '@/views/SignupView.vue';
import ExchangeView from '@/views/ExchangeView.vue';
import MapView from '@/views/MapView.vue';
import ProfileView from '@/views/ProfileView.vue';
import ProductsView from '@/views/ProductsView.vue';
import ProductDepositList from '@/components/ProductDepositList.vue';
import ProductSavingList from '@/components/ProductSavingList.vue';
import ProductAnnuityList from '@/components/ProductAnnuityList.vue';
import ProductDetail from '@/components/ProductDetail.vue';
import CreateArticle from '@/components/CreateArticle.vue';
import BoardView from '@/views/BoardView.vue';
import BoardArticleDetail from '@/components/BoardArticleDetail.vue';
import UpdateArticle from '@/components/UpdateArticle.vue';
import ProductsRecommendView from '@/views/ProductsRecommendView.vue';
import ProductRecommendList from '@/components/ProductRecommendList.vue';
import ErrorView from '@/views/ErrorView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/exchange-rate',
      name: 'exchange',
      component: ExchangeView,
    },
    {
      path: '/bank',
      name: 'map',
      component: MapView,
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView,
      children: [
        {
          path: '',
          name: 'deposit',
          component: ProductDepositList,
        },
        {
          path: 'saving',
          name: 'saving',
          component: ProductSavingList,
        },
        {
          path: 'annuity',
          name: 'annuity',
          component: ProductAnnuityList,
        },
      ],
    },
    {
      path: '/create-article',
      name: 'create-article',
      component: CreateArticle,
    },
    {
      path: '/product/:type/:code',
      name: 'product-detail',
      component: ProductDetail,
    },
    {
      path: '/profile/:tab',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView,
    },
    {
      path: '/board/:id',
      name: 'board-detail',
      component: BoardArticleDetail,
    },
    {
      path: '/board/:id/update',
      name: 'update-article',
      component: UpdateArticle,
    },
    {
      path: '/products/recommend',
      name: 'recommend',
      component: ProductsRecommendView,
    },
    {
      path: '/products/recommend/list',
      name: 'recommend-list',
      component: ProductRecommendList,
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'error',
      component: ErrorView,
    },
  ],
});

import { useUserStore } from '@/stores/user';

router.beforeEach((to, from) => {
  const store = useUserStore();
  if (
    (to.name == 'board-detail') |
      (to.name == 'create-article') |
      (to.name == 'product-detail') |
      (to.name == 'update-article') |
      (to.name == 'recommend-list') &&
    store.isLogin === false
  ) {
    window.alert('로그인이 필요합니다.');
    return { name: 'login' };
  }

  // 인증 o 로그인x 회원가입x
  if ((to.name == 'signup') | (to.name == 'login') && store.isLogin === true) {
    window.alert('이미 로그인 되어있습니다.');
    return { name: 'home' };
  }

  if (to.name === 'update-article' && store.user !== store.article.username) {
    window.alert('본인이 아닌 경우 수정할 수 없습니다.');
    return { name: 'board-detail', params: { id: store.article.id } };
  }
});

export default router;
