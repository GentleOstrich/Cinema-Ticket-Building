<template>
  <div class="h-6">
    <el-menu class="el-menu-demo" style="border: 0;" mode="horizontal" background-color="#c45656" text-color="#ffffff"
             router="true"
             active-text-color="#ffd04b" @select="handleSelect">
      <el-menu-item index="/movies/index">电影列表</el-menu-item>
      <el-menu-item index="/home/userinfo">个人主页</el-menu-item>
      <el-sub-menu>
        <template #title>更多</template>
        <el-menu-item @click="changeUser">切换账号</el-menu-item>
        <el-menu-item index="/about">关于我们</el-menu-item>
        <el-menu-item @click="adminCheck">管理员入口</el-menu-item>
        <el-menu-item @click="returnWelcome">登出</el-menu-item>
      </el-sub-menu>
      <div class="flex-grow"/>
      <el-menu-item>您好，{{ props.msg }}</el-menu-item>
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import {ElMessage, ElMessageBox} from 'element-plus';
import {useRouter} from 'vue-router';
import {Action} from 'element-plus';
import axios from "axios"
import qs from "qs";
import {ref} from "vue";

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

import {defineProps} from 'vue'
const props = defineProps({
  msg:String
})

const form = ref({
  username: ""
})

const adminCheck = () => {
  // 此处需要判断一下当前账号是否为管理员账号
  form.value.username = props.msg
  console.log(form.value.username)
  axios
      .post("/user/adminCheck/", qs.stringify(form))
      .then((res) => {
        console.log(res)
        if (res.data.errno === 0) {
          ElMessage.success('欢迎您,尊贵的管理员' + form.value.username)
          route.push('/admin/home')
        } else {
          route.push('/admin/error')
        }
      })
      .catch((error) => {
        console.log(error)
      })
}



</script>

<style>
.flex-grow {
  flex-grow: 0.94;
}
</style>

