<template>
  <div>
    <h1 class="text-white my-5">Signup</h1>
    <div>
      <b-form-input v-model="credentials.username" placeholder="Enter your ID"></b-form-input>
      <!-- <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username"> -->
    </div>
    <div>
      <b-form-input class="my-5" v-model="credentials.password" placeholder="Enter your PW"></b-form-input>
      <!-- <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password"> -->
    </div>
    <div>
      <b-form-input @keypress.enter="signup" class="my-5" v-model="credentials.passwordConfirmation" placeholder="Enter your PW (one more time)"></b-form-input>
      <!-- <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password" 
        id="passwordConfirmation" 
        v-model="credentials.passwordConfirmation"
        @keypress.enter="signup"
      > -->
    </div>
    <button class="btn btn-success" @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios.post(`${SERVER_URL}/accounts/signup/`, this.credentials)
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'Login' })
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
