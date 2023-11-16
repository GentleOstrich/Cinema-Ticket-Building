<template>
  <div class="h-6" />
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    background-color="#c45656"
    text-color="#fff"
    active-text-color="#ffd04b"
    @select="handleSelect"
  >
    <el-menu-item index="1">
      <router-link to="/" style="text-decoration: none;">登录</router-link>
    </el-menu-item>
    <el-menu-item index="2">电影列表</el-menu-item>
    <div class="flex-grow" />
    <el-sub-menu index="3">
      <template #title>Workspace</template>
      <el-menu-item index="3-1">
        <router-link to="/home" style="text-decoration: none; color: inherit;">个人主页</router-link>
      </el-menu-item>
      <el-menu-item index="3-2">设置</el-menu-item>
    </el-sub-menu>
    
  </el-menu>
</template>




<script lang="ts" setup>
import { ref } from 'vue'
const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style>
.flex-grow {
  flex-grow: 1;
}

</style>

