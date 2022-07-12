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
    console.log("user: ", user);
    await authService.post("/log-in", user).then((response) => {
      console.log("response: ", response);
      commit("setUser", response["data"]);
    });
  },
  async signUser({ commit }, user) {
    await authService.post("/sign-up", user).then((response) => {
      console.log("response: ", response);
      commit("setUser", response["data"]);
    });
  },
  async updateUser({ commit }, user /*var*/) {
    console.log(user);
    let token = JSON.parse(sessionStorage.getItem("antonio")); //idUser
    token = token["user"];
    await authService
      .patch("/editar-perfil/", { antigua: token, nueva: user })
      .then((response) => {
        console.log("response: ", response["data"]);
        commit("setUser", response["data"]);
      });
  },
  //crear funciones
  async createCourse({ commit }, course) {
    console.log(course);
    await authService.post("/creation_cursos", course).then((response) => {
      console.log("response: ", response["data"]);
      commit("setUser", response["data"]);
    });
  },
  // async createPost({ commit }, user) {},
  async logoutUser({ commit }, user) {
    await authService.post("/logout");
    localStorage.removeItem(user);
    sessionStorage.removeItem(user);
    commit("logoutUserState");
  },
};

const mutations = {
  setUser(state, user) {
    console.log("user");
    console.log(user);
    state.isLoggedIn = true;
    state.user = user;
    state.accessToken = user["access_token"];
    console.log("access_token");
    console.log(state.accessToken);
    localStorage.setItem(user["user"]["username"], JSON.stringify(state.user)); //se puede ovbiar
    sessionStorage.setItem(
      user["user"]["username"],
      JSON.stringify(state.user)
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
