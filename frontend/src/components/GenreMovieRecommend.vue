<template>
  <div>
      <div class="d-flex mb-3">
        <p class="justify-content-start ml-5 mt-5 text-left recommend-title mr-5">장르별 영화</p>
        <select v-model="selectedGenre" @change="genreChange" class="ml-auto custom-select w-25 my-5" name="genre">
            <option v-for="(genre, idx) in genres" :key="idx">{{ genre.name }}</option>
        </select>
      </div>
      <carousel :loop="true" v-if="genreMovies" class="d-flex justify-content-center mx-3"
      :mouse-drag="false" 
      :navigationEnabled="true" :navigationClickTargetSize="18"
      :paginationEnabled="false" 
      :perPageCustom="[[400,2],[548,2], [768, 3], [1024, 4], [1209, 5],]">
          <slide class="mx-auto px-2" v-for="(movie, idx) in genreMovies" :key="idx">
              <img class="rounded movie-img" :movie='movie' @click='moveToDetail(movie)' :src="`https://image.tmdb.org/t/p/w185${movie.image}`">
          </slide>
      </carousel>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    name: 'GenreMovieRecommend',
    data: function () {
        return {
            selectedGenre: '',
            genreMovies: [],
        }
    },
    methods: {
        moveToDetail: function (movie) {
            this.$store.dispatch('moveToDetail', movie)
            this.$router.push('/movie-detail')
        },
        genreChange: function () {
            this.genreMovies = this.popularMovies.filter((movie) => {
                for (let genre of movie.genres) {
                    return genre.name === this.selectedGenre
                }
            })
            console.log(this.selectedGenre)
            console.log(this.popularMovies)
        },
    },
    computed: {
        ...mapState([
            'popularMovies',
            'genres'
        ])
    },
    created: function () {
        this.$store.dispatch('getPopularMovies')
        this.$store.dispatch('getGenres')
    }
}
</script>

<style>
    .movie-img {
        transition: .5s ease;
    }

    .movie-img:hover {
        transform: scale(1.2);
    }
</style>