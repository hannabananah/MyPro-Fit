import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from '@/views/LoginView.vue';
import SignupView from '@/views/SignupView.vue';
import ExchangeView from '@/views/ExchangeView.vue';
import MapView from '@/views/MapView.vue';
import ProfileView from '@/views/ProfileView.vue';

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
      path: '/around-bank',
      name: 'map',
      component: MapView,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
    },
  ],
});

export default router;
