<template>
    <div id="loginPage" style="margin-bottom:0 ;">
      <TopColumn></TopColumn>
      <div id="loginCard">
        <LoginCard></LoginCard>
      </div>
      <div id="loginPageBottomText">
        愿时间停止在这挚爱的时刻。&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——亚托莉
      </div>
  
    </div>
</template>
  
  <script lang="ts" setup>
  import TopColumn from '../components/TopColomn.vue';
  import LoginCard from '../components/LoginCard.vue';
  </script>
  
  <style>
  #loginPage {
    background: url("../assets/亚托莉6.png");
    height: 100vh;
    width: 100vw;
    background-size: cover;
    background-position: center center;
  }
  
  #loginPageBottomText {
    position: absolute;
    text-align: center;
    left: 0;
    right: 0;
    bottom: 0;
    font-size: 0.8cm;
    font-family: 'Lucida Calligraphy', cursive, serif, sans-serif;
    font-weight: bolder;
    background: rgba(255, 255, 255, 0.4);
    color: black;
  }
  </style>
  