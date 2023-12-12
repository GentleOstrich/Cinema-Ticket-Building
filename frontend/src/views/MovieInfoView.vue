<script setup>
import {onMounted, ref} from "vue";

import {useRoute} from "vue-router";

const route = useRoute()

let movie_name = ref(null)


onMounted(() => {
  movie_name.value = route.query.movie_name
})


</script>

<template>
  <div>{{ movie_name }}</div>
  <router-link to="/movies/index">
    back
  </router-link>
</template>

<style scoped>

</style>