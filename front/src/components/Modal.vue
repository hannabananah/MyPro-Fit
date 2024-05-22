<template>
  <vue-final-modal
    v-slot="{ params, close }"
    v-bind="$attrs"
    classes="flex justify-center items-center"
    content-class="relative flex flex-col max-h-full p-6 mx-4 bg-white border rounded gap-y-3"
  >
    <span class="mr-8 text-xl font-bold">
      {{ modalTitle }}
    </span>
    <div class="flex-grow overflow-y-auto text-sm">
      <slot></slot>
    </div>
    <div class="flex items-center justify-center flex-shrink-0 gap-2 pt-4">
      <v-button
        class="basis-1/2 btn-inactive"
        @click="$emit('cancel', close)"
        >{{ cancelText }}</v-button
      >
      <v-button class="basis-1/2 btn-active" @click="$emit('confirm', close)">{{
        confirmText
      }}</v-button>
    </div>
    <button class="absolute top-0 right-0 mt-3 mr-3" @click="close">
      <span class="text-lg cursor-pointer">&times;</span>
    </button>
  </vue-final-modal>
</template>

<script setup>
const props = defineProps({
  modalTitle: String,
  confirmText: String,
  cancelText: String,
});

// const CustomModal = {
//   name: 'CustomModal',
//   inheritAttrs: false,
//   emits: ['cancel', 'confirm'],
// };
</script>
