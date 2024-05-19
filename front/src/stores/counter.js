import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import { useRouter } from 'vue-router';

export const useCounterStore = defineStore(
  'counter',
  () => {
    const API_URL = 'http://127.0.0.1:8000';
    const token = ref(null);
    const username = ref(null);
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const errorMessage = ref(null);
    const isLogin = computed(() => {
      return token.value !== null;
    });
    const router = useRouter();

    const signUp = function (payload) {
      const { email, password1, password2, username } = payload;

      if (!email || !password1 || !password2 || !username) {
        errorMessage.value = '모든 필드를 입력해주세요.';
        return;
      }
      if (!emailRegex.test(email)) {
        errorMessage.value = '올바른 이메일 주소를 입력해주세요.';
        return;
      }
      if (password1.length < 8) {
        errorMessage.value = '비밀번호는 최소 8자 이상이어야 합니다.';
        return;
      } else if (password1.length > 15) {
        errorMessage.value = '비밀번호는 최대 15자 이하이어야 합니다.';
        return;
      }
      if (password1 !== password2) {
        errorMessage.value = '비밀번호가 일치하지 않습니다.';
        return;
      }
      if (username.length < 2) {
        errorMessage.value = '닉네임은 최소 두 글자 이상이어야 합니다.';
        return;
      } else if (username.length > 20) {
        errorMessage.value = '닉네임은 최대 20자 이하이어야 합니다.';
        return;
      }

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          email,
          password1,
          password2,
          username,
        },
      })
        .then(res => {
          console.log('회원가입 성공!');
          const password = password1;
          logIn({ email, password });
        })
        .catch(error => {
          console.log('error.response', error);
          if (error.response && error.response.status === 500) {
            errorMessage.value = '이미 존재하는 이메일 주소입니다.';
          } else if (error.response && error.response.status === 400) {
            errorMessage.value = error.response.data.password1.join(' ');
          } else {
            console.error('회원가입 중 오류 발생:', error);
          }
        });
    };

    const logIn = function (payload) {
      const { email, password } = payload;

      if (!email || !password) {
        errorMessage.value = '모든 필드를 입력해주세요.';
        return;
      }

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          email,
          password,
        },
      })
        .then(response => {
          console.log('로그인 성공!');
          token.value = response.data.key;
          // getUserInfo();
          router.push({ name: 'home' });
        })
        .catch(error => {
          console.log(error);
          if (error.response && error.response.status === 400) {
            errorMessage.value =
              '존재하지 않는 ID이거나 올바르지 않은 비밀번호입니다.';
          }
        });
    };

    const logOut = function () {
      token.value = null;
      username.value = null;
      router.push({ name: 'login' });
    };

    // const getUserInfo = function () {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/accounts/userinfo/`,
    //     headers: {
    //       Authorization: `Token ${token.value}`,
    //     },
    //   })
    //     .then(response => {
    //       console.log('사용자 정보 가져오기 성공!');
    //       username.value = response.data.username;
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // };

    return {
      signUp,
      API_URL,
      logIn,
      logOut,
      token,
      isLogin,
      username,
      errorMessage,
    };
  },
  { persist: true },
);
