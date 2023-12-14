<template>
  <el-table v-loading.fullscreen.lock="fullscreenLoading" :data="tableData" style="width: 10000px; margin-left: 20px; margin-top: 50px" table-layout="fixed" empty-text="没有用户">
    <el-table-column prop="fields.username" label="用户名" width="500" />
    <el-table-column prop="fields.email" label="邮箱" width="500" />
    <el-table-column fixed="right" label="操作" width="500">
      <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          style="color: red"
          @click.prevent="deleteRow(scope.$index)"
        >
          注销用户
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts" setup>
import { ref,onMounted } from 'vue'
import { ElMessage,ElMessageBox } from "element-plus";
import axios from 'axios';

const fullscreenLoading = ref(true);

interface User {
  fields: {
    username: string;
    email: string;
  };
}

const tableData = ref<User[]>([]);

// 在组件加载时获取数据
onMounted(fetchData);

async function fetchData() {
  try {
    fullscreenLoading.value = true;
    const response = await axios.get('/user/index');
    tableData.value = response.data.data;
    fullscreenLoading.value = false;
  } catch (error) {
    fullscreenLoading.value = false;
    console.error('Error fetching data:', error);
  }
}

const deleteRow = (index: number) => {
  ElMessageBox.confirm(
    '该操作会注销当前账户且无法撤销，确认吗？',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    }
  )
    .then(() => {
      const username = tableData.value[index].fields.username;
      axios
        .post("/user/delete/",{username:username})
        .then((res) => {
            console.log(res)
            if (res.data.errno === 0) {
              ElMessage.success('删除成功');
              tableData.value.splice(index, 1);
            } else {
              ElMessage.error('删除失败');
            }
          })
          .catch((error) => {
            console.log(error)
          })
    })
    .catch(() => {

    })

}
</script>
