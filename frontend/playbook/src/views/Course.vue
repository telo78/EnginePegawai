<template>
  <b-container>
    <b-row class="mt-5">
      <b-col md="4">
        <FilterCourse v-model="filter" />
        <FilterProviderCourse v-model="filterPro" />
      </b-col>
      <b-col md="8">
        <div class="py-2 px-2 viewChange mb-3 text-right">
          <b-form-checkbox v-model="show" name="check-button" switch>
            <b>{{ show ? "Table" : "Card" }}</b>
          </b-form-checkbox>
        </div>

        <transition name="slide-fade" mode="out-in">
          <b-skeleton-wrapper :loading="loading" v-if="show" key="mode1">
            <template #loading>
              <b-row>
                <b-col>
                  <b-card class="mb-5">
                    <b-skeleton-table
                      :rows="10"
                      :columns="4"
                      :table-props="{ bordered: true, striped: true }"
                    ></b-skeleton-table>
                  </b-card>
                </b-col>
              </b-row>
            </template>
            <b-row>
              <RowCourse :items="courses['data']" />
            </b-row>
          </b-skeleton-wrapper>
          <b-skeleton-wrapper :loading="loading" v-else key="mode2">
            <template #loading>
              <b-row>
                <b-col md="4" v-for="i in 6" :key="i.id">
                  <b-card class="mb-5">
                    <b-skeleton width="85%"></b-skeleton>
                    <b-skeleton width="55%"></b-skeleton>
                    <b-skeleton width="70%"></b-skeleton>
                  </b-card>
                </b-col>
              </b-row>
            </template>
            <b-row>
              <ListCourse
                v-for="course in courses['data']"
                :key="course.id"
                :name="course.title"
                :image="course.image"
                :provider="course.providers.name"
                :author="course.instructors"
                :url="course.url"
                :id="course.id"
                :user="user"
                :check="course.check"
              />
            </b-row>
          </b-skeleton-wrapper>
        </transition>
        <b-row>
          <b-col v-if="!loading">
            <b-pagination
              align="center"
              pills
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              @change="handleClick"
            ></b-pagination>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>
<style scoped>
.slide-fade-enter-active {
  transition: all 0.19s ease;
}
.slide-fade-leave-active {
  transition: all 0.18s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active di bawah versi 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
.viewChange {
  background: white;
  border-radius: 10px;
  -webkit-box-shadow: 0px 0px 42px -18px rgba(120, 120, 120, 0.24);
  -moz-box-shadow: 0px 0px 42px -18px rgba(120, 120, 120, 0.24);
  box-shadow: 0px 0px 42px -18px rgba(120, 120, 120, 0.24);
}
</style>
<script>
import axios from "axios";
import ListCourse from "@/components/ListCouse.vue";
import FilterCourse from "@/components/FilterCourse.vue";
import RowCourse from "@/components/RowCourse.vue";
import FilterProviderCourse from "@/components/FilterProviderCourse.vue";
import { mapGetters } from "vuex";

export default {
  name: "Course",
  components: { ListCourse, FilterCourse, RowCourse, FilterProviderCourse },
  data() {
    return {
      loading: true,
      visible: false,
      courses: [],
      filter: "",
      filterPro: "",
      categoryData: "",
      providerData: "",
      show: false,
      perPage: 6,
      currentPage: 1,
      rows: 0,
    };
  },
  created() {
    this.getData(this.currentPage);
  },
  computed: {
    ...mapGetters({ user: "auth/user", results: "savecourse/result" }),
  },
  methods: {
    handleClick(value) {
      this.currentPage = value;
    },
    async getData(page = 1, newUrl = "", prov = "") {
      let url =
        "http://localhost:8000/course?page=" +
        page +
        "&page_size=" +
        this.perPage +
        newUrl +
        prov;
      let response = await axios.get(url);
      this.courses = this.checkdata(response.data);
      this.rows = response.data["countAll"];
      this.loading = false;
    },
    checkdata(data) {
      for (let index = 0; index < this.results.length; index++) {
        const element = this.results[index].courses;
        data.data.forEach((el) => {
          if (element.id === el.id) {
            el["check"] = true;
          }
        });
      }
      return data;
    },
  },

  watch: {
    currentPage(newValue, oldValue) {
      if (newValue !== oldValue) {
        this.getData(newValue, this.categoryData, this.providerData);
      } else {
        this.getData();
      }
    },
    filter(newValue, oldValue) {
      if (newValue !== oldValue) {
        this.categoryData = "&category=" + newValue;
        this.getData(this.currentPage, this.categoryData, this.providerData);
      } else {
        this.getData();
      }
    },
    filterPro(newValue, oldValue) {
      if (newValue !== oldValue) {
        this.providerData = "&provider=" + newValue;
        this.getData(this.currentPage, this.providerData, this.providerData);
      } else {
        this.getData();
      }
    },
  },
};
</script>
