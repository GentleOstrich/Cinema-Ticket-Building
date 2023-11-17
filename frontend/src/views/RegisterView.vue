<template>
    <div id="registerPage">
        <div style="
        text-align: center; 
        padding-top: 30px; 
        font-size: 1cm; 
        color: #000000; 
        font-family: 'Lucida Calligraphy', cursive, serif, sans-serif ;
        background: rgba(255, 255, 255, 0.4);">
            <strong>欢&nbsp;迎&nbsp;您&nbsp;加&nbsp;入&nbsp;影&nbsp;院&nbsp;票&nbsp;楼&nbsp;！</strong>
        </div>
        <div id="registerCard">
            <RegisterCard></RegisterCard>
        </div>
    </div>
</template>
  
<script lang="ts" setup>
import RegisterCard from '../components/RegisterCard.vue';
</script>
  
<style>
#registerPage {
    background: url("../assets/亚托莉1.png");
    height: 100vh;
    width: 100vw;
    background-size: cover;
    background-position: center center;
}
</style>
  