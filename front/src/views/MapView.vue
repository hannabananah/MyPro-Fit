<template>
  <div class="py-12">
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="container mx-auto w-4/5 flex flex-col"
    >
      <img style="width: 100%" src="@/assets/images/map.svg" alt="" />
      <div id="map-container" style="width: 60%; height: 500px" class="my-8">
        <div ref="mapContainer" style="width: 100%; height: 100%"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
const mapContainer = ref(null);
onMounted(() => {
  loadMap(mapContainer.value);
});

const loadMap = container => {
  const script = document.createElement('script');
  script.src =
    'https://dapi.kakao.com/v2/maps/sdk.js?appkey=19d64a8f19b787f13e9dda583e49dad8&autoload=false';
  document.head.appendChild(script);

  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
      };

      const mapInstance = new window.kakao.maps.Map(container, options);
    });
  };
};
</script>

<style scoped></style>
