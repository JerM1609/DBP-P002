import { authService } from "@/api";

const namespaced = true;

const state = {
  user: {},
  isLoggedIn: false,
};

const getters = {
  isLoggedIn: (state) => state.isLoggedIn,
  user: (state) => state.user,
};

const actions = {
  async registerUser({ dispatch }, user) {
    await authService.post("/register", user);
    await dispatch("fetchUser");
  },
  async loginUser({ commit }, user) {
    await authService.post("/sign-up", user).then((response) => {
      console.log("response: ", response);
      commit("setUser", response["data"]);
    });
  },
  async logoutUser({ commit }) {
    await authService.post("/logout");
    commit("logoutUserState");
  },
};

const mutations = {
  setUser(state, user) {
    console.log(user);
    state.isLoggedIn = true;
    state.user = user;
    localStorage.setItem("user", JSON.stringify(state.user));
    sessionStorage.setItem("user", JSON.stringify(state.user));
  },
  logoutUserState(state) {
    state.isLoggedIn = false;
    state.user = {};
  },
};

export default {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};
