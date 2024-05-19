<template>
    <div :class="{
        'flex flex-col w-full h-screen lg:flex-row': true,
        'bg-sky-100 items-center justify-center p-4': !isLg,
    }">
        <div :class="{
            'flex flex-col items-center justify-center w-full gap-10 py-10 bg-sky-100 lg:w-3/5': true,
            hidden: !isLg,
        }">
            <img :src="LogoSvg" alt="Logo Icon" class="w-1/5 h-auto lg:w-64" />
            <img :src="SignupSvg" alt="Login Icon" class="w-1/5 h-auto lg:w-[30rem]" />
        </div>
        <div
            class="flex flex-col items-center justify-center w-full h-screen lg:w-2/5 lg:items-start lg:justify-center lg:px-16">
            <h2 class="mb-6 text-2xl font-bold text-center lg:text-left">Create your Account</h2>
            <form @submit.prevent="signUp" class="flex flex-col w-full max-w-md gap-12">
                <div class="flex flex-col gap-2 lg:gap-4">
                    <div class="relative">
                        <Email class="absolute top-2.5 left-3" fillColor="#6B7280" :size="20" />
                        <input type="text" v-model.trim="email" placeholder="이메일 형식의 아이디를 입력해주세요." class="text-input" />
                    </div>
                    <div class="relative">
                        <Lock class="absolute top-2.5 left-3" fillColor="#6B7280" :size="20" />
                        <input :type="password1Visible ? 'text' : 'password'" v-model.trim="password1"
                            placeholder="8~15자 사이의 특수문자를 포함한 비밀번호를 입력해주세요." maxLength="20" class="text-input" />
                        <EyeOff v-if="!password1Visible" @click="password1Visible = true"
                            class="absolute top-2.5 right-3.5 cursor-pointer" fillColor="#6B7280" :size="20" />
                        <Eye v-else @click="password1Visible = false" class="absolute top-2.5 right-3.5 cursor-pointer"
                            fillColor="#111827" :size="20" />
                    </div>
                    <div class="relative">
                        <LockPlus class="absolute top-2.5 left-3" fillColor="#6B7280" :size="20" />
                        <input :type="password2Visible ? 'text' : 'password'" v-model.trim="password2"
                            placeholder="비밀번호를 한 번 더 입력해주세요." maxLength="20" class="text-input" />
                        <EyeOff v-if="!password2Visible" @click="password2Visible = true"
                            class="absolute top-2.5 right-3.5 cursor-pointer" fillColor="#6B7280" :size="20" />
                        <Eye v-else @click="password2Visible = false" class="absolute top-2.5 right-3.5 cursor-pointer"
                            fillColor="#111827" :size="20" />
                    </div>
                    <div class="relative">
                        <Account class="absolute top-2.5 left-3" fillColor="#6B7280" :size="20" />
                        <input type="text" v-model.trim="username" placeholder="닉네임을 입력해주세요." maxLength="20"
                            class="text-input" />
                    </div>
                    <p class="text-xs underline text-sky-700 text-end">비밀번호를 잊어버리셨습니까?</p>
                </div>
                <div class="flex flex-col gap-2">
                    <input type="submit" class="btn-active" value="Sign up" />
                    <div class="h-4">
                        <p v-if="store.errorMessage" class="text-xs text-red-500">{{ store.errorMessage }}</p>
                    </div>
                </div>
            </form>
            <div class="flex justify-center w-full gap-2 mt-4 text-xs">
                <p class="text-gary-900">이미 가입한 회원이신가요?</p>
                <RouterLink :to="{ name: 'login' }" class="font-bold text-sky-700">로그인하기</RouterLink>
            </div>
        </div>
        <div :class="{ 'hidden': isLg, 'flex items-center justify-center w-full h-20 bg-sky-100': !isLg }">
            <img :src="LogoSvg" alt="Logo Icon" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import SignupSvg from '@/assets/images/signup.svg'
import LogoSvg from '@/assets/images/logo.svg'
import Email from 'vue-material-design-icons/EmailOutline.vue';
import Lock from 'vue-material-design-icons/LockOutline.vue';
import LockPlus from 'vue-material-design-icons/LockPlusOutline.vue';
import Eye from 'vue-material-design-icons/EyeOutline.vue';
import EyeOff from 'vue-material-design-icons/EyeOffOutline.vue';
import Account from 'vue-material-design-icons/AccountOutline.vue';

const email = ref(null)
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const password1Visible = ref(false)
const password2Visible = ref(false)
const isLg = ref(window.innerWidth >= 1024)
const store = useCounterStore()

const updateWidth = () => {
    isLg.value = window.innerWidth >= 1024
}

onMounted(() => {
    store.errorMessage = null;
    window.addEventListener('resize', updateWidth)
    updateWidth()
})

onUnmounted(() => {
    window.removeEventListener('resize', updateWidth)
})

const signUp = () => {
    const payload = {
        email: email.value,
        username: username.value,
        password1: password1.value,
        password2: password2.value,
    }
    store.signUp(payload)
}

</script>