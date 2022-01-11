<template>
  <b-card
    :img-src="image"
    img-height="150"
    img-width="150"
    img-alt="Card image"
    img-left
    class="mb-2"
  >
    <b-card-text class="text-left">
      <h4>
        <a :href="url" target="_blank" style="color: black"> {{ title }}</a>
      </h4>
      <p>{{ instr }}</p>
    </b-card-text>
  </b-card>
</template>

<script>
export default {
  name: "SearchResult",
  props: ["image", "title", "instr", "provider", "url"],
};
</script>
