<template>
  <el-table :data="tableData" style="width: 10000px; margin-left: 20px; margin-top: 50px" table-layout="fixed">
    <el-table-column prop="username" label="电影名" width="450" />
    <el-table-column prop="password" label="密码" width="450" />
    <el-table-column prop="isAdmin" label="管理员" width="200" />
    <el-table-column fixed="right" label="操作" width="400">
      <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          style="color: red"
          @click.prevent="deleteRow(scope.$index)"
        >
          删除用户
        </el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import {ElMessageBox} from "element-plus";

const tableData = ref([
  {
    username: 'Tom',
    password: 'California',
    isAdmin: '是'
  },
  {
    username: 'Tom',
    password: 'California',
    isAdmin: '是'
  },
  {
    username: 'Tom',
    password: 'California',
    isAdmin: '是'
  },
])

const deleteRow = (index: number) => {
  ElMessageBox.confirm(
    '该操作会注销当前账户，确认吗',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    }
  )
    .then(() => {
      tableData.value.splice(index, 1)
    })
    .catch(() => {

    })

}
</script>
