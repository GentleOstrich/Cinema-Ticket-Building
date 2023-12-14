<template>
  <span style="font-size: 0.6cm; margin-bottom: 50px">您可以在此修改您的密码和邮箱</span>
  <el-form :model="form" label-width="120px">
    <el-form-item label="密码" style="margin-bottom: 50px; margin-top: 50px">
      <el-input v-model="form.password" />
    </el-form-item>
    <el-form-item label="邮箱" style="margin-bottom: 50px">
      <el-input v-model="form.email" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">保存</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import {onMounted, ref} from "vue";
import axios from "axios";
import { reactive } from 'vue'
import {ElMessage} from "element-plus";

// do not use same name with ref
const form = ref({
  password: '',
  email: '',
})

const onSubmit = () => {
  axios
    .post('/user/update/',form.value)
    .then((res) => {
          if (res.data.errno === 0) {
            ElMessage({
              message: '保存成功！',
              type: 'success',
            })
          } else {

          }
        })
        .catch((error) => {
          console.error(error);
          ElMessage.error('系统错误');
        });
}

onMounted(() => {
  setTimeout(() => askName(), 500)
})

let username = ref(null)

function askName() {
  axios
      .post("/user/askName/")
      .then((res) => {
        if (res.data.errno === 0) {
          username.value = res.data.username
        } else {
          
        }
      }).catch((error) => {
    console.log(error)
  })
}

</script>