<template>
  <el-table :data="tableData" style="width: 10000px; margin-left: 20px; margin-top: 50px" table-layout="fixed">
    <el-table-column prop="fields.name" label="电影名" width="450" />
    <el-table-column prop="fields.genre" label="类型" width="250" />
    <el-table-column prop="fields.region" label="地区" width="200" />
    <el-table-column prop="fields.lasting" label="时长" width="200" />
    <el-table-column fixed="right" label="操作" width="400">
      <template #default="scope">
        <el-button
          link
          type="primary"
          size="small"
          style="color: red"
          @click.prevent="deleteRow(scope.$index)"
        >
          删除电影
        </el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-button class="mt-4" style="width: 100%" @click="dialogTableVisible = true"
    >添加电影</el-button
  >

  <el-dialog v-model="dialogTableVisible" title="新电影信息">
    <div>&nbsp;</div>
     <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >电影名</span
      >
      <el-input
        v-model="form.name"
        class="w-50 m-2"
        placeholder="请输入电影名"
        style="margin: 10px 0 10px 0"
      />
    </el-row>
  </div>
  <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >类型</span
      >
      <el-input
          v-model="form.genre"
          class="w-50 m-2"
          placeholder="请输入电影类型"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >年份</span
      >
      <el-input
          v-model="form.year"
          class="w-50 m-2"
          placeholder="请输入电影年份"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >地区</span
      >
      <el-input
          v-model="form.region"
          class="w-50 m-2"
          placeholder="请输入电影地区"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >时长（min）</span
      >
      <el-input
          v-model="form.lasting"
          class="w-50 m-2"
          placeholder="请输入电影时长"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >语言</span
      >
      <el-input
          v-model="form.language"
          class="w-50 m-2"
          placeholder="请输入电影语言"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <div class="demo-input-suffix">
    <el-row :gutter="20">
      <span class="ml-3 w-35 text-gray-600 inline-flex items-center"
        >详细描述</span
      >
      <el-input
          v-model="form.description"
          class="w-50 m-2"
          placeholder="请输入详细描述"
          autosize
          type="textarea"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <el-button @click="addMovie; dialogTableVisible = false" style="margin-left: 670px; margin-top: 30px">确定</el-button>
  </el-dialog>


</template>

<script lang="ts" setup>
import { ref,onMounted } from 'vue'
import {ElMessage, ElMessageBox} from "element-plus";
import axios from 'axios';

const dialogTableVisible = ref(false)

const form = ref({
  name: '',
  region: '',
  genre: '',
  lasting: '',
  year: '',
  language: '',
  description: ''
})

const addMovie = () => {
  axios
    .post('/movie/create/',form.value)
    .then((res) => {
      if (res.data.errno === 0) {
        ElMessage.success('添加成功');
        // 假设 res.data.movie 是新添加的电影数据
        tableData.value.push(res.data.data); // 将新电影添加到 tableData
      } else {
        ElMessage.error('添加失败');
      }
    })
    .catch((error) => {
      console.error(error);
      ElMessage.error('系统错误');
    });
}

interface Movie {
  fields: {
    name: string;
    genre: string;
    region: string;
    lasting: string;
  };
}

const tableData = ref<Movie[]>([]);

// 在组件加载时获取数据
onMounted(fetchData);

async function fetchData() {
  try {
    const response = await axios.get('/movie/index');
    tableData.value = response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
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
      const name = tableData.value[index].fields.name;
      axios
        .post("/movie/delete/",{name:name})
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

