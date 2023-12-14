<template>
    <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" style="min-height: 100vh;">
        <el-menu-item index="1">
            <el-icon><icon-menu /></el-icon>
            <span><router-link to="/home/userinfo" 
                style="text-decoration: none; 
                color: inherit; 
                padding-right: 99px; 
                padding-top: 25px; 
                padding-bottom: 10px;">
                    个人信息
                </router-link>
            </span>
        </el-menu-item>
        <el-menu-item index="2">
            <el-icon><Star /></el-icon>
            <span><router-link to="/home/userticket" 
                style="text-decoration: none; 
                color: inherit; 
                padding-right: 99px; 
                padding-top: 25px; 
                padding-bottom: 10px;">
                我的影票</router-link>
            </span>
        </el-menu-item>
        <el-menu-item index="3">
            <el-icon><Star /></el-icon>
            <span><router-link to="/home/userfavorite" 
                style="text-decoration: none; 
                color: inherit; 
                padding-right: 99px; 
                padding-top: 25px; 
                padding-bottom: 10px;">
                我的收藏</router-link>
            </span>
        </el-menu-item>
    </el-menu>
</template>

<script lang="ts" setup>
import {
  Menu as IconMenu,
  Star,
  Setting,
} from '@element-plus/icons-vue'
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>