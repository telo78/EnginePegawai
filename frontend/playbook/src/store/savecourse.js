import axios from "axios";

export default {
  namespaced: true,
  state: {
    courses: [],
  },
  getters: {
    result(state) {
      return state.courses;
    },
  },
  mutations: {
    SET_COURSE(state, data) {
      state.courses = data;
    },
  },
  actions: {
    async getdata({ commit }, input) {
      let query = "http://localhost:8000/course/savecourse/" + input;
      let response;
      try {
        response = await axios.get(query);
        commit("SET_COURSE", response.data);
      } catch (e) {
        return;
      }
      return response;
    },
  },
};
