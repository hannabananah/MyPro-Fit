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
import BoardView from '@/views/BoardView.vue';

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
      path: '/product/:type/:code',
      name: 'product-detail',
      component: ProductDetail,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView,
    },
  ],
});

export default router;
