<template>
  <div>
    <div v-if="`${this.$route.params.contentId}`=='undefined'">
      <b-input v-model="articleItem.title" placeholder="제목을 입력해 주세요"></b-input>
      <br>
      <b-form-textarea
        v-model="articleItem.content"
        placeholder="내용을 입력해 주세요"
        rows="6"
        max-rows="10"
      ></b-form-textarea>
      <br>
      <b-button class="mr-5" @click="createArticle">저장</b-button>
      <b-button @click="cancle">취소</b-button>
    </div>
    <div v-else>
      <b-input v-model="items.title" placeholder="제목을 입력해 주세요"></b-input>
      <b-form-textarea
        v-model="items.content"
        placeholder="내용을 입력해 주세요"
        rows="6"
        max-rows="10"
      ></b-form-textarea>
      <b-button @click="updateArticle">저장</b-button>
      <b-button @click="cancle">취소</b-button>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Create',
  data() {
    return {
      items: [],
      articleItem: {
        title: '',
        content: '',
      }
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },

    createArticle: function () {
    const config = this.setToken()
    axios.post(`${SERVER_URL}/board/`, this.articleItem, config)
    .then(() => {
      this.$router.push({
        path: '/board/free/'
      })
    })
    },
    updateArticle: function () {
      const config = this.setToken()
      axios.put(`${SERVER_URL}/board/${this.$route.params.contentId}/`, this.items, config)
      .then(() => {
        this.$router.push({
          path: `/board/free/detail/${this.$route.params.contentId}`
        })
      })
    },
    cancle: function () {
      this.$router.push({
        path: '/board/free/'
      })
    }
  },
  created: function () {
    const config = this.setToken()
    axios.get(`${SERVER_URL}/board/${this.$route.params.contentId}`, config)
    .then((res) => {
      this.items = res.data
    })
  },
  }
</script>