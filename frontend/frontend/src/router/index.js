import { createRouter, createWebHistory } from "vue-router";
import RootView from "../views/RootView.vue";
import SignUp from "../views/SignUp.vue";
import Login from "../views/Login.vue";
import Dashboard from "../views/DashboardView.vue";

// URLS are mapped to the components
const routes = [
  {
    path: "/",
    name: "RootView",
    component: RootView,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    props: true,
    component: Dashboard,
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
    path: "/profile/:idUser",
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
      import(/* webpackChunkName: "about" */ "../views/FormView.vue"),
  },
  {
    path: "/course/:slug",
    name: "Course",
    props: true,
    component: () =>
      import(/* webpackChunkName: "CourseView" */ "../views/CourseView.vue"),
  },
  {
    path: "/post/:slug",
    name: "Post",
    props: true,
    component: () =>
      import(/* webpackChunkName: "PostView" */ "../views/PostView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
