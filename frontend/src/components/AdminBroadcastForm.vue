<template>
  <el-backtop :right="100" :bottom="100"/>
  <div style="font-size: 0.6cm; margin: 30px 0 0 50px">您可以在这里新加放映信息</div>
  <div style="text-align: center; margin-top: 30px">
    <el-button class="mt-4" style="width: 30%; margin-right: 30px" @click="dialogTableVisible = true"
    >添加放映信息
    </el-button
    >
    <el-dialog v-model="dialogTableVisible" title="新电影信息">
      <div>&nbsp;</div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >开始时间</span
      >
          <el-input
              v-model="form.beginTime"
              class="w-50 m-2"
              placeholder="请输入开始时间"
              style="margin: 10px 0 10px 0"
          />
        </el-row>
      </div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >结束时间</span
      >
          <el-input
              v-model="form.endTime"
              class="w-50 m-2"
              placeholder="请输入结束时间"
              style="margin: 10px 0 10px 0">
          </el-input>
        </el-row>
      </div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >座位码（01）</span
      >
          <el-input
              v-model="form.seats"
              class="w-50 m-2"
              placeholder="请输入座位码（01）"
              style="margin: 10px 0 10px 0">
          </el-input>
        </el-row>
      </div>
      <el-button @click="addBroadcast" style="margin-left: 670px; margin-top: 30px">确定</el-button>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible1" title="修改电影信息">
      <div style="font-size: 0.5cm">请您重新编辑已有电影的相关信息</div>
      <div>&nbsp;</div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >开始时间</span
      >
          <el-input
              v-model="form.beginTime"
              class="w-50 m-2"
              placeholder="请输入开始时间"
              style="margin: 10px 0 10px 0"
          />
        </el-row>
      </div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >结束时间</span
      >
          <el-input
              v-model="form.endTime"
              class="w-50 m-2"
              placeholder="请输入结束时间"
              style="margin: 10px 0 10px 0">
          </el-input>
        </el-row>
      </div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >座位码（01）</span
      >
          <el-input
              v-model="form.seats"
              class="w-50 m-2"
              placeholder="请输入座位码（01）"
              style="margin: 10px 0 10px 0">
          </el-input>
        </el-row>
      </div>
      <el-button @click="updateBroadcast" style="margin-left: 670px; margin-top: 30px">确定</el-button>
    </el-dialog>
  </div>
  <el-table :data="tableData" style="width: 10000px; margin-left: 20px; margin-top: 50px" table-layout="fixed">
    <el-table-column prop="beginTime" label="开始时间" width="450"/>
    <el-table-column prop="endTime" label="结束时间" width="250"/>
    <el-table-column prop="seats" label="座位码" width="200"/>
    <el-table-column fixed="right" label="操作" width="400">
      <template #default="scope">
        <el-button
            link
            type="primary"
            size="small"
            @click.prevent="updateRow(scope.$index)"
        >
          修改放映信息
        </el-button>

        <el-button
            link
            type="primary"
            size="small"
            style="color: red"
            @click.prevent="deleteRow(scope.$index)"
        >
          删除放映信息
        </el-button>

      </template>

    </el-table-column>
  </el-table>

</template>

<script lang="ts" setup>
import {ref, onMounted} from 'vue'
import {ElMessage, ElMessageBox} from "element-plus";
import {useRoute} from "vue-router";
import axios from 'axios';



const route = useRoute()
const movie_name = ref('')
const curIndex = ref(-1)

const dialogTableVisible = ref(false)
const dialogTableVisible1 = ref(false)

// 在组件加载时获取数据
onMounted(fetchData);

async function fetchData() {
  try {
    movie_name.value = route.query.movie_name as string
    const response = await axios.get(`/broadcast/index/${movie_name.value}`);
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

interface Broadcast {
  id: BigInt;
  beginTime: string;
  endTime: string;
  seats: string;
}

const tableData = ref<Broadcast[]>([]);

const addBroadcast = () => {
  const formData = new FormData();
  for (const key in form.value) {
    formData.append(key, form.value[key]);
  }

  axios
      .post(`/broadcast/create/${movie_name.value}/`, formData)
      .then((res) => {
        if (res.data.errno === 0) {
          ElMessage.success('添加成功');
          tableData.value.push(res.data.data);
          dialogTableVisible.value = false
        } else {
          form.value.beginTime = ''
          form.value.endTime = ''
          form.value.seats = ''
        }
      })
      .catch((error) => {
        console.error(error);
        ElMessage.error('系统错误');
      });
}

const updateBroadcast = () => {
  const id = tableData.value[curIndex.value].id
  const formData = new FormData();
  for (const key in form.value) {
    formData.append(key, form.value[key]);
  }
  axios
      .post(`/broadcast/update/${id}/`, formData)
      .then((res) => {
        if (res.data.errno === 0) {
          ElMessage.success('修改成功');
          tableData.value.splice(curIndex.value, 0, res.data.data);
          tableData.value.splice(curIndex.value + 1, 1);
          dialogTableVisible1.value = false
        } else {
          form.value.beginTime = ''
          form.value.endTime = ''
          form.value.seats = ''
        }
      })
      .catch((error) => {
        console.error(error);
        ElMessage.error('系统错误');
      });
}

const updateRow = (index: number) => {
  dialogTableVisible1.value = true
  curIndex.value = index
}


const deleteRow = (index: number) => {
  ElMessageBox.confirm(
      '该操作会删除当前电影，确认吗',
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
            .post(`/broadcast/delete/${id}/`)
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
