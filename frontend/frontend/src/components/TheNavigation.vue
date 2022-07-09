<template>
  <section>
    <div class="nav">
      <button v-on:click="detect('inicio')" class="head">My page</button>
      <ul class="nav-links">
        <li class="links">
          <button class="name">Post</button>
          <ul class="hidden">
            <li v-for="route in Post" :key="route.id">
              <router-link
                :to="{ name: route.name, params: { slug: route.slug } }"
                >{{ route.description }}</router-link
              >
            </li>
          </ul>
        </li>
        <li class="links">
          <button class="name">Course</button>
          <ul class="hidden">
            <li v-for="route in Course" :key="route.id">
              <router-link
                :to="{ name: route.name, params: { slug: route.slug } }"
                >{{ route.description }}</router-link
              >
            </li>
          </ul>
        </li>
      </ul>
      <div class="photo">
        <router-link :to="{ name: 'Profile', params: { name: 'a' } }">
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
      Post: routes.Post,
      Course: routes.Course,
      datas: null,
      page: null,
      slug: null,
    };
  },
  props: {
    profile: {
      type: String,
      require: true,
    },
  },
  methods: {},
};
</script>
<style scoped>
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
  width: 5%;
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
