<template>
 <el-table :data="tableData" style="width: 10000px; margin-left: 20px;" table-layout="fixed">
    <el-table-column prop="movie_name" label="电影名" width="300" />
    <el-table-column prop="beginTime" label="开始时间" width="200" />
    <el-table-column prop="endTime" label="结束时间" width="200" />
    <el-table-column prop="time" label="购票时间" width="200" />
    <el-table-column prop="seat" label="座位号" width="200" />
    <el-table-column fixed="right" label="操作" width="200">
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
import {ref,onMounted} from 'vue'
import {ElMessage, ElMessageBox} from "element-plus";
import axios from "axios";

const now = new Date()
// 在组件加载时获取数据
onMounted(fetchData);

async function fetchData() {
  try {
    const response = await axios.get('/ticket/index/');
    tableData.value = response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

const form = ref({
  beginTime: '',
  endTime: '',
  seats: ''
})

interface Ticket {
  id: BigInt;
  movie_name: string;
  beginTime: string;
  endTime: string;
  time: string;
  seat: BigInt;
}

const tableData = ref<Ticket[]>([]);

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
      const id = tableData.value[index].id;
      axios
        .post(`/ticket/delete/${id}/`)
        .then((res) => {
          if (res.data.errno === 0) {
            ElMessage.success('退订成功');
            tableData.value.splice(index, 1);
          } else {

          }
        })
        .catch((error) => {
          console.error(error);
          ElMessage.error('系统错误');
        });
    })
    .catch(() => {

    })
}

</script>