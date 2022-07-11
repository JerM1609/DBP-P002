import { createStore } from "vuex";
import auth from "./modules/auth";

export default createStore({
  state: {
    Usuario: Object(),
  },
  modules: {
    auth,
  },
  mutations: {
    set_user(state) {
      state.Usuario = state;
    },
  },

  actions: {
    commit_user(state) {
      state.commit("set_user");
    },
  },
  getters: {
    user(state) {
      return state.Usuario;
    },
  },
});
