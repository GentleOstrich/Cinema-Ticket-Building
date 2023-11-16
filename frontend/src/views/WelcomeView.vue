<template>
  <div id="welcomePage">
    <TopColumn></TopColumn>
    <!-- 一些介绍 -->
    <div id="loginCard"><LoginCard></LoginCard></div>
    <BottomScoring></BottomScoring>
  </div>
  
</template>


<script setup>
import TopColumn from '../components/TopColomn.vue';
import LoginCard from '../components/loginCard.vue';
import BottomScoring from '../components/BottomScoring.vue';

</script>


<style>
  #welcomePage{
  background:url("../assets/亚托莉6.png");
  width:100%;
  height:100%;
  position:center;
  background-size:100% auto;
  background-repeat: no-repeat;
  }

</style>
