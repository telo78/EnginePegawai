<template>
  <div class="container filterco text-left px-3 py-3 mb-3">
    <h5 class="text-center">Provider</h5>

    <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-checkbox
        v-model="selecteda"
        class="mb-2"
        :aria-describedby="ariaDescribedby"
        name="Filter"
        v-for="cat in category"
        :key="cat.id"
        :value="cat.id"
        >{{ cat.name }}
      </b-form-checkbox>
    </b-form-group>
  </div>
</template>

<style scoped>
.filterco {
  background: white;
  border-radius: 10px;
}
</style>
<script>
export default {
  name: "FilterProviderCourse",
  data() {
    return {
      selecteda: "",
      category: [
        { name: "Udemy", id: 1 },
        { name: "Pluralsight", id: 2 },
        { name: "Skill Academy", id: 3 },
      ],
    };
  },
  watch: {
    value(newVal, oldVal) {
      // this check is mandatory to prevent endless cycle
      if (newVal !== oldVal) this.selecteda = newVal;
    },
    selecteda(newVal, oldVal) {
      // this check is mandatory to prevent endless cycle
      if (newVal !== oldVal) this.$emit("input", newVal);
    },
  },
};
</script>
