<template>
    <el-page-header @back="goBack" style="margin: 30px 0 0 20px;">
    <template #content>
      <span class="text-large font-600 mr-3"> 管理员页面 </span>
    </template>
  </el-page-header>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router';

const route = useRouter()
const goBack = () => {
  route.back()
}
</script>