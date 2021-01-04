import Vue from 'vue'
import VueRouter from 'vue-router'
// Movie
import Home from '../views/Home.vue'
import MovieDetail from '@/views/MovieDetail.vue'
// Community
import Community from '@/views/Community.vue'
import Board from '@/views/Board'
import ContentDetail from '@/views/ContentDetail';
import Create from '@/views/Create';
// Login
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Fake from '@/views/Fake'
// import Movie from '@/views/Movie.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/fake',
    name: 'Fake',
    component: Fake
  },
  {
    path: '/movie-detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/board/free',
    name: 'Board',
    component: Board
  },
  {
    path: '/board/free/detail/:contentId',
    name: 'ContentDetail',
    component: ContentDetail
  },
  {
    path: '/board/free/create/:contentId?',
    name: 'Create',
    component: Create
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  // {
  //   path: '/movie',
  //   name: 'Movie',
  //   component: Movie
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
