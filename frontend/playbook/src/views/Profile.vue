<template>
  <div class="container rounded bg-white mt-5 mb-5">
    <div class="row">
      <div class="col-md-3 border-right">
        <div class="d-flex flex-column align-items-center text-center p-3 py-5">
          <img
            class="rounded-circle mt-5"
            src="../assets/default_profile.png"
            width="90"
          /><span class="font-weight-bold mt-2">{{ user.username }}</span
          ><span class="text-black-50">{{ user.email }}</span
          ><span>Kementerian Sekretariat Negara</span>

          <div class="mt-5" v-if="user.role === 'Admin'">
            <b-badge variant="success" pill
              ><a href="/dashboard" style="color: white" class="btn">
                Dashboard</a
              ></b-badge
            >
          </div>
        </div>
      </div>
      <div class="col-md-5 border-right">
        <div class="p-3 py-5 text-left">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h6 class="text-right">Edit your profile</h6>
          </div>
          <div class="row mt-2">
            <div class="col-md-12">
              <label class="labels">Name</label
              ><input
                type="text"
                class="form-control"
                :value="user.username"
                disabled
              />
            </div>
          </div>
          <div class="row mt-3">
            <div class="col-md-12">
              <label class="labels">Email</label
              ><input
                type="text"
                class="form-control"
                :value="user.email"
                disabled
              />
            </div>
            <div class="col-md-12 mt-3">
              <label class="labels">Role</label
              ><input
                type="text"
                class="form-control"
                :value="user.role"
                disabled
              />
            </div>
            <div class="col-md-12 mt-3">
              <label class="labels">Status</label>
              <br />
              <span
                v-if="user.status === 1"
                class="badge badge-pill badge-primary"
                >Active</span
              >
              <span v-else class="badge badge-pill badge-danger">Inactive</span>
            </div>
          </div>
          <div class="mt-5 text-center">
            <button class="btn btn-primary profile-button" type="button">
              Edit Profile
            </button>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="p-3 py-5">
          <div
            class="d-flex justify-content-between align-items-center experience"
          >
            <span
              >My Course
              <b-badge variant="success">{{ result.length }}</b-badge></span
            >
          </div>
          <div class="scrolltab">
            <div class="cardHis" v-for="i in result" :key="i.id">
              <div class="d-flex flex-row mt-3 exp-container text-left">
                <img :src="i.courses.image" width="45" height="45" />
                <div class="work-experience ml-1">
                  <a
                    :href="i.courses.url"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <span class="font-weight-bold d-block">{{
                      i.courses.title
                    }}</span>
                  </a>
                  <span class="d-block text-black-50 labels">{{
                    i.courses.providers.name
                  }}</span>
                </div>
              </div>
              <hr />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.scrolltab {
  height: 400px;
  overflow-y: scroll;
}
</style>
<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Profile",
  computed: {
    ...mapGetters({
      user: "auth/user",
      result: "savecourse/result",
    }),
  },
  created() {
    this.handledata();
  },
  methods: {
    ...mapActions({ getdata: "savecourse/getdata" }),
    handledata() {
      const respon = this.getdata(this.user.id);
      return respon;
    },
  },
};
</script>
