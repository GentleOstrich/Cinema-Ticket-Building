<script setup>
import TopColomn from "../components/TopColomn.vue";
import SearchSection from "../components/SearchSection.vue";
</script>

<script>
export default {
  data() {
    return {
      user: '',
      radio1: ''
    }
  },
  mounted() {

  }
}
</script>

<template>
  <TopColomn></TopColomn>
  <SearchSection></SearchSection>
</template>


