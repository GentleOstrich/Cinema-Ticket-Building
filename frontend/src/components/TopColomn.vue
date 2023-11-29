<template>
  <div class="h-6">
    <el-menu class="el-menu-demo" style="border: 0;" mode="horizontal" background-color="#c45656" text-color="#ffffff" router="true"
      active-text-color="#ffd04b" @select="handleSelect" >
      <el-menu-item index="/movies/index">电影列表</el-menu-item>
      <el-menu-item index="/home/userinfo">个人主页</el-menu-item>
      <el-sub-menu>
        <template #title>更多</template>
        <el-menu-item @click="changeUser">切换账号</el-menu-item>
        <el-menu-item index="/about">关于我们</el-menu-item>
        <el-menu-item index="/admin">管理员入口</el-menu-item>
      </el-sub-menu>
      <div class="flex-grow" />
      <el-menu-item @click="returnWelcome">登出</el-menu-item>
      
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import { ElMessage , ElMessageBox } from 'element-plus';
import { useRouter } from 'vue-router';
import { Action } from 'element-plus';
const route = useRouter()
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const returnWelcome = () => {
  ElMessageBox.confirm(
    '<strong>此操作会登出当前帐号，确定吗?</strong>',
    '系统提示',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
      dangerouslyUseHTMLString: true
    }
  )
    .then(() => {
        ElMessageBox.alert(
          '<strong style="font-size: 0.5cm">期待与您再次相遇</strong>',
          '登出成功',
          {
            dangerouslyUseHTMLString: true,
            confirmButtonText: '确定',
            draggable: true,
            type: 'info',
            callback: (action: Action) => {
              route.push('/')
            },
          }
        )
        
    })
    .catch(() => {

    })
}

const changeUser = () => {
  ElMessageBox.confirm(
    '<strong>此操作会登出当前帐号，确定吗?</strong>',
    '系统提示',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
      dangerouslyUseHTMLString: true
    }
  )
    .then(() => {
        route.push('/login')
    })
    .catch(() => {
      
    })
}

</script>

<style>
.flex-grow {
  flex-grow: 0.94;
}
</style>

