import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "../views/Login.vue";
import store from "../store";
import Dashboard from "../views/Dashboard.vue";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/search",
    name: "Search",
    component: () => import("../views/Search.vue"),
  },
  {
    path: "/course",
    name: "Course",
    component: () => import("../views/Course.vue"),
    // component: Course,
  },
  {
    path: "/signIn",
    name: "Sign In",
    component: Login,
  },
  {
    path: "/profil",
    name: "Profil",
    component: () => import("../views/Profile.vue"),
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    (to.name === "Dashboard" || to.name === "Profil") &&
    !store.getters["auth/authenticated"]
  )
    return next({ name: "Sign In" });
  else {
    next();
  }
  if (
    to.name === "Dashboard" &&
    store.getters["auth/authenticated"].role !== "Admin"
  )
    return next({ name: "Profil" });
});

export default router;
