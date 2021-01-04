<template>
  <div class="comment-create">
    <b-input-group :prepend="name" class="mt-3">
      <b-form-textarea
        id="textarea"
        v-model="commentItem.content"
        :placeholder="'코멘트를 달아주세요~!'"
        rows="3"
        max-rows="6"
      ></b-form-textarea>
      <b-input-group-append>
        <b-button variant="info" @click="createComment">작성하기</b-button>
      </b-input-group-append>
    </b-input-group>
  </div>
</template>
<script>
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: "CommentCreate",
  data: function () {
    return {
      commentItem: {
        content: '',
      }
    };
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

    createComment: async function () {
      const config = this.setToken()
      // console.log('?' ,this.commentItem, config)
      await axios.post(`${SERVER_URL}/board/${Number(this.$route.params.contentId)}/comments/`, this.commentItem, config)
      this.$emit('create-comment')
      this.commentItem.content = ''
      // this.$router.push({
      //   path: `/board/free/detail/${Number(this.$route.params.contentId)}`
      // })
    },
  },
};
</script>
<style scoped>
.comment-create {
  display: flex;
  margin-bottom: 1em;
}
</style>