<template>
    <el-menu default-active="none" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" style="min-height: 100vh;">
        <el-menu-item index="1">
            <el-icon><icon-menu /></el-icon>
            <span>个人信息</span>
        </el-menu-item>
        <el-menu-item index="2">
            <el-icon><Star /></el-icon>
            <span><router-link to="/home/userticket" style="text-decoration: none; color: inherit;">我的影票</router-link></span>
        </el-menu-item>
        <el-menu-item index="3">
            <el-icon>
                <setting />
            </el-icon>
            <span>设置</span>
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