<template>
  <div class="loginPage">
    <b-container class="mt-3 mb-5">
      <b-card
        no-body
        class="overflow-hidden mx-auto shadow-lg rounded"
        style="max-width: 850px"
      >
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img
              src="https://picsum.photos/400/400/?image=20"
              alt="Image"
              class="rounded-0"
            ></b-card-img>
          </b-col>
          <b-col md="6">
            <b-card-body title="Masuk">
              <b-alert
                v-model="showDismissibleAlert"
                variant="danger"
                dismissible
                fade
              >
                Username/Password Tidak Sesuai
              </b-alert>
              <b-card-text class="text-left">
                <b-overlay :show="loader" rounded="sm">
                  <b-form class="px-3 mb-4" @submit.prevent="handleSubmit">
                    <b-form-group
                      id="input-group-1"
                      label="Username:"
                      label-for="input-1"
                    >
                      <b-form-input
                        id="inputUsername"
                        type="text"
                        v-model="form.username"
                        placeholder="Username"
                        required
                      ></b-form-input>
                    </b-form-group>

                    <b-form-group
                      id="input-group-2"
                      label="Password:"
                      label-for="input-2"
                    >
                      <b-form-input
                        id="inputPassword"
                        type="password"
                        v-model="form.password"
                        placeholder="Password"
                        required
                      ></b-form-input>
                    </b-form-group>

                    <b-button type="submit" variant="primary" block
                      >Login</b-button
                    >
                  </b-form>
                </b-overlay>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </b-container>
  </div>
</template>

<style scoped>
.loginPage {
  max-height: 100%;
  margin-top: 150px;
}
</style>
<script>
import { mapActions } from "vuex";
import { required, minLength, maxLength } from "vuelidate/lib/validators";

export default {
  name: "Login",
  data() {
    return {
      loader: false,
      form: {
        username: "",
        password: "",
      },
      showDismissibleAlert: false,
    };
  },
  validations: {
    username: {
      required,
      minLength: minLength(1),
      maxLength: maxLength(20),
    },
    password: {
      required,
      minLength: minLength(1),
      maxLength: maxLength(20),
    },
  },
  methods: {
    ...mapActions({ signIn: "auth/signIn" }),
    handleSubmit() {
      this.loader = true;
      const payload = new FormData();
      payload.append("username", this.form.username);
      payload.append("password", this.form.password);
      this.signIn(payload).then(() => {
        this.loader = false;
        this.$router
          .replace({
            name: "Profil",
          })
          .catch(() => {
            this.loader = false;
            this.showDismissibleAlert = true;
            this.form.username = null;
            this.form.password = null;
          });
      });
    },
  },
};
</script>
