<template id="home">
  <div class="common-layout">
    <el-container style="margin: 0;">
      <el-header style="padding: 0; background-color: black;">
        <TopColomn></TopColomn>
      </el-header>
      <el-container>
        <el-aside width="200px">
          <SideColomn></SideColomn>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script lang="ts" setup>
import TopColomn from '../components/TopColomn.vue';
import SideColomn from '../components/SideColomn.vue';
</script>


