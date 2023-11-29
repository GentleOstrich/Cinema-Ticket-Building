<template>
    <el-card class="box-card" shadow="hover"
        style="width: 30%;  margin-bottom: 10%;  margin-top: 100px;  opacity: 0.7;  margin-left: 250px;" >
        <template #header>
            <div class="card-header" style="margin-top: 30px;">
                <span style="margin-left: 30px; font-size: 0.65cm;"><strong>请注册</strong></span>
                <el-button class="button" text style="font-size: 0.34cm; background-color: white">
                    <router-link to="/login" style="text-decoration: none; color: green;">已有账户？快来登录！</router-link></el-button>
            </div>
            <el-input v-model.lazy="form.username" placeholder="请输入2~8个字的用户名（支持字母与汉字）" style="padding: 20px 30px 5px 30px;" />
            <el-input v-model.lazy="form.password" type="password" placeholder="请输入6~16位的密码（不支持汉字）" show-password
                style="padding: 20px 30px 5px 30px;" />
        </template>
        <div style="text-align: right; margin: 5px 30px 5px 0">
            <el-button type="success" @click="register" style="margin-left: 240px;">
                <!-- 此处需要进行向用户主页的跳转 -->
                注册</el-button>
        </div>
    </el-card>

</template>

<script lang="ts" setup>
import { ElNotification } from 'element-plus'
import { ElMessage, ElMessageBox } from 'element-plus'
import type { Action } from 'element-plus'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from "axios"
import qs from "qs"
const form = ref({
    username: "",
    password: "",
})
const route = useRouter()
const register = () => {
    // 这里需要保证username不重复,并且校验用户名是否合法
    if (form.value.username.length < 2 || form.value.username.length > 8) {
        ElMessage.error('请输入符合要求的用户名')
        form.value.username = ''
        form.value.password = ''
        return
    } else if (form.value.password.length < 6) {
        ElMessage.error('请输入符合要求的密码')
        form.value.username = ''
        form.value.password = ''
        return
    } else {
        axios
        .post("/user/create/", qs.stringify(form))
        .then((res) => {
            if (res.data.errno === 0) {
                ElMessageBox.alert(
                '<strong>恭喜您，注册成功！</strong>',
                '系统提示：',
                {
                    dangerouslyUseHTMLString: true,
                    confirmButtonText: '确定',
                    draggable: true,
                    callback: (action: Action) => {
                        
                    },
                }
                )
                route.push('./login/')
            } else {
            ElMessage.error('账号或密码错误')
            }
            form.value.username = ''
            form.value.password = ''
        })
        .catch((error) => {
            console.log(error)
        })
    }
}
</script>
