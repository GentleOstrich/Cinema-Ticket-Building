<template>
  <div id="welcomePage">
    <TopColumn></TopColumn>
    <!-- 一些介绍 -->
    <div id="loginCard">
      <LoginCard></LoginCard>
    </div>
    <BottomScoring></BottomScoring>
  </div>
</template>

<script lang="ts" setup>
import TopColumn from '../components/TopColomn.vue';
import LoginCard from '../components/LoginCard.vue';
import BottomScoring from '../components/BottomScoring.vue';
</script>

<style>
#welcomePage {
  background: url("../assets/亚托莉6.png");
  height: 100vh;
  width: 100vw;
  background-size: cover;
  background-position: center center;
}
</style>
