<template>
  <div class="h-6">
    <el-menu class="el-menu-demo" :default-active="activeIndex" style="border: 0;" mode="horizontal" background-color="#c45656" text-color="#ffffff"
      active-text-color="#ffd04b" @select="handleSelect">
      <el-menu-item index="1">
        <router-link to="/" style="text-decoration: none;">欢迎页</router-link>
      </el-menu-item>
      <el-menu-item index="2">电影列表</el-menu-item>
      <el-sub-menu index="3" :default-active="activeIndex">
        <template #title>更多</template>
        <el-menu-item index="3-1">
          <router-link to="/home/userinfo" style="text-decoration: none; color: inherit;">个人主页</router-link>
        </el-menu-item>
        <el-menu-item index="3-2">
          <router-link to="/about" style="text-decoration: none; color: inherit;">关于我们</router-link>
        </el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const activeIndex = ref(1)
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>

