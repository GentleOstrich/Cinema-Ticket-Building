<template>
    <el-card class="box-card" >
    <template #header>
      <div class="card-header" style="margin-top: 30px;">
        <span style="margin-left: 30px; font-size: 0.65cm;"><strong>请登录</strong></span>
        <el-button class="button" text style="font-size: 0.34cm; background-color: white"
        @click="">
        <!-- 此处需要进行向注册页面的跳转 -->
        没有账户？点此注册！</el-button>

      </div>
      <el-input v-model="idNum" placeholder="请输入账号" style="padding: 20px 30px 5px 30px;"/>
      <el-input
      v-model="password"
      type="password"
      placeholder="请输入密码"
      show-password
      style="padding: 20px 30px 5px 30px;"
      />
    </template>
    <div style="text-align: right; margin: 5px 30px 5px 0"><el-button type="success" @click="login"
      :plain="true">
      <!-- 此处需要进行向用户主页的跳转 -->
      登录</el-button></div>
  </el-card>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus';
const idNum = ref('')
const password = ref('')
const login = () => {
  // 此处需要连接后端进一步校验
  if (idNum.value == '') {
    ElMessage.error('请输入正确的账号')
  } else if (password.value == '') {
    ElMessage.error('请输入正确的密码')
  }
}
</script>
<style>
.box-card {
  width: 30%;
  margin-bottom: 10%; 
  margin-top: 170px; 
  opacity: 0.7;
  margin-left: 800px;
}
</style>