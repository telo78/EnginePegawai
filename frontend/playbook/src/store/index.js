import Vue from "vue";
import Vuex from "vuex";
import auth from "./auth";
import search from "./search";
import savecourse from "./savecourse";
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  plugins: [createPersistedState()],
  mutations: {},
  actions: {},
  modules: { auth, search, savecourse },
});
