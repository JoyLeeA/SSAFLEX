<template>
  <div>
    <b-card>
      <div class="content-detail-content-info">
        <div class="content-detail-content-info-left">
          <div class="content-detail-content-info-left-number">
            {{items.id}}
          </div>
          <div class="content-detail-content-info-left-subject">
            {{items.title}}
          </div>
        </div>
        <div class="content-detail-content-info-right">
          <div class="content-detail-content-info-right-user">
            글쓴이: {{items.user.username}}
          </div>
          <div class="content-detail-content-info-right-created">
            등록시간: {{items.created_at | slice}}
            <br>
            수정시간: {{items.updated_at | slice}}
          </div>
        </div>
      </div>
      <div class="content-detail-content">
        {{items.content}}
      </div>
      <div class="content-detail-button">
        <b-button variant="primary" @click="updateData">수정</b-button>
        <b-button variant="success" @click="deleteData">삭제</b-button>
      </div>
        <CommentCreate @create-comment="getComments" />
      <div v-for="(comment, idx) in comments" :key='idx'>
          <div class="content-detail-comment" v-if="items.id === comment.article.id">
            작성자: {{ comment.user.username }} |
            내용: {{ comment.content }} |
            작성시간: {{ comment.created_at | slice }}
            <b-button variant="success" @click="deleteComment(comment.id)">삭제</b-button>

          </div>
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

import CommentCreate from './CommentCreate.vue';

export default {
  name: "ContentDetail",
  components: {
    CommentCreate,
  },
  data: function () {
    return {
      items: [],
      comments: [],
    };
  },
  computed: {
    rows() {
      return this.comments.length;
    }
  },
  created() {
    // const config = this.setToken()
    this.getItems()
    this.getComments()
    // this.getList();
    // this.getCommentCount();
    },
    filters: {
    slice: function (origin) {
      return origin.slice(0, 19);
    },
  },
  methods: {
    getItems: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/board/${this.$route.params.contentId}`, config)
      .then((res) => {
        this.items = res.data
    })
    },
    getComments: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/board/${this.$route.params.contentId}/comments/`, config)
      .then((res) => {
      this.comments = res.data
      console.log(this.comments)
    })
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    deleteData: async function () {
      const config = this.setToken()
      await axios.delete(`${SERVER_URL}/board/${Number(this.$route.params.contentId)}`, config)
      this.$router.push({
        path: '/board/free'
      })
    },
    deleteComment: async function (idx) {
      const config = this.setToken()
      await axios.delete(`${SERVER_URL}/board/${Number(this.$route.params.contentId)}/comments/${Number(idx)}`, config)
      this.getComments()
      // this.$router.push({
      //   path: `/board/free/detail/${Number(this.$route.params.contentId)}`
      // })
    },
    updateData() {
      this.$router.push({
        path: `/board/free/create/${Number(this.$route.params.contentId)}`,
      })
    }
  },
  watch: {
    comments: function (newComments) {
      this.comments = newComments
    }
  }
};
</script>
<style scoped>
.content-detail-content-info {
  border: 1px solid black;
  display: flex;
  justify-content: space-between;
}
.content-detail-content-info-left {
  width: 720px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}
.content-detail-content-info-right {
  width: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}
.content-detail-content {
  border: 1px solid black;
  margin-top: 1rem;
  padding-top: 1rem;
  min-height: 720px;
}
.content-detail-button {
  border: 1px solid black;
  margin-top: 1rem;
  padding: 2rem;
}
.content-detail-comment {
  border: 1px solid black;
  margin-top: 1rem;
  padding: 2rem;
}
</style>