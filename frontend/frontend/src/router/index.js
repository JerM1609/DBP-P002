import { createRouter, createWebHistory } from "vue-router";
import RootView from "../views/RootView.vue";
import SignUp from "../components/SignUpForm.vue";
import Login from "../components/LoginForm.vue";
import Dashboard from "../views/DashboardView.vue";

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
    name: "Dashboard",
    props: true,
    component: Dashboard,
  },
  {
    path: "/post/:slug",
    name: "Post",
    props: true,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/PostView.vue"),
  },
  {
    path: "/profile/:name",
    name: "Profile",
    props: true,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ProfileView.vue"),
  },
  {
    path: "/create/:slug",
    name: "Create",
    props: true,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/PostView.vue"),
  },
  {
    path: "/edit/:slug/:Id",
    name: "Change",
    props: true,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/PostView.vue"),
  },
  {
    path: "/course/:slug",
    name: "Course",
    props: true,
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/CourseView.vue"),
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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
