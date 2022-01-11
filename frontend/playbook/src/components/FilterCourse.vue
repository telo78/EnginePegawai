<template>
  <div class="container filterco text-left px-3 py-3 mb-3">
    <h4 class="text-center">Kategori</h4>
    <b-form-group v-slot="{ ariaDescribedby }">
      <b-form-radio
        v-model="selected"
        class="mb-2"
        :aria-describedby="ariaDescribedby"
        name="Filter"
        v-for="cat in category"
        :key="cat.id"
        :value="cat.id"
        >{{ cat.name }}
      </b-form-radio>
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
  name: "FilterCourse",
  data() {
    return {
      selected: "",
      category: [
        { name: "IT & Software", id: 1 },
        { name: "Business", id: 2 },
        { name: "Design", id: 3 },
        { name: "Development", id: 4 },
        { name: "Finance & Accounting", id: 5 },
        { name: "Health & Fitness", id: 6 },
        { name: "Lifestyle", id: 7 },
        { name: "Marketing", id: 8 },
        { name: "Music", id: 9 },
        { name: "Office Productivity", id: 10 },
        { name: "Personal Development", id: 11 },
        { name: "Photography & Video", id: 12 },
        { name: "Teaching & Academics", id: 13 },
      ],
    };
  },
  watch: {
    value(newVal, oldVal) {
      // this check is mandatory to prevent endless cycle
      if (newVal !== oldVal) this.selected = newVal;
    },
    selected(newVal, oldVal) {
      // this check is mandatory to prevent endless cycle
      if (newVal !== oldVal) this.$emit("input", newVal);
    },
  },
};
</script>
