import { createRouter, createWebHashHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Example from "../components/Example.vue";
import SignUpForm from "../components/SignUpForm.vue";
import LoginForm from "../components/LoginForm.vue";

// URLS are mapped to the components
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/example",
    name: "Example",
    component: Example,
  },
  {
    path: "/sign-up",
    name: "SignUpForm",
    component: SignUpForm,
  },
  {
    path: "/log-in",
    name: "LoginForm",
    component: LoginForm,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
