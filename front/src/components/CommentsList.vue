<template>
  <div class="relative">
    <li
      class="w-full"
      :class="{
        'comment-hover': props.comment.username === userStore.username,
      }"
      @click="toggleEditForm"
    >
      <span class="block font-bold lg:inline-block lg:mr-3 text-md">{{
        props.comment.username
      }}</span>
      <p
        v-if="!editing"
        class="w-full text-xs font-light truncate lg:inline lg:text-sm"
      >
        {{ props.comment.comment_content }}
      </p>
      <input
        v-else
        class="w-10/12 h-8 px-3 text-xs font-light text-blue-400 truncate outline-none text-input lg:inline lg:text-sm bg-slate-50"
        type="text"
        v-model="inputValue"
        @keydown.enter.stop.prevent="editComment"
        @click.stop
      />
    </li>
    <div
      v-if="editing && props.comment.username === userStore.username"
      class="absolute right-0 flex flex-row top-5 gap-x-2"
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
  </div>
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
    console.log(res.data);
    editing.value = false;
    const reload = () => {
      router.go(0);
    };
    reload();
  });
};
</script>
