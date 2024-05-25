<template>
  <li
    class="relative w-full"
    :class="{
      'comment-hover': props.comment.nickname === userStore.nickname,
    }"
    @click="toggleEditForm"
  >
    <span class="block font-bold lg:inline-block lg:mr-3 text-md">{{
      props.comment.nickname
    }}</span>
    <p
      v-if="!editing"
      class="w-full text-xs font-light truncate lg:inline lg:text-sm"
    >
      {{ props.comment.comment_content }}
    </p>
    <input
      v-else
      class="w-10/12 h-8 px-3 text-xs font-light text-blue-400 truncate outline-none text-input lg:inline-block lg:text-sm bg-slate-50 max-w-[40rem]"
      type="text"
      v-model="inputValue"
      @keydown.enter.stop.prevent="editComment"
      @click.stop
    />
    <div
      v-if="editing && props.comment.nickname === userStore.nickname"
      class="absolute right-0 flex flex-row -translate-y-3 top-4 gap-x-2"
      @click.stop
    >
      <button
        @click="editComment"
        class="hover:drop-shadow transform-gpu hover:scale-110"
      >
        <Save />
      </button>
      <button
        @click="deleteComment"
        class="hover:drop-shadow transform-gpu hover:scale-110"
      >
        <Delete />
      </button>
    </div>
  </li>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import Save from 'vue-material-design-icons/ContentSaveCheck.vue';
import Delete from 'vue-material-design-icons/TrashCanOutline.vue';

const userStore = useUserStore();
const route = useRoute();
const router = useRouter();
const props = defineProps({
  comment: Object,
});

const editing = ref(false);
const inputValue = ref(props.comment.comment_content);

const toggleEditForm = () => {
  editing.value = !editing.value;
  if (!editing.value) {
    inputValue.value = props.comment.comment_content;
  }
};

const editComment = function () {
  const articleId = route.params.id;
  axios({
    url: `${userStore.API_URL}/articles/${articleId}/comments/${props.comment.id}/`,
    method: 'put',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
    data: {
      comment_content: inputValue.value,
    },
  }).then(res => {
    editing.value = false;
    const reload = () => {
      router.go(0);
    };
    reload();
  });
};

const deleteComment = function () {
  const articleId = route.params.id;
  axios({
    url: `${userStore.API_URL}/articles/${articleId}/comments/${props.comment.id}/`,
    method: 'delete',
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  }).then(res => {
    editing.value = false;
    const reload = () => {
      router.go(0);
    };
    reload();
  });
};
</script>
