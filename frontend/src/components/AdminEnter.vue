<script setup>
import {useRouter} from "vue-router";

const route = useRouter();
const toAdminMovies = () => {
  route.push('/admin/movies')
}

const toAdminUsers = () => {
  route.push('/admin/users')
}
</script>

<template>
<div class="common-layout">
    <el-container>
      <el-header style="margin-top: 80px;">
        <div class="container">您好，管理员{{这里需要传入管理员的名称}}</div>
      </el-header>
      <el-main style="text-align: center">
        <div style="text-align: center; margin-top: 200px">
          <el-button id="button" round @click="toAdminMovies">管理电影</el-button>
          <el-button id="button" round @click="toAdminUsers">管理用户</el-button>
        </div>
      </el-main>
    </el-container>
  </div>

</template>

<style scoped>
  .container {
    font-size: 50px;
    letter-spacing: 10px;
    /*文字渐变*/
    background: linear-gradient(180deg, #ffffff 10%, #fc3c3c 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    /*倒影*/
    -webkit-box-reflect: below -14px linear-gradient(transparent, rgba(0,0,0,0.4));
    text-align: center
  }
  #button {
    margin: 0 100px 0 100px;
    font-size: 0.6cm;
    width: 250px;
    height: 70px;
    border-radius: 50px;
    border-width: 2px;
    background: none;
  }
</style>