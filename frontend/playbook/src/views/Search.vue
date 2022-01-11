<template>
  <b-container class="mb-4">
    <b-row class="mt-5 mb-4 text-left">
      <b-col>
        <h3>
          Search Result: <strong>{{ result.keyword }}</strong>
        </h3>
        <p class="text-muted">Total: {{ result.countAll }}</p>
      </b-col>
    </b-row>
    <b-row class="mb-2" v-for="i in itemforList()" :key="i.id">
      <b-col md="12">
        <SearchResult
          :title="i.title"
          :image="i.image"
          :instr="i.instructors"
          :url="i.url"
        />
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-pagination
          align="center"
          pills
          v-model="currentPage"
          :total-rows="result.countAll"
          :per-page="perPage"
          @change="handleClick"
        ></b-pagination>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import SearchResult from "@/components/SearchResult.vue";
import { mapGetters } from "vuex";

export default {
  name: "Search",
  data() {
    return {
      currentPage: 1,
      perPage: 10,
      rows: 0,
    };
  },
  created() {
    this.itemforList();
  },
  computed: {
    ...mapGetters({ result: "search/result" }),
  },
  methods: {
    handleClick(value) {
      this.currentPage = value;
    },

    itemforList() {
      return this.result.data.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      );
    },
  },
  components: { SearchResult },
};
</script>
