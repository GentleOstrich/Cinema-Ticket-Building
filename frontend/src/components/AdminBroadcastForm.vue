<script setup>
import {useRoute} from "vue-router";
import {onMounted, ref} from "vue";

const route = useRoute()

let movie_name = ref(null)

onMounted(() => {
  movie_name.value = route.query.movie_name
})

</script>

<template>
  <div>{{ movie_name.value }}</div>
</template>

<style scoped>

</style>