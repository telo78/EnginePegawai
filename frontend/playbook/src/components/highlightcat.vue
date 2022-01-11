<template>
  <div class="box">
    <p class="h5 my-auto">
      <b-icon icon="search" class="my-auto mr-2"></b-icon>lorem ipsum
    </p>
  </div>
</template>

<style scoped>
.box {
  flex: 20%;
  width: 100px;
  padding: 10px;
  margin: 10px;
  background: rgba(226, 226, 226, 0.65);
  backdrop-filter: blur(11px);
  -webkit-backdrop-filter: blur(11px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 30px;
  transition: transform 0.3s;
}
.box:hover {
  box-shadow: 0 5px 32px 0 rgba(95, 101, 192, 0.144);
  transform: scale(1.1);
}
.box p {
  color: black;
}
</style>
<script>
export default {
  name: "highlightcat",
};
</script>
