<template>
  <div id="app">
    <div id="nav" class="my-5">
      <router-link v-if="mainOn" class="display-1" :to="{ name: 'Home'}">SSAFLIX</router-link>
      <div @click="mainChange" v-if="mainOn" class="sideNav">
        <router-link  class="text-white sideBtn" :to="{ name: 'Community'}">SSAMUNITY</router-link>
      </div>
      <router-link v-if="!mainOn" class="display-1" :to="{ name: 'Community'}">SSAMUNITY</router-link>
      <div @click="mainChange" v-if="!mainOn" class="sideNav">
        <router-link  class="text-white sideBtn" :to="{ name: 'Home'}">SSAFLIX</router-link>
      </div>
      <!-- <router-link class="ml-auto" :to="{ name:'Movie' }">Movie</router-link> -->
    </div>
    <Community />
    <router-view/>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Community from '@/views/Community'

export default {
  name: 'App',
  data: function () {
    return {

    }
  },
  components: {
    Community,
  },
  methods: {
    mainChange: function () {
      console.log('change')
      this.$store.dispatch('mainChange')
    }
  },
  computed: {
    ...mapState([
      'mainOn',
    ])
  }
}
</script>

<style>
body {
  height: 100%;
  margin: 0;
  min-height: 100%;
  background-color: rgb(0, 0, 0);
  background-repeat: no-repeat;
  background-size: cover;
  color: #1dc278;
  padding-bottom: 200px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  font-size: 30px;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #1dc278;
}

#nav a.router-link-exact-active {
  color: #1dc278;
}

.sideBtn:hover {
  transition: .5s ease;
  left:0;
}

.sideBtn {
  position: absolute; 
  left: -80px;
  transition: 0.3s;
  padding: 5px;
  width: 150px;
  text-decoration: none;
  font-size: 20px;
  color: white;
  border-radius: 0 5px 5px 0;
  top: 200px;
  background-color: #1dc278;
}

footer {
  position:fixed;
  left: 0;
  bottom:0;
  margin-top: -1.7em;
  width:100%;
  height:1.7em;
  color: white;
  background: #1dc278;
}
</style>
