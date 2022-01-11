<template>
  <b-navbar toggleable="lg" type="dark" variant="dark" fixed sticky>
    <b-navbar-brand href="#">
      <img
        src="../assets/logo.png"
        alt="logo playbook"
        width="30px"
        height="30px"
        class="mr-1"
      />
      Playbook</b-navbar-brand
    >
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item v-for="i in rt" :key="i.id" :to="i.path">
          <b-icon
            v-bind:icon="i.name === 'Home' ? 'house' : 'columns'"
            aria-hidden="true"
            scale=".75"
            shift-v="1"
            class="mr-1"
          ></b-icon>
          {{ i.name }}</b-nav-item
        >
      </b-navbar-nav>
      <b-dropdown-divider class="d-block d-sm-none" />
      <!-- Right aligned nav items -->

      <b-navbar-nav class="ml-auto" v-if="authenticated">
        <b-nav-item to="/profil">
          <b-icon
            icon="person"
            aria-hidden="true"
            shift-v="1"
            scale=".75"
            class="mr-1"
          ></b-icon
          >Profil</b-nav-item
        >
        <b-nav-item @click.prevent="signOuts" to="/home">
          <b-icon
            icon="power"
            aria-hidden="true"
            shift-v="1"
            scale=".75"
            class="mr-1"
          ></b-icon>
          Sign Out
        </b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="ml-auto" v-else>
        <b-nav-item to="/signIn">
          <b-icon
            icon="person"
            aria-hidden="true"
            shift-v="1"
            scale=".75"
            class="mr-1"
          ></b-icon
          >Sign In</b-nav-item
        >
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "Navbar",
  mounted() {
    this.rt = this.$router.options.routes;
    this.removeDataNav(this.rt);
  },
  data() {
    return {
      rt: null,
      normal: ["Sign In", "Profil", "Dashboard", "Search"],
    };
  },
  computed: {
    ...mapGetters({
      authenticated: "auth/authenticated",
      user: "auth/user",
    }),
  },
  methods: {
    ...mapActions({
      signOut: "auth/signOut",
    }),
    removeDataNav(datas) {
      let temp = datas.slice(0);
      temp.forEach((element) => {
        if (this.normal.includes(element["name"])) {
          let removeind = datas
            .map((item) => item["name"])
            .indexOf(element["name"]);
          datas.splice(removeind, 1);
        }
      });
    },
    signOuts() {
      this.signOut().then(() => {
        this.$router
          .replace({
            name: "Home",
          })
          .catch((e) => {
            console.log(e);
          });
      });
    },
  },
};
</script>
