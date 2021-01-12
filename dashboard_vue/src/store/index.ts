import { createStore } from "vuex";
import UserStore from "./UserModule";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    User: UserStore
  },
  getters: {
    loggedIn(state: any) {
      return !!state.user;
    },
  },
});
