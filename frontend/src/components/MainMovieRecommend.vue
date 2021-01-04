<template>
  <div class="recommend my-5">
      <p class="ml-5 mb-5 text-left recommend-title">인기 영화</p>
      <carousel class="d-flex justify-content-center mx-3"
      :mouse-drag="false" :loop="true"
      :navigationEnabled="true" :navigationClickTargetSize="18"
      :paginationEnabled="false" 
      :perPageCustom="[[400,2],[548,2], [768, 3], [1024, 4], [1209, 5],]">
          <slide class="mx-auto px-2" v-for="(movie, idx) in popularMovies" :key="idx">
              <img class="rounded movie-img" :movie='movie' @click='moveToDetail(movie)' :src="`https://image.tmdb.org/t/p/w185${movie.image}`">
          </slide>
      </carousel>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'MainMovieRecommend',
    data: function () {
        return {
            
        }
    },
    methods: {
        getPopularMovies: function () {
            this.$store.dispatch('getPopularMovies')
        },
        moveToDetail: function (movie) {
            this.$store.dispatch('moveToDetail', movie)
            this.$router.push('/movie-detail')
        }
    },
    computed: {
        ...mapState([
            'popularMovies',
        ])
    },
    created: function () {
        this.getPopularMovies()
    }
}
</script>

<style>
    .recommend-title {
        color: white;
    }
    .VueCarousel-navigation-button {
        color: white !important;
    }
    .movie-img {
        transition: .5s ease;
    }

    .movie-img:hover {
        transform: scale(1.2);
    }
</style>    