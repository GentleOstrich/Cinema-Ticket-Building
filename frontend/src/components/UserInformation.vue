<template>
  <span style="font-size: 0.6cm">您可以在此查看并修改您的信息</span>
  <el-form :model="form" label-width="120px">
    <el-form-item label="用户名" style="margin-bottom: 50px">
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="邮箱" style="margin-bottom: 50px">
      <el-input v-model="form.email" />
    </el-form-item>
    <el-form-item label="个人简介" style="margin-bottom: 50px">
      <el-input v-model="form.desc" type="textarea" />
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
const form = reactive({
  name: '',
  email: '',
  desc: '',
})

const onSubmit = () => {
   ElMessage({
    message: '保存成功！',
    type: 'success',
  })
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
          username.value = '大傻逼'
        }
      }).catch((error) => {
    console.log(error)
  })
}

</script>