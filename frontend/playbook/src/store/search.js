import axios from "axios";

export default {
  namespaced: true,
  state: {
    searchres: [],
  },
  getters: {
    result(state) {
      return state.searchres;
    },
  },
  mutations: {
    SET_SEARCH(state, data) {
      state.searchres = data;
    },
  },
  actions: {
    async getdata({ commit }, input) {
      let query = "http://localhost:8000/course/search/?query=" + input;
      let response;
      try {
        response = await axios.get(query);
        commit("SET_SEARCH", response.data);
      } catch (e) {
        return;
      }
    },
  },
};
