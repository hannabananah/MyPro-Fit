import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useUserStore = defineStore(
  'counter',
  () => {
    const API_URL = 'http://127.0.0.1:8000';
    const token = ref(null);
    const username = ref(null);
    const nickname = ref(null);
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const errorFields = ref({
      username: '',
      password: '',
      password1: '',
      password2: '',
      nickname: '',
      general: '',
    });
    const isLogin = computed(() => token.value !== null);
    const router = useRouter();
    const clearErrors = () => {
      Object.keys(errorFields.value).forEach(field => {
        errorFields.value[field] = '';
      });
    };

    const validateSignup = ({ username, password1, password2, nickname }) => {
      clearErrors();

      if (!username || !password1 || !password2 || !nickname) {
        errorFields.value.general = '모든 필드를 입력해주세요.';
        if (!username) errorFields.value.username = '필수 입력 필드입니다.';
        if (!password1) errorFields.value.password1 = '필수 입력 필드입니다.';
        if (!password2) errorFields.value.password2 = '필수 입력 필드입니다.';
        if (!nickname) errorFields.value.nickname = '필수 입력 필드입니다.';
        return false;
      }
      if (!emailRegex.test(username)) {
        errorFields.value.username = '올바른 이메일 주소를 입력해주세요.';
        return false;
      }
      if (password1.length < 8) {
        errorFields.value.password1 = '비밀번호는 최소 8자 이상이어야 합니다.';
        return false;
      }
      if (password1.length > 15) {
        errorFields.value.password1 = '비밀번호는 최대 15자 이하이어야 합니다.';
        return false;
      }
      if (password1 !== password2) {
        errorFields.value.password2 = '비밀번호가 일치하지 않습니다.';
        return false;
      }
      if (nickname.length < 2) {
        errorFields.value.nickname = '닉네임은 최소 두 글자 이상이어야 합니다.';
        return false;
      }
      if (nickname.length > 20) {
        errorFields.value.nickname = '닉네임은 최대 20자 이하이어야 합니다.';
        return false;
      }

      return true;
    };

    const validateLogin = ({ username, password }) => {
      clearErrors();

      if (!username || !password) {
        errorFields.value.general = '모든 필드를 입력해주세요.';
        if (!username) errorFields.value.username = '필수 입력 필드입니다.';
        if (!password) errorFields.value.password = '필수 입력 필드입니다.';
        return false;
      }

      if (!emailRegex.test(username)) {
        errorFields.value.username = '올바른 이메일 주소를 입력해주세요.';
        return false;
      }

      return true;
    };

    const shouldShowError = field => errorFields.value[field] !== '';

    const signUp = function (payload) {
      if (!validateSignup(payload)) return;

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
          nickname: payload.nickname,
        },
      })
        .then(res => {
          console.log('회원가입 성공!');
          logIn({ username: payload.username, password: payload.password1 });
        })
        .catch(error => {
          if (error.response && error.response.status === 500) {
            errorFields.value.general = '이미 존재하는 이메일 주소입니다.';
          } else {
            errorFields.value.general = error.message;
          }
        });
    };

    const logIn = function (payload) {
      if (!validateLogin(payload)) return;

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      })
        .then(response => {
          console.log('로그인 성공!');
          token.value = response.data.key;
          router.push({ name: 'home' });
        })
        .catch(error => {
          console.log(error);
          const errorMessage =
            error.response?.data?.detail ||
            '존재하지 않는 ID이거나 올바르지 않은 비밀번호입니다. 다시 시도해주세요.';
          errorFields.value.general = errorMessage;
        });
    };

    const logOut = function () {
      token.value = null;
      nickname.value = null;
      router.push({ name: 'login' });
    };

    const deleteAccount = function () {
      axios({
        method: 'delete',
        url: `${API_URL}/accounts/delete/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then(() => {
          console.log('계정 삭제 성공!');
          logOut();
        })
        .catch(error => {
          console.error('계정 삭제 중 오류 발생:', error);
        });
    };

    const getUserInfo = function () {
      if (!token.value) {
        console.error('Token is not set');
        return;
      }

      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then(response => {
          nickname.value = response.data.nickname;
          username.value = response.data.username;
          console.log('유저 정보 가져오기 성공:', response.data);
        })
        .catch(error => {
          console.error('유저 정보 가져오기 중 오류 발생:', error);
          throw error;
        });
    };
    return {
      signUp,
      logIn,
      logOut,
      shouldShowError,
      clearErrors,
      errorFields,
      token,
      isLogin,
      deleteAccount,
      API_URL,
      getUserInfo,
      username,
      nickname,
    };
  },
  { persist: true },
);
