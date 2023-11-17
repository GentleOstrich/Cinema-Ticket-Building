<template>
  <el-card class="box-card"  
  style="width: 30%;
  margin-bottom: 100px;
  margin-top: 120px;
  opacity: 0.7;
  margin-left: 800px;"
  >
    <template #header>
      <div class="card-header" style="margin-top: 30px;">
        <span style="margin-left: 30px; font-size: 0.65cm;"><strong>请登录</strong></span>
        <el-button class="button" text style="font-size: 0.34cm; background-color: ">
          <router-link to="/register" style="text-decoration: none; color: red;" >没有账户？快来注册！</router-link></el-button>
      </div>
      <el-input v-model.lazy="form.username" placeholder="请输入用户名" style="padding: 20px 30px 5px 30px;" />
      <el-input v-model.lazy="form.password" type="password" placeholder="请输入密码" show-password
        style="padding: 20px 30px 5px 30px;" />
    </template>
    <div style="text-align: right; margin: 5px 30px 5px 0">
      <el-button type="success" @click="login" :plain="true">
        <!-- 此处需要进行向用户主页的跳转 -->
        登录</el-button>
    </div>
  </el-card>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import axios from "axios"
import qs from "qs"
const form = {
  username: "",
  password: "",
}
const login = () => {
  if (form.username == '') {
    ElMessage.error('请输入正确的用户名')
    form.username = ''
    form.password = ''
    return
  } else if (form.password == '') {
    ElMessage.error('请输入正确的密码')
    form.username = ''
    form.password = ''
    return
  } else {
    axios
      .post("/user/login", qs.stringify(form))
      .then((res) => {
        if (res.data.errno === 0) {
          ElMessage.success('欢迎您,' + form.username)
        } else {
          ElMessage.error('账号或密码错误')
        }
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
