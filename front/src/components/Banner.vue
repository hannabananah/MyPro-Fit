<template>
  <carousel :items-to-show="1" :autoplay="4000" :wrap-around="true">
    <slide v-for="index in images" :key="index">
      <img
        :src="getImageUrl(index)"
        :alt="getAltText(index)"
        class="object-cover w-full max-h-96"
      />
    </slide>
  </carousel>
</template>

<script>
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide } from 'vue3-carousel';

export default {
  name: 'Banner',
  components: {
    Carousel,
    Slide,
  },
  data() {
    return {
      images: [1, 2, 3, 4, 5, 6],
    };
  },
  methods: {
    getImageUrl(index) {
      return `images/banners/banner${index}.jpg`;
    },
    getAltText(index) {
      return `배너이미지${index}`;
    },
  },
};
</script>
