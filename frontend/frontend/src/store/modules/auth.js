import { authService } from "@/api";

const namespaced = true;

const state = {
  user: {},
  accessToken: null,
  isLoggedIn: false,
};

const getters = {
  isLoggedIn: (state) => state.isLoggedIn,
  user: (state) => state.user,
};

const actions = {
  async loginUser({ commit }, user) {
    await authService.post("/log-in", user).then((response) => {
      console.log("response: ", response);
      commit("setUser", response);
    });
  },
  async signUser({ commit }, user) {
    await authService.post("/sign-up", user).then((response) => {
      console.log("response: ", response);
      commit("setUser", response);
    });
  },
  async logoutUser({ commit }) {
    await authService.post("/logout");
    localStorage.removeItem("user");
    sessionStorage.removeItem("user");
    commit("logoutUserState");
  },
};

const mutations = {
  setUser(state, user) {
    //user = response
    console.log("user");
    console.log(user);
    state.isLoggedIn = true;
    state.user = user["data"]["user"];
    state.accessToken = user["data"]["access_token"];
    localStorage.setItem(
      user["data"]["user"]["username"],
      JSON.stringify(user)
    );
    sessionStorage.setItem(
      user["data"]["user"]["username"],
      JSON.stringify(user)
    );
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
