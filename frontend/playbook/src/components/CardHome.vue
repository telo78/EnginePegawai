<template>
  <b-card tag="article" style="max-width: 25rem" class="mb-1">
    <b-img
      :src="image"
      fluid
      alt="Responsive image"
      width="100px"
      height="100px"
    ></b-img>
    <b-card-text class="text-center">
      <h4 id="hg" class="mt-3">{{ title }}</h4>
    </b-card-text>
  </b-card>
</template>

<style scoped>
#hg {
  font-weight: 600;
  font-size: 16px;
}
.card {
  transition: 0.4s ease;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 50px;
}
.card:hover {
  box-shadow: rgba(85, 107, 204, 0.288) 0px 10px 50px;
  transform: scale(1.01);
}
</style>
<script>
export default {
  name: "CardHome",
  props: ["image", "title"],
};
</script>
