<template>
  <div>
    <h1 class="text-white my-5">Login</h1>
    <div>
      <b-form-input v-model="credentials.username" placeholder="Enter your ID"></b-form-input>
      <!-- <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username"> -->
    </div>
    <div>
      <b-form-input class="my-5" @keypress.enter="login" v-model="credentials.password" placeholder="Enter your PW"></b-form-input>
      <!-- <label for="password">비밀번호: </label>
      <input 
        type="password" 
        id="password" 
        v-model="credentials.password"
        @keypress.enter="login"
      > -->
    </div>
    <button class="btn btn-success" @click="loginn">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    loginn: function () {
      axios.post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('login')
          this.$router.push({ name: 'Board' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'login',
    ])
  }
}
</script>
