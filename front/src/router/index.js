import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ExchangeView from '@/views/ExchangeView.vue';
import MapView from '@/views/MapView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
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
  ],
});

export default router;
