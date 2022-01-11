<template>
  <div class="Home">
    <Highlight />
    <b-container fluid="md">
      <b-row class="mt-5">
        <b-col md="12">
          <h6 class="mt-5 text-left" id="hg">Highlight</h6>
        </b-col>
      </b-row>
      <b-row class="mt-3 mb-5 text-left">
        <b-col md="6" id="hh"
          >Temukan kursus terbaik dari seluruh Provider!</b-col
        >
      </b-row>
      <b-row class="mt-5 justify-content-center">
        <b-col md="3">
          <b-card
            :img-src="require('../assets/provider/udemy.png')"
            img-alt="Image"
            overlay
            class="card2"
          >
          </b-card>
          <h5 id="hf">Udemy</h5>
        </b-col>
        <b-col md="3">
          <b-card
            :img-src="require('../assets/provider/skillacademy.png')"
            img-alt="Image"
            class="card2"
            overlay
          ></b-card>
          <h5 id="hf">Skill Academy</h5>
        </b-col>
        <b-col md="3">
          <b-card
            :img-src="require('../assets/provider/pluralsight.png')"
            img-alt="Image"
            class="card2"
            overlay
          ></b-card>
          <h5 id="hf">Pluralsight</h5>
        </b-col>
      </b-row>
      <b-row class="mt-5">
        <b-col md="12">
          <h6 class="mt-5 text-left" id="hg">Kategori</h6>
        </b-col>
      </b-row>
      <b-row class="mt-3 mb-5 text-left">
        <b-col md="6" id="hh">Kategori kursus</b-col>
      </b-row>
      <b-row class="mt-5">
        <b-col md="4">
          <CardHome
            :image="require('../assets/category/it.png')"
            :title="category[0].name"
          />
        </b-col>
        <b-col md="4">
          <CardHome
            :image="require('../assets/category/design.png')"
            :title="category[2].name"
          />
        </b-col>
        <b-col md="4">
          <CardHome
            :image="require('../assets/category/bisnis.png')"
            :title="category[1].name"
          />
        </b-col>
      </b-row>
      <b-row class="mt-5">
        <b-col md="4">
          <CardHome
            :image="require('../assets/category/finance.png')"
            :title="category[3].name"
          />
        </b-col>
        <b-col md="4">
          <CardHome
            :image="require('../assets/category/lifestyle.png')"
            :title="category[4].name"
          />
        </b-col>
        <b-col md="4">
          <CardHome
            :image="require('../assets/category/personaldev.png')"
            :title="category[5].name"
          />
        </b-col>
      </b-row>
      <b-row class="mt-3">
        <b-col md="12">
          <b-button block>Selengkapnya</b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style scoped>
#hg {
  color: #4141a5;
  font-weight: 600;
  letter-spacing: 3px;
}
#hh {
  font-size: 40px;
  font-weight: 900;
}

#hf {
  font-weight: 800;
}

.card2 {
  display: block;
  top: 0px;
  position: relative;
  max-width: 262px;
  background-color: white;
  border-radius: 4px;
  padding: 32px 24px;
  margin: 12px;
  text-decoration: none;
  z-index: 0;
  overflow: hidden;
  border: 1px solid #f2f8f9;
}
.card2:hover {
  transition: all 0.2s ease-out;
  box-shadow: 0px 4px 8px rgba(38, 38, 38, 0.2);
  top: -4px;
  border: 1px solid #cccccc;
  background-color: white;
}
.card2:before {
  content: "";
  position: absolute;
  z-index: -1;
  top: -16px;
  right: -16px;
  background: #00838d;
  height: 32px;
  width: 32px;
  border-radius: 32px;
  transform: scale(2);
  transform-origin: 50% 50%;
  transition: transform 0.15s ease-out;
}
.card2:hover:before {
  transform: scale(2.15);
}
</style>
<script>
// @ is an alias to /src
import Highlight from "@/components/Highlight.vue";
import CardHome from "@/components/CardHome.vue";

export default {
  name: "Home",
  data() {
    return {
      category: [
        { name: "IT & Software", id: 1 },
        { name: "Business", id: 2 },
        { name: "Design", id: 3 },
        { name: "Finance & Accounting", id: 5 },
        { name: "Lifestyle", id: 7 },
        { name: "Personal Development", id: 11 },
      ],
    };
  },
  components: {
    Highlight,
    CardHome,
  },
};
</script>
Highlight
