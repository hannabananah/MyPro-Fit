import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useProductStore = defineStore(
  'product',
  () => {
    return {};
  },
  { persist: true },
);
