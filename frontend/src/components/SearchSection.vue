<template>
  <el-input
      v-model="searchInfo"
      class="w-50 m-2"
      size="large"
      placeholder="请输入电影名/导演名"
      :suffix-icon="Search"
  />
  <div class="demo-collapse">
    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item title="类型" name="1">
        <div style="margin-top: 0px">
          <el-radio-group v-model="radio1" size="small">
            <el-radio label="1" border="true">全部</el-radio>
            <el-radio label="2" border="true">悬疑</el-radio>
            <el-radio label="3" border="true">动作</el-radio>
            <el-radio label="4" border="true">爱情</el-radio>
          </el-radio-group>
        </div>
      </el-collapse-item>
      <el-collapse-item title="地区" name="2">
        <div style="margin-top: 0px">
          <el-radio-group v-model="radio2" size="small">
            <el-radio label="1" border="true">全部</el-radio>
            <el-radio label="2" border="true">中国大陆</el-radio>
            <el-radio label="3" border="true">港台</el-radio>
            <el-radio label="4" border="true">日韩</el-radio>
            <el-radio label="5" border="true">欧美</el-radio>
          </el-radio-group>
        </div>
      </el-collapse-item>
      <el-collapse-item title="时长" name="3">
        <div style="margin-top: 0px">
          <el-radio-group v-model="radio3" size="small">
            <el-radio label="1" border="true">全部</el-radio>
            <el-radio label="2" border="true">小于60分钟</el-radio>
            <el-radio label="3" border="true">60分钟-120分钟</el-radio>
            <el-radio label="4" border="true">大于120分钟</el-radio>
          </el-radio-group>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>

  <div v-for="(movie,index) in movies">
    <el-row style=" margin-left: 30px;">
      <el-col :span="24">
        <div v-if="checkString(movie) == true" class="grid-content ep-bg-purple" @change="$forceUpdate">
          {{ movie.fields.name }}
        </div>
      </el-col>
    </el-row>
  </div>

</template>

<script lang="ts" setup>
import {createApp, onBeforeMount, ref} from 'vue'
import {Search} from '@element-plus/icons-vue'
import {onMounted} from "vue";

import axios from "axios";
onMounted(async() => update())
const searchInfo = ref('')
const radio1 = ref('1')
const radio2 = ref('1')
const radio3 = ref('1')
const activeNames = ref([''])

const handleChange = (val: string[]) => {
  console.log(val)
}

const checkString = (movie) => {
  console.log(radio1.value)
  if (radio1.value == 1) {
    return true;
  } else if (radio1.value == 2) {
    return false;
  } else if (radio1.value == 3) {
    return false;
  }
  return true;
}

let os = []
let movies = []
const update = () => {
  axios
      .get("/movie/index/")
      .then((res) => {
        if (res.data.errno === 0) {
          movies = res.data.data
        }
      })
      .catch((error) => {
        console.log(error)
      })
}

const cond = () => {

}


</script>

