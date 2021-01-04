<template>
  <div>
    <b-table 
      striped hover 
      :per-page="perPage"
      :current-page="currentPage"
      :items="items"
      :fields="fields"
      @row-clicked="rowClick"></b-table>
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      align="center"
    ></b-pagination>
    <b-button @click="writeContent">글쓰기</b-button>
  </div>
</template>

<script>
// import data from '@/data';
import axios from 'axios';

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Board',
  created() {
    const config = this.setToken()

    axios.get(`${SERVER_URL}/board/`, config)
    .then((res) => {
      this.items = res.data
    })
    this.getList();
  },
  filters: {
    slice: function (origin) {
      return origin.slice(0, 19)
    }
  },
  data() {
    return {
      currentPage: 1,
      perPage: 10,
      fields: [
        {
          key: "id",
          label: "글번호",
        },
        {
          key: "title",
          label: "제목",
        },
        {
          key: "created_at",
          label: "등록일",
        },
        {
          key: 'user.username',
          label: '작성자',
        },
      ],
      items: []
    };
  },
  computed: {
    rows() {
      return this.items.length;
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

    rowClick(item) {
      this.$router.push({
        path: `/board/free/detail/${item.id}`
      })
    },
    writeContent() {
      this.$router.push({
        path: '/board/free/create'
      })
    },
  }
}
</script>