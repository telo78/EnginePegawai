import Vue from "vue";
import App from "./App.vue";
import "./plugins/bootstrap-vue";
import router from "./router";
import Vuelidate from "vuelidate";
import store from "./store";
import "./assets/styles/app.css";
require("./store/subcriber");

Vue.config.productionTip = false;
store.dispatch("auth/attempt", localStorage.getItem("token")).then(() => {
  new Vue({
    router,
    store,
    Vuelidate,
    render: (h) => h(App),
  }).$mount("#app");
});
