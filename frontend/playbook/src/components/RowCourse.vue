<template>
  <div class="container">
    <b-table
      id="CourseTable"
      striped
      hover
      responsive="sm"
      :fields="fieldslist"
      :items="items"
      class="table-light"
    >
      <template #cell(title)="data">
        <a :href="data.item.url" style="color: black">{{ data.item.title }}</a>
      </template>
      <template #cell(image)="data">
        <img
          height="100px"
          width="100px"
          :src="data.value"
          alt="Center image"
          fluid
        />
      </template>
      <template #cell(providers)="data">
        <p>{{ data.item.providers.name }}</p>
      </template>
    </b-table>
  </div>
</template>

<script>
export default {
  name: "RowCourse",
  props: ["items"],
  data() {
    return {
      fieldslist: [
        { key: "image", label: "" },
        "title",
        "instructors",
        "providers",
      ],
    };
  },
};
</script>
