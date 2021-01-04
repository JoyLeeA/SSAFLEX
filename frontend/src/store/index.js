import Vue from 'vue'
import Vuex from 'vuex'
import VueCarousel from 'vue-carousel';
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)
Vue.use(VueCarousel);

// const API_KEY = process.env.VUE_APP_MOVIE_API_KEY

export default new Vuex.Store({
  state: {
    popularMovies: [],
    mainOn: true,
    login: false,
    currentMovie: {},
    genres: [],
    selectedGenreId: '',
  },
  getters : {

  },
  mutations: {
    GET_POPULAR_MOVIES: function (state, movies) {
      state.popularMovies = movies
      state.popularMovies = _.sortBy(state.popularMovies, ['userRating', 'pubDate']).reverse()
    },
    MOVE_TO_DETAIL: function (state, movie) {
      state.currentMovie = movie
    },
    GET_GENRES: function (state, genres) {
      state.genres = genres
    },
    MAIN_CHANGE: function (state) {
      state.mainOn = !state.mainOn
    },
    LOGOUT: function (state) {
      state.login = false
    },
    LOGIN: function (state) {
      state.login = true
    }
  },
  actions: {
    getPopularMovies: function ({ commit }) {
      axios.get('http://127.0.0.1:8000/movies/list')
      .then((res) => {
        commit('GET_POPULAR_MOVIES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    moveToDetail: function ({ commit }, movie) {
      commit('MOVE_TO_DETAIL', movie)
    },
    getGenres: function ({ commit }) {
      axios.get('http://127.0.0.1:8000/movies/genres')
      .then((res) => {
        // console.log(res.data)
        commit('GET_GENRES', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    mainChange: function ({ commit }) {
      commit('MAIN_CHANGE')
    },
    logout: function ({ commit }) {
      commit('LOGOUT')
    },
    login: function ({ commit }) {
      commit('LOGIN')
    }
  },
})
