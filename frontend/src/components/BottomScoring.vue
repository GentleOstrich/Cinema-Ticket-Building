<template>
    <strong style="margin: 0 0 0 20px">对我们的网站满意？请给我们好评！👉&nbsp;&nbsp;&nbsp;</strong>
    <el-rate
    v-model="value"
    :texts="['太差劲了😫', '还需努力😔', '一般般😐', '不错😀', '非常棒😊']"
    show-text
    @click="scoring"
    />
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus';
const scoring = () => {
  ElMessage({
    message: "我们收到了反馈，感谢您的评价！",
    type: 'success'
  })
}
const value = ref('')
</script>

