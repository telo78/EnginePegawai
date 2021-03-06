import axios from "axios";

export default {
  namespaced: true,
  state: {
    token: null,
    user: null,
  },
  getters: {
    authenticated(state) {
      return state.token && state.user;
    },
    user(state) {
      return state.user;
    },
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token;
    },
    SET_USER(state, data) {
      state.user = data;
    },
  },
  actions: {
    async signIn({ dispatch }, credentials) {
      let response;
      try {
        response = await axios.post(
          "http://localhost:8000/login/",
          credentials
        );
      } catch (e) {
        return;
      }
      if (response.status !== 404)
        return dispatch("attempt", response.data.access_token);
    },

    async attempt({ commit, state }, token) {
      if (token) {
        commit("SET_TOKEN", token);
      }
      if (!state.token) {
        return;
      }
      try {
        let response = await axios.get("http://localhost:8000/login/me");
        commit("SET_USER", response.data);
      } catch (e) {
        commit("SET_TOKEN", null);
        commit("SET_USER", null);
      }
    },

    signOut({ commit }) {
      commit("SET_TOKEN", null);
      commit("SET_USER", null);
    },
  },
};
