<template>
 <el-table :data="tableData" style="width: 10000px; margin-left: 20px;" table-layout="fixed">
    <el-table-column prop="fields.name" label="电影名" width="250" />
    <el-table-column prop="fields.genre" label="类型" width="250" />
    <el-table-column prop="fields.region" label="地区" width="200" />
    <el-table-column prop="fields.lasting" label="时长" width="150" />
    <el-table-column fixed="right" label="操作" width="400">
      <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          style="color: red"
          @click.prevent="deleteRow(scope.$index)"
        >
          退订
        </el-button>
        </template>
    </el-table-column>
 </el-table>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {ElMessage, ElMessageBox} from "element-plus";
import axios from "axios/index";

const now = new Date()

const tableData = ref([
  {
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
  },
])

const deleteRow = (index: number) => {
  ElMessageBox.confirm(
    '该操作会删除已订的影票，确认吗',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning',
    }
  )
    .then(() => {
        ElMessage.success('退订成功');
        tableData.value.splice(index, 1);
    })
    .catch(() => {

    })
}

</script>