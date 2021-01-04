<template>
  <div>
    <RandomRecommend></RandomRecommend>
    <hr>
    <MainMovieRecommend></MainMovieRecommend>
    <hr>
    <GenreMovieRecommend></GenreMovieRecommend>
  </div>
</template>

<script>
import RandomRecommend from '@/components/RandomRecommend.vue'
import MainMovieRecommend from  '@/components/MainMovieRecommend.vue'
import GenreMovieRecommend from '@/components/GenreMovieRecommend.vue'

export default {
  name: 'Home',
  components: {
    RandomRecommend,
    MainMovieRecommend,
    GenreMovieRecommend,
  },
  methods: {
  },
  // created: function () {

  // }
}
</script>
