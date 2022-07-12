<template>
  <section>
    <div class="nav">
      <p class="logo">UTEChana App</p>
      <router-link to="/dashboard">
        <button @click="detect('inicio')" class="head">Dashboard</button>
      </router-link>
      <ul class="nav-links">
        <li class="links">
          <div class="dropdown">
            <button class="name">Posts</button>
            <div class="dropdown-content">
              <a v-for="route in Post" :key="route.id">
                <router-link
                  :to="{ name: route.name, params: { slug: route.slug } }"
                  >{{ route.description }}</router-link
                >
              </a>
            </div>
          </div>
        </li>
        <li class="links">
          <div class="dropdown">
            <button class="name">Cursos</button>
            <div class="dropdown-content">
              <a v-for="route in Course" :key="route.id">
                <router-link
                  :to="{ name: route.name, params: { slug: route.slug } }"
                  >{{ route.description }}</router-link
                >
              </a>
            </div>
          </div>
        </li>
      </ul>
      <div class="photo">
        <router-link :to="{ name: 'Profile', params: { idUser: this.idUser } }">
          <img alt="Vue logo" src="../assets/logo.png"
        /></router-link>
      </div>
    </div>
  </section>
</template>

<script>
import routes from "@/routes";
export default {
  name: "TheNavigation",
  data() {
    return {
      idUser: sessionStorage.key(0),
      Post: routes.Post,
      Course: routes.Course,
      datas: null,
      page: null,
      slug: null,
    };
  },
  methods: {},
};
</script>

<style scoped>
/* Navbar container */
.navbar {
  overflow: hidden;
  background-color: #333;
  font-family: Arial;
}

/* Links inside the navbar */
.navbar a {
  float: left;
  font-size: 16px;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* The dropdown container */
.dropdown {
  float: left;
  overflow: hidden;
}
/* Dropdown content (hidden by default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}
.nav {
  display: flex;
  width: 100%;
  height: 50px;
  border-radius: 10px;
  background-color: #a2c841;
}

.nav a {
  font-weight: bold;
  color: #2c3e50;
}

.nav a.router-link-exact-active {
  color: #42b983;
}

.nav-links {
  display: flex;
  width: 91%;
  padding: 0%;
}

.links {
  width: 10%;
  list-style: none;
}

.head {
  width: 10%;
}

.photo {
  height: 100%;
  width: 3%;
}
img {
  height: calc(100% - 4px);
  border: 2px solid black;
  border-radius: 50%;
}
.name {
  font-weight: bold;
  color: #2c3e50;
  font-size: 20px;
  padding: 0%;
  margin: 0%;
  background-color: transparent;
  border: 0px;
}
.hidden {
  margin-top: 15px;
}
.name ~ .hidden {
  display: none;
}
.name:focus ~ .hidden {
  display: block;
}
.hidden:hover {
  display: block;
}
</style>
