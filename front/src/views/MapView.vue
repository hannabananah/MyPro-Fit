<template>
  <div class="h-screen py-12">
    <div
      style="
        border-radius: 60px;
        overflow: hidden;
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.05);
      "
      class="container relative flex flex-col w-4/5 pb-6 mx-auto"
    >
      <img
        class="object-cover overflow-hidden max-h-56"
        src="@/assets/images/map.jpg"
        alt="지점검색 페이지 헤더 이미지"
      />
      <h1
        class="absolute text-xl font-bold tracking-widest text-center text-white transition-all transform -translate-x-1/2 lg:text-5xl md:text-3xl top-24 left-1/2 sm:text-2xl"
      >
        주변 은행 지점 찾기
      </h1>
      <div class="flex flex-row mb-4 h-[600px]">
        <div
          id="map-container"
          style="width: 70%; height: 100%"
          class="flex flex-col items-center"
        >
          <form
            class="flex justify-center w-full"
            @submit.prevent="searchPlaces"
          >
            <div
              class="flex justify-between border border-slate-400 rounded-2xl mb-4 w-1/2 h-[5vh] mt-6"
            >
              <input
                type="text"
                class="w-5/6 ml-5 bg-transparent focus:outline-none"
                placeholder="(예시) 역삼역 OO은행"
                v-model="keyWord"
              />
              <button>
                <img
                  src="@/assets/icons/search-icon-slate200.svg"
                  class="mr-4 h-3/5"
                />
              </button>
            </div>
          </form>
          <div ref="mapContainer" style="width: 100%; height: 100%"></div>
        </div>
        <div id="bank-list" class="h-[510px] mt-6 ml-3 w-1/3">
          <h2 class="my-5 text-xl font-bold text-gray-900">목록 보기</h2>
          <div id="menu_wrap" class="h-full overflow-auto">
            <ul class="" id="placesList"></ul>
            <div class="hidden" id="pagination"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
const apiKey = import.meta.env.VITE_MAP_API_KEY;

const mapContainer = ref(null);
const keyWord = ref(null);
const markers = ref([]);
// 장소 검색 객체를 생성합니다
const ps = new kakao.maps.services.Places();

// 검색 결과 목록이나 마커를 클릭했을 때 장소명을 표출할 인포윈도우를 생성합니다
const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
let mapInstance;
onMounted(() => {
  loadMap(mapContainer.value);
});

