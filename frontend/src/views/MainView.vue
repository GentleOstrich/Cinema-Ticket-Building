<script setup>
import axios from "axios";

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
  <div>this is movie list</div>
  <button @click="getList">get</button>
</template>
