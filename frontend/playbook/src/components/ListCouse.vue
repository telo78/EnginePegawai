<template>
  <b-col md="4" class="d-flex pb-3">
    <b-card :img-src="image" img-alt="Image" img-top tag="article">
      <a v-bind:href="url" style="color: black">
        <b-card-title title-tag="h6" class="text-left font-weight-bold">{{
          name
        }}</b-card-title>
      </a>
      <p class="text-left" id="custext">{{ author }}</p>
      <p class="text-left" id="custpro">{{ provider }}</p>
      <template #footer v-if="user">
        <div v-if="!show && !check">
          <b-overlay
            :show="busy"
            rounded
            opacity="0.6"
            spinner-small
            spinner-variant="primary"
            class="d-inline-block"
            @hidden="onHidden"
          >
            <b-button
              ref="button"
              :disabled="busy"
              variant="primary"
              size="sm"
              @click="onClickInsert"
            >
              <i class="fa fa-folder mr-1"></i>
              Save
            </b-button>
          </b-overlay>
        </div>
        <div v-else>
          <b-overlay
            :show="busy"
            rounded
            opacity="0.6"
            spinner-small
            spinner-variant="success"
            class="d-inline-block"
            @hidden="onHidden"
          >
            <b-button
              ref="button"
              :disabled="busy"
              variant="success"
              size="sm"
              @click="onClickDelete"
            >
              <i class="fa fa-minus-square mr-1"></i>
              Unsave
            </b-button>
          </b-overlay>
        </div>
      </template>
    </b-card>
  </b-col>
</template>

<style scoped>
.card {
  transition: transform 0.4s;
  border-radius: 0.8rem;
}

.card:hover {
  box-shadow: 0 5px 32px 0 rgba(95, 101, 192, 0.144);
  transform: scale(1.1);
}
.customcard {
  padding: 0.85rem;
}
#custext {
  font-size: 12px;
  line-height: 4px;
}
#custpro {
  font-size: 12px;
  line-height: 6px;
  font-weight: 800;
  color: #4141a5;
}
</style>
<script>
import axios from "axios";
export default {
  name: "ListCourse",
  props: ["name", "image", "provider", "author", "url", "id", "user", "check"],
  data() {
    return {
      busy: false,
      show: false,
    };
  },

  methods: {
    onHidden() {
      // Return focus to the button once hidden
      this.$refs.button.focus();
    },
    onClickInsert() {
      let payloadIns = { courseId: this.id, userId: this.user.id };
      this.busy = true;
      this.procdata("insert", payloadIns).then(() => {
        this.busy = false;
        this.show = true;
      });
    },
    onClickDelete() {
      let payloadDel = { courseId: this.id, userId: this.user.id };
      this.busy = true;
      this.procdata("delete", payloadDel).then(() => {
        this.busy = false;
        this.show = false;
        this.check = false;
      });
    },
    async procdata(tags, data) {
      let response;
      try {
        if (tags === "insert") {
          response = await axios.post(
            "http://localhost:8000/course/savecourse/insert/",
            data
          );
        } else {
          response = await axios.post(
            "http://localhost:8000/course/savecourse/delete/",
            data
          );
        }
      } catch (e) {
        return;
      }
      return response;
    },
  },
};
</script>
