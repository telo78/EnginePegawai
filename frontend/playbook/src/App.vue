<template>
  <div id="app">
    <template v-if="getCurrentRoute !== 'Dashboard'">
      <Navbar />
    </template>

    <router-view />
    <template
      v-if="
        getCurrentRoute !== 'Sign In' &&
        getCurrentRoute !== 'Profil' &&
        getCurrentRoute !== 'Dashboard'
      "
    >
      <Footer />
    </template>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";

export default {
  components: { Navbar, Footer },
  computed: {
    getCurrentRoute() {
      return this.$route.name;
    },
  },
};
</script>
