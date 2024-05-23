<template>
  <div class="masonry" v-if="articles">
    <BoardArticleListItem
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import BoardArticleListItem from '@/components/BoardArticleListItem.vue';
defineProps({ articles: Object });
</script>
