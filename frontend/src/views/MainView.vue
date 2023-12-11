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
    let userName = JSON.parse(sessionStorage.getItem('user'))
    if (userName) {
      this.user = userName.username
    }
    console.log(this.user)
  }
}
</script>

<template>
  <TopColomn :msg="user"></TopColomn>
  <SearchSection></SearchSection>
</template>
