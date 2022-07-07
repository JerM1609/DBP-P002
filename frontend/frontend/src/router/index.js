import { createRouter, createWebHistory } from "vue-router";
import RootView from "../views/RootView.vue";
import SignUp from "../views/SignUp.vue";
import Login from "../views/Login.vue";
import TheNavigation from "../components/TheNavigation.vue";

// URLS are mapped to the components
const routes = [
  {
    path: "/",
    name: "RootView",
    component: RootView,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/dashboard",
    name: "TheNavigation",
    props: true,
    component: TheNavigation,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/log-in",
    name: "Login",
    component: Login,
  },
  {
    path: "/post/:slug",
    name: "Post",
    props: true,
    component: () =>
      import(/* webpackChunkName: "Post" */ "../views/PostView.vue"),
  },
  {
    path: "/course/:slug",
    name: "Course",
    props: true,
    component: () =>
      import(/* webpackChunkName: "Course" */ "../views/CourseView.vue"),
  },
  {
    path: "/profile/:prof",
    name: "Profile",
    component: () =>
      import(/* webpackChunkName: "Profile" */ "../views/ProfileView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
