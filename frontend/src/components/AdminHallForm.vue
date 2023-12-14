<template>
  <el-backtop :right="100" :bottom="100"/>
  <div style="font-size: 0.6cm; margin: 30px 0 0 50px">您可以在这里新建场馆</div>
  <div style="text-align: center; margin-top: 30px">
    <el-button class="mt-4" style="width: 30%; margin-right: 30px" @click="dialogTableVisible = true"
    >新建场馆
    </el-button
    >
    <el-dialog v-model="dialogTableVisible" title="新建场馆">
      <div>&nbsp;</div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >场馆名</span
      >
          <el-input
              v-model="form.name"
              class="w-50 m-2"
              placeholder="请输入场馆名"
              style="margin: 10px 0 10px 0"
          />
        </el-row>
      </div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >座位数</span
      >
          <el-input
              v-model="form.seats_num"
              class="w-50 m-2"
              placeholder="请输入座位数"
              type="integer"
              style="margin: 10px 0 10px 0">
          </el-input>
        </el-row>
      </div>
      <el-button @click="addHall" style="margin-left: 670px; margin-top: 30px">确定</el-button>
    </el-dialog>

    <el-dialog v-model="dialogTableVisible1" title="修改电影信息">
      <div style="font-size: 0.5cm">请您重新编辑已有电影的相关信息</div>
      <div>&nbsp;</div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >场馆名</span
      >
          <el-input
              v-model="form.name"
              class="w-50 m-2"
              placeholder="请输入场馆名"
              style="margin: 10px 0 10px 0"
          />
        </el-row>
      </div>
      <div class="demo-input-suffix">
        <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
      >座位数</span
      >
          <el-input
              v-model="form.seats_num"
              class="w-50 m-2"
              placeholder="请输入电影类型"
              type="integer"
              style="margin: 10px 0 10px 0">
          </el-input>
        </el-row>
      </div>
      <el-button @click="updateHall" style="margin-left: 670px; margin-top: 30px">确定</el-button>
    </el-dialog>
  </div>
  <el-table :data="tableData" style="width: 10000px; margin-left: 20px; margin-top: 50px" table-layout="fixed">
    <el-table-column prop="name" label="场馆名" width="450"/>
    <el-table-column prop="seats_num" label="座位数" width="250"/>
    <el-table-column fixed="right" label="操作" width="400">
      <template #default="scope">
        <el-button
            link
            type="primary"
            size="small"
            @click.prevent="updateRow(scope.$index)"
        >
          修改场馆信息
        </el-button>

        <el-button
            link
            type="primary"
            size="small"
            style="color: red"
            @click.prevent="deleteRow(scope.$index)"
        >
          删除场馆
        </el-button>

      </template>

    </el-table-column>
  </el-table>

</template>

<script lang="ts" setup>
import {ref, onMounted} from 'vue'
import {ElMessage, ElMessageBox} from "element-plus";
import axios from 'axios';

const dialogTableVisible = ref(false)
const dialogTableVisible1 = ref(false)

const curIndex = ref(-1)

const form = ref({
  name: '',
  seats_num: 0,
})

interface Hall {
  name: string;
  seats_num: BigInt;
}

const tableData = ref<Hall[]>([]);

const addHall = () => {
  const formData = new FormData();
  for (const key in form.value) {
    formData.append(key, form.value[key]);
  }

  axios
      .post('/hall/create/', formData)
      .then((res) => {
        if (res.data.errno === 0) {
          ElMessage.success('添加成功');
          tableData.value.push(res.data.data);
          dialogTableVisible.value = false
        } else {
          if (res.data.errno === 1) ElMessage.error('场馆名不能为空');
          else if (res.data.errno === 2) ElMessage.error('添加失败(已有该场馆)');
          form.value.name = ''
          form.value.seats_num = 0
        }
      })
      .catch((error) => {
        console.error(error);
        ElMessage.error('系统错误');
      });
}

const updateHall = () => {
  const old_name = tableData.value[curIndex.value].name
  const formData = new FormData();
  for (const key in form.value) {
    formData.append(key, form.value[key]);
  }
  axios
      .post(`/hall/update/${old_name}/`, formData)
      .then((res) => {
        if (res.data.errno === 0) {
          ElMessage.success('修改成功');
          tableData.value.splice(curIndex.value, 0, res.data.data);
          tableData.value.splice(curIndex.value + 1, 1);
          dialogTableVisible1.value = false
        } else {
          if (res.data.errno === 1) ElMessage.error('场馆名不能为空');
          else if (res.data.errno === 2) ElMessage.error('修改失败(场馆名重复)');
          form.value.name = ''
          form.value.seats_num = 0
        }
      })
      .catch((error) => {
        console.error(error);
        ElMessage.error('系统错误');
      });
}

// 在组件加载时获取数据
onMounted(fetchData);

async function fetchData() {
  try {
    const response = await axios.get('/hall/index');
    tableData.value = response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

const updateRow = (index: number) => {
  dialogTableVisible1.value = true
  curIndex.value = index
}


const deleteRow = (index: number) => {
  ElMessageBox.confirm(
      '该操作会删除当前场馆，确认吗',
      '警告',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
  )
      .then(() => {
        const name = tableData.value[index].name;
        axios
            .post("/hall/delete/", {name: name})
            .then((res) => {
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

