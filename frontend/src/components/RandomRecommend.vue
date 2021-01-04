<template>
  <div class="mb-5">
      <img @click="randomPick"
      class="capImg" src="@/assets/potter_cap.png">
      <br>
      <h1 @click="randomPick" class="text-white">오늘의 추천</h1>
      <br>
      <br>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import _ from 'lodash'

export default {
    name: 'RandomRecommend',
    methods: {
        randomPick: function () {
            const pickedIdx = _.random(this.popularMovies.length)
            this.$store.dispatch('moveToDetail', this.popularMovies[pickedIdx])
            this.$router.push('/movie-detail')
        }
    },
    computed: {
        ...mapState([
            'popularMovies',
        ])
    },
}
</script>

<style>
    .capImg {
        opacity: 1;
        width: 75%;
        height: auto;
        transition: .5s ease;
    }

    .capImg:hover {
        transform: scale(1.2);
    }
</style>