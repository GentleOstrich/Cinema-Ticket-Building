<template>
  <el-table :data="tableData" style="width: 10000px; margin-left: 20px; margin-top: 50px" table-layout="fixed">
    <el-table-column prop="moviename" label="电影名" width="450" />
    <el-table-column prop="moviegenre" label="类型" width="250" />
    <el-table-column prop="movieregion" label="地区" width="200" />
    <el-table-column prop="movietime" label="时长" width="200" />
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
          v-model="form.describtion"
          class="w-50 m-2"
          placeholder="请输入详细描述"
          autosize
          type="textarea"
          style="margin: 10px 0 10px 0">
      </el-input>
    </el-row>
  </div>
    <el-button @click="addMovie" style="margin-left: 670px; margin-top: 30px">确定</el-button>
  </el-dialog>


</template>

<script lang="ts" setup>
import { ref } from 'vue'


import {ElMessage, ElMessageBox} from "element-plus";
const dialogTableVisible = ref(false)
const addMovie = () => {

}

const tableData = ref([
  {
    moviename: '',
    moviegenre: '',
    movieregion: '',
    movielasting: '',
  },
])

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
      ElMessage.success('删除成功！')
      tableData.value.splice(index, 1)
    })
    .catch(() => {

    })

}
import { reactive, ref } from 'vue'

const form = reactive({
  name: '',
  region: '',
  genre: '',
  lasting: '',
  year: '',
  language: '',
  describtion: ''
})
</script>

