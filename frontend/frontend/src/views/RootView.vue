<template>
  <div>
    <nav>
      <ul class="nav-links">
        <li class="links">
          <router-link :to="{ name: 'Login' }"> Login </router-link>
        </li>
        <li class="links">
          <router-link :to="{ name: 'SignUp' }"> SignUp </router-link>
        </li>
        <li class="links">
          <router-link :to="{ name: 'About' }"> About </router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: "RootView",
};
</script>

<style scoped>
#nav {
  display: flex;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

.nav-links {
  display: flex;
}

.links {
  padding-right: 20px;
  list-style: none;
}
.links:hover {
  text-decoration: underline;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
