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


</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {Search} from '@element-plus/icons-vue'

const searchInfo = ref('')
const radio1 = ref('1')
const radio2 = ref('1')
const radio3 = ref('1')
const activeNames = ref([''])
const handleChange = (val: string[]) => {
  console.log(val)
}
</script>