const loadMap = container => {
  const script = document.createElement('script');
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${apiKey}&autoload=false&libraies=services`;
  document.head.appendChild(script);

  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
      };

      mapInstance = new window.kakao.maps.Map(container, options);
    });
  };
};

// 키워드 검색을 요청하는 함수입니다
function searchPlaces() {
  if (!keyWord.value.replace(/^\s+|\s+$/g, '')) {
    alert('키워드를 입력해주세요.');
    return false;
  }

  // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다
  ps.keywordSearch(keyWord.value + '은행', placesSearchCB);
  keyWord.value = '';
}

// 장소검색이 완료됐을 때 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    // 정상적으로 검색이 완료됐으면
    // 검색 목록과 마커를 표출합니다
    displayPlaces(data);

    // 페이지 번호를 표출합니다
    displayPagination(pagination);
  } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
    alert('검색 결과가 존재하지 않습니다.');
    return;
  } else if (status === kakao.maps.services.Status.ERROR) {
    alert('검색 결과 중 오류가 발생했습니다.');
    return;
  }
}

// 검색 결과 목록과 마커를 표출하는 함수입니다
function displayPlaces(places) {
  var listEl = document.getElementById('placesList'),
    menuEl = document.getElementById('menu_wrap'),
    fragment = document.createDocumentFragment(),
    bounds = new kakao.maps.LatLngBounds(),
    listStr = '';

  // 검색 결과 목록에 추가된 항목들을 제거합니다
  removeAllChildNods(listEl);

  // 지도에 표시되고 있는 마커를 제거합니다
  removeMarker();

  for (var i = 0; i < places.length; i++) {
    // 마커를 생성하고 지도에 표시합니다
    var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
      marker = addMarker(placePosition, i),
      itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    bounds.extend(placePosition);

    // 마커와 검색결과 항목에 mouseover 했을때
    // 해당 장소에 인포윈도우에 장소명을 표시합니다
    // mouseout 했을 때는 인포윈도우를 닫습니다
    (function (marker, title) {
      kakao.maps.event.addListener(marker, 'mouseover', function () {
        displayInfowindow(marker, title);
      });

      kakao.maps.event.addListener(marker, 'mouseout', function () {
        infowindow.close();
      });

      itemEl.onmouseover = function () {
        displayInfowindow(marker, title);
      };

      itemEl.onmouseout = function () {
        infowindow.close();
      };
    })(marker, places[i].place_name);

    fragment.appendChild(itemEl);
  }

  // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
  listEl.appendChild(fragment);
  menuEl.scrollTop = 0;

  // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
  mapInstance.setBounds(bounds);
}

// 검색결과 항목을 Element로 반환하는 함수입니다
function getListItem(index, places) {
  var el = document.createElement('li'),
    itemStr =
      '<span class="markerbg marker_' +
      (index + 1) +
      '"></span>' +
      '<div class="p-2 mb-3 mr-3 info bg-slate-50">' +
      '   <h5 class="text-sm text-gray-900">' +
      places.place_name +
      '</h5>';

  if (places.road_address_name) {
    itemStr +=
      '    <span class="text-xs text-gray-500">' +
      places.road_address_name +
      '</span>';
    // +
    // '   <p class="text-gray-500">' +
    // places.address_name +
    // '</p>';
  } else {
    itemStr +=
      '    <span class="text-xs text-gray-500">' +
      places.address_name +
      '</span>';
  }

  itemStr +=
    '  <span class="text-xs tel text-sky-700">' +
    places.phone +
    '</span>' +
    '</div>';

  el.innerHTML = itemStr;
  el.className = 'item';

  return el;
}

// 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
function addMarker(position, idx, title) {
  var imageSrc =
      'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
    imageSize = new kakao.maps.Size(36, 37), // 마커 이미지의 크기
    imgOptions = {
      spriteSize: new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
      spriteOrigin: new kakao.maps.Point(0, idx * 46 + 10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
      offset: new kakao.maps.Point(13, 37), // 마커 좌표에 일치시킬 이미지 내에서의 좌표
    },
    markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
    marker = new kakao.maps.Marker({
      position: position, // 마커의 위치
      image: markerImage,
    });

  marker.setMap(mapInstance); // 지도 위에 마커를 표출합니다
  markers.value.push(marker); // 배열에 생성된 마커를 추가합니다

  return marker;
}

// 지도 위에 표시되고 있는 마커를 모두 제거합니다
function removeMarker() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  markers.value = [];
}

// 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
function displayPagination(pagination) {
  var paginationEl = document.getElementById('pagination'),
    fragment = document.createDocumentFragment(),
    i;

  // 기존에 추가된 페이지번호를 삭제합니다
  while (paginationEl.hasChildNodes()) {
    paginationEl.removeChild(paginationEl.lastChild);
  }

  for (i = 1; i <= pagination.last; i++) {
    var el = document.createElement('a');
    el.href = '#';
    el.innerHTML = i;

    if (i === pagination.current) {
      el.className = 'on';
    } else {
      el.onclick = (function (i) {
        return function () {
          pagination.gotoPage(i);
        };
      })(i);
    }

    fragment.appendChild(el);
  }
  paginationEl.appendChild(fragment);
}

// 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
// 인포윈도우에 장소명을 표시합니다
function displayInfowindow(marker, title) {
  var content = '<div style="padding:5px;z-index:1;">' + title + '</div>';

  infowindow.setContent(content);
  infowindow.open(mapInstance, marker);
}

// 검색결과 목록의 자식 Element를 제거하는 함수입니다
function removeAllChildNods(el) {
  while (el.hasChildNodes()) {
    el.removeChild(el.lastChild);
  }
}
</script>

<style scoped></style>
