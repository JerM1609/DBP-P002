<template>
  <section>
    <div class="nav">
      <button v-on:click="detect('inicio')" class="head">My page</button>
      <ul class="nav-links">
        <li class="links">
          <button class="name">Post</button>
          <ul class="hidden">
            <li v-for="route in Post" :key="route.id">
              <button v-on:click="detect(route.slug)">
                {{ route.description }}
              </button>
            </li>
          </ul>
        </li>
        <li class="links">
          <button class="name">Course</button>
          <ul class="hidden">
            <li v-for="routes in Course" :key="routes.id">
              <button v-on:click="detect(routes.slug)">
                {{ routes.description }}
              </button>
            </li>
          </ul>
        </li>
      </ul>
      <div class="photo">
        <button v-on:click="detect('profile')" class="photo">
          <img alt="Vue logo" src="../assets/logo.png" />
        </button>
      </div>
    </div>
    <HomeView v-if="page === 'inicio' || page === null" />
    <Post v-else-if="page === 'Post'" :slug="slug" :datas="datas" />
    <Post v-else-if="page === 'MyPost'" :slug="slug" :datas="datas" />
    <Course v-else-if="page === 'Course'" :slug="slug" :datas="datas" />
    <Course v-else-if="page === 'MyCourse'" :slug="slug" :datas="datas" />
    <Form v-else-if="page === 'CreatePost'" :datas="datas" :slug="slug" />
    <Form v-else-if="page === 'CreateCourse'" :datas="datas" :slug="slug" />
    <Profile v-else-if="page === 'profile'" />
  </section>
</template>

<script>
import routes from "@/routes";
import forms from "@/forms";
import Form from "@/views/FormView.vue";
import HomeView from "@/views/HomeView.vue";
import Profile from "@/views/ProfileView.vue";
import Course from "@/views/CourseView.vue";
import Post from "@/views/PostView.vue";
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
  components: {
    Form,
    HomeView,
    Profile,
    Post,
    Course,
  },
  methods: {
    detect(cadena) {
      if (cadena === "post") {
        this.post();
        this.page = "Post";
        this.slug = "post";
      } else if (cadena === "mypost") {
        this.mypost();
        this.page = "MyPost";
        this.slug = "mypost";
      } else if (cadena === "course") {
        this.course();
        this.page = "Course";
        this.slug = "course";
      } else if (cadena === "mycourse") {
        this.mycourse();
        this.page = "MyCourse";
        this.slug = "mycourse";
      } else if (cadena === "createpost") {
        this.createpost();
        this.page = "CreatePost";
        this.slug = "createpost";
      } else if (cadena === "createcourse") {
        this.createcourse();
        this.page = "CreateCourse";
        this.slug = "createcourse";
      } else if (cadena === "inicio") {
        this.page = "inicio";
        this.slug = "inicio";
      } else if (cadena === "profile") {
        this.page = "profile";
        this.slug = "profile";
      }
    },
    mypost() {
      fetch("/api/mypost/", { method: "POST" }).then(
        (response) => (this.datas = response.data)
      );
    },
    post() {
      fetch("/api/showpost/", { method: "POST" }).then(
        (response) => (this.datas = response.data)
      );
    },
    mycourse() {
      fetch("/api/mycourse/", { method: "POST" }).then(
        (response) => (this.datas = response.data)
      );
    },
    course() {
      fetch("/api/courses/", { method: "POST" }).then(
        (response) => (this.datas = response.data)
      );
    },
    createcourse() {
      this.datas = forms.createcourse;
    },
    createpost() {
      this.datas = forms.createpost;
    },
  },
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
