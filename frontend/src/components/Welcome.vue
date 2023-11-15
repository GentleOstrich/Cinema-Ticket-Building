<template>
    <div class="common-layout">
    <el-container>
      <el-header>
        <h1 style="text-align: center; font-size: 1.5cm;">🎉Welcome!🎉</h1>
      </el-header>
      <el-main style="margin-top: 100px;">
        <el-card class="box-card" style="width: 30%; margin: 10px auto 50px auto;">
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
      </el-main>
      <el-footer>
        <strong>对我们的网站满意？请给我们好评！👉&nbsp;&nbsp;&nbsp;</strong>
        <el-rate
        v-model="value"
        :texts="['太差劲了😫', '还需努力😔', '一般般😐', '不错😀', '非常棒😊']"
        show-text
        @click="scoring"
        />
      </el-footer>
    </el-container>
  </div>
</template>


<script lang="ts" setup>
import { ref } from 'vue'
import { ElMessage, emptyProps } from 'element-plus';
const idNum = ref('')
const password = ref('')
const value = ref('')
const scoring = () => {
  ElMessage({
    message: "我们收到了反馈，感谢您的评价！",
    type: 'success'
  })
}

const login = () => {
  // 此处需要连接后端进一步校验
  if (idNum.value == '') {
    ElMessage.error('请输入正确账号')
  } else if (password.value == '') {
    ElMessage.error('请输入正确密码')
  }
}
</script>
