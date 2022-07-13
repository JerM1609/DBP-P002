<template>
  <TheNavigation v-if="isLoggedIn" />
  <router-view />
</template>

<script>
import TheNavigation from "./components/TheNavigation.vue";

export default {
  name: "App",
  components: { TheNavigation },
  computed: {
    isLoggedIn() {
      return (
        this.$route.name !== "Login" &&
        this.$route.name !== "SignUp" &&
        this.$route.name !== "RootView" &&
        this.$route.name !== "About"
      );
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
html {
  background-color: #c2c2fe;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
