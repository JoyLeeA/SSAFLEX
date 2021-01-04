<template>
  <div>
    <b-button right="true" class="sideBar" v-b-toggle.sidebar-right>메뉴</b-button>
    <b-sidebar id="sidebar-right" bg-variant="dark" text-variant="light" right shadow>
      <template #default="{ hide }">
        <div class="p-3 text-left">
          <h4 v-if="mainOn" id="sidebar-right-title">SSAFLIX</h4>
          <h4 v-if="!mainOn" id="sidebar-right-title">SSAMUNITY</h4>
          <b-navbar toggleable="lg" type="dark" variant="">
            <b-navbar-toggle target="nav_collapse"/>

            <b-collapse is-nav id="nav_collapse">
              <b-navbar-nav>
                <b-nav vertical>
                  <b-nav-item v-if="!mainOn" :to="{ name: 'Fake' }">공지사항</b-nav-item>
                  <b-nav-item v-if="!mainOn" :to="{ name: 'Board' }">자유게시판</b-nav-item>
                  <b-nav-item  :to="{ name: 'Signup' }">회원가입</b-nav-item>
                  <b-nav-item  :to="{ name: 'Login' }">로그인</b-nav-item>
                  <b-nav-item  @click.native="logoutt" :to="{ name: 'Login' }">로그아웃</b-nav-item>
                </b-nav>
                <!-- <b-nav-item href="#">공지사항</b-nav-item>
                <b-nav-item to="/board/free">자유게시판</b-nav-item>
                <router-link @click.native="logout" to="#">Logout</router-link>
                <b-nav-item @click.native="logout" to="#">로그아웃</b-nav-item>
                <b-nav-item :to="{ name: 'Signup' }">회원가입</b-nav-item>
                <b-nav-item :to="{ name: 'Login' }">로그인</b-nav-item> -->
              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
          <b-button variant="dark" block @click="hide">Close Sidebar</b-button>
        </div>
      </template>
    </b-sidebar>
    <!-- <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="#">Vue.js로 게시판 만들기</b-navbar-brand>

      <b-navbar-toggle target="nav_collapse"/>

      <b-collapse is-nav id="nav_collapse">
        <b-navbar-nav>
          <b-nav-item href="#">공지사항</b-nav-item>
          <b-nav-item to="/board/free">자유게시판</b-nav-item>
          <router-link @click.native="logout" to="#">Logout</router-link>
          <b-nav-item @click.native="logout" to="#">로그아웃</b-nav-item>
          <b-nav-item :to="{ name: 'Signup' }">회원가입</b-nav-item>
          <b-nav-item :to="{ name: 'Login' }">로그인</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar> -->
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Community',
  data: function () {
    return {
    }
  },
  methods: {
    logoutt: function () {
      localStorage.removeItem('jwt')
      // this.$store.state.login = false
      this.$store.dispatch('logout')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.$store.dispatch('login')
      // this.$store.state.login = true
    }
  },
  computed: {
    ...mapState([
      'mainOn',
      'login',
    ])
  }
}
</script>

<style scoped>
  nav {
    color:white;
  }
  
  .sideBar:hover {
    transition: .5s ease;
    right: 0;
  }

  .sideBar {
    position: absolute; 
    right: -80px;
    transition: 0.3s;
    padding: 5px;
    width: 150px;
    text-decoration: none;
    font-size: 20px;
    color: white;
    /* border-radius: 0 5px 5px 0; */
    top: 200px;
    background-color: #1dc278;
  }
</style>