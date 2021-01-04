<template>
  <div class="detail-container">
    <div class="recommend-title d-flex backdrop" :style="{ backgroundImage: 'url(' + `https://image.tmdb.org/t/p/w185${currentMovie.backdrop}` + ')' }">
      <div class="detail-img mr-5 p-3 col">
        <img class="w-100" :src="`https://image.tmdb.org/t/p/w185${currentMovie.image}`">
      </div>
      <div class="col">
        <!-- <br> -->
        <p class="movie-title mb-3 text-left">{{ currentMovie.title }}</p>
        <p class="detail-content text-left">장르: {{ genres }}</p>
        <div class="d-flex">
          <p class="detail-content mr-3 mb-0 pt-2">평점: </p>
          <StarRating class="detail-content align-middle" :star-size="40" :rating="halfRating" :read-only="true" :increment="0.01" active-color="#1dc278"></StarRating>
        </div>
        <hr>
        <p class="detail-content text-left" v-if="currentMovie.description">{{ currentMovie.description }}</p>
        <p v-else>내용이 등록되지 않았습니다.</p>
        <hr>
        <div class="d-flex">
          <p class="pt-4 mr-3">평점 등록: </p>
          <star-rating :increment="0.5" active-color="#1dc278" />
        </div>
      </div>
    </div>
    <br>
    <iframe class="col mb-5" v-for="(video, idx) in videos" :key="idx" :src="`https://www.youtube.com/embed/${video.key}`" frameborder="0"
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen width='854' height="640"></iframe>
    <!-- <video v-for="(video, idx) in videos" :key="idx" :src="`https://www.youtube.com/watch?v=${video.key}`"></video> -->
    <!-- <p>{{ currentMovie }}</p> -->
    <!-- <textarea v-model="this.inputText" class="review"></textarea> -->
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'MovieDetail',
  components: {
    StarRating
  },
  data: function () {
    return {
      inputText: '',
      genre: '',
      videos: [],
    }
  },
  methods: {
    getVideo: function () {
      axios.get(`https://api.themoviedb.org/3/movie/${this.currentMovie.id}/videos?api_key=c490341bb152caad936b3f5ad428a088&language=ko-KR`)
      .then((res) => {
        // this.videoUrl = `https://www.youtube.com/watch?v=${res}`
        this.videos = res.data.results
      })
    }
  },
  computed: {
    ...mapState([
      'currentMovie',
    ]),
    genres: function () {
      let genreList = ''
      for (let gr of this.currentMovie.genres) {
        genreList = genreList + '  ' + gr.name
      }
      return genreList
    },
    halfRating: function () {
      return this.currentMovie.userRating/2
    },
  },
  created: function() {
    this.getVideo()
  }
}
</script>

<style>
  hr {
    /* width: 50%; */
    /* opacity: 0.5; */
    border-top: 3px solid #ffffff;
    border-bottom: 1px solid rgb(117, 122, 121);
    /* text-align: right; */
    overflow: hidden;
  }

  .movie-title {
    font-size: 1.5em;
  }

  .detail-img {
    /* float: left; */
    width: 50%;
  }

  .detail-content {
    font-size: 0.7em;
  }
  
  .review {
    width: 100%;
  }

  .detail-container {
    position: relative;
  }

  .backdrop {
    background-repeat: no-repeat;
    background-size: cover;
    /* opacity: 0.5 !important; */
  }

  .backdrop::before {
    background-color: #000;
    /* background-repeat: no-repeat;
    background-size: cover; */
    opacity: 0.7;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0px;
    left: 0px;
    right: 0px;
    bottom: -50px;
    }

</style>