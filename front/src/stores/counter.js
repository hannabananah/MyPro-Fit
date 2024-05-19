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
    const errorMessage = ref(null);
    const isLogin = computed(() => {
      return token.value !== null;
    });
    const router = useRouter();

    const signUp = function (payload) {
      const { email, password1, password2, username } = payload;

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
          if (error.response && error.response.status === 500) {
            // 이미 존재하는 이메일 주소인 경우
            errorMessage.value = '이미 존재하는 이메일 주소입니다.';
          } else {
            console.error('회원가입 중 오류 발생:', error);
          }
        });
    };

    const logIn = function (payload) {
      const { email, password } = payload;
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
          getUserInfo();
          router.push({ name: 'home' });
        })
        .catch(error => {
          console.log(error);
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

    return { signUp, API_URL, logIn, logOut, token, isLogin, username };
  },
  { persist: true },
);
