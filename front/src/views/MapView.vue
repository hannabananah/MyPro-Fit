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
      <div></div>
      <div class="flex flex-row mb-4">
        <div
          id="map-container"
          style="width: 50%; height: 400px"
          class="flex flex-col items-center"
        >
          <form class="flex justify-center w-full">
            <div
              class="flex justify-between border border-slate-400 rounded-2xl mb-4 w-1/2 h-[5vh] mt-6"
            >
              <input
                type="text"
                class="bg-transparent w-5/6 ml-5"
                placeholder="은행 찾기 : 지역명을 입력하세요."
              />
              <button>
                <img
                  src="@/assets/icons/search-icon-slate200.svg"
                  class="h-3/5 mr-4"
                />
              </button>
            </div>
          </form>
          <div ref="mapContainer" style="width: 100%; height: 80%"></div>
        </div>
        <div id="bank-list" class="mt-6 ml-5">
          <p class="text-xl text-gray-900">목록 보기</p>
        </div>
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
