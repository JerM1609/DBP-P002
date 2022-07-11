import { createStore } from "vuex";

export default createStore({
  state: {
    Usuario: Object(),
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
