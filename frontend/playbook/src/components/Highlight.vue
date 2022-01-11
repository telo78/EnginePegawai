<template>
  <div class="highlight mb-5">
    <b-jumbotron class="overlay text-white">
      <div class="row mt-5">
        <div class="col-md-12">
          <h1 class="mt-5" id="typing">Pilih Kursus Sesuai</h1>
          <h2 class="mb-5">dengan keinginanmu</h2>
          <div class="row">
            <div class="col-md-12">
              <b-form
                inline
                class="justify-content-center"
                @submit.prevent="handleSubmit"
              >
                <label class="sr-only" for="inline-form-input-name">Name</label>
                <b-form-input
                  id="inline-form-input-name"
                  size="lg"
                  v-model="form.inputdata"
                  class="mb-2 mr-sm-2 mb-sm-0"
                  placeholder="Kata Pencarian..."
                ></b-form-input>

                <b-button variant="primary" size="lg" type="submit">
                  <b-icon
                    icon="search"
                    aria-hidden="true"
                    shift-v="1"
                    scale=".75"
                    class="mr-1"
                  ></b-icon
                  >Cari</b-button
                >
              </b-form>
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-md-12">
              <p>atau pilih berdasarkan kategori</p>
            </div>
          </div>
        </div>
      </div>
    </b-jumbotron>
  </div>
</template>

<style scoped>
.overlay {
  background: rgb(255, 255, 255);
  background: linear-gradient(
    0deg,
    rgba(255, 255, 255, 1) 2%,
    rgba(139, 138, 137, 0.1922969871542367) 38%,
    rgba(78, 78, 78, 0.5592437658657212) 81%,
    rgba(0, 0, 0, 0.648879620207458) 100%
  );
  height: inherit;
}
.highlight {
  background-image: url("../assets/img/bg-cover.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  height: 650px;
}

.overlay h1 {
  font-size: 70px;
  font-weight: 700;
}
</style>
<script>
import { mapActions } from "vuex";
export default {
  name: "Highlight",
  data() {
    return {
      form: {
        inputdata: "",
      },
    };
  },
  methods: {
    ...mapActions({ getdata: "search/getdata" }),
    handleSubmit() {
      this.getdata(this.form.inputdata);
      this.$router.replace("Search");
    },
  },
};
</script>
