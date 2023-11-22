<script setup>
import axios from "axios";
import TopColomn from "../components/TopColomn.vue";
import SearchSection from "../components/SearchSection.vue";
const getList = () => {
  axios
      .get("/movie/index/")
      .then((res) => {
          console.log(res.data)
      })
      .catch((error) => {
        console.log(error)
      })
}
</script>

<template>
  <TopColomn></TopColomn>
  <SearchSection></SearchSection>
  <router-view/>
</template>
