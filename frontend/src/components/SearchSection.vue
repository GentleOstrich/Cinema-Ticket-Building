<template>
   <el-backtop :right="100" :bottom="100" />
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

     <!-- 卡片风格 -->
     <el-row justify="start" :gutter="20" style="margin: 20px">
      <el-col
        v-for="movie in movies"
        :span="6"
        style="margin-top: 10px"
      >
        <div v-if="checkString(movie) == true">
          <el-card>
            {{ movie.name }}
            <img :src="'data:image/jpg;base64,' + movie.image"/>
          </el-card>
        </div>
      </el-col>
    </el-row>


  <!-- <ul v-for="(movie,index) in movies" style="list-style: none">
    <li v-if="checkString(movie) == true">
      <span>{{movie.fields.name}}</span>
      <el-divider />
    </li>
  </ul> -->

<!--  <template v-for="(movie,index) in movies">-->
<!--    <el-row style=" margin-left: 30px;">-->
<!--       <div v-if="checkString(movie) == true"  @change="$forceUpdate">-->
<!--        <el-col :span="24"><div class="grid-content ep-bg-purple" />-->
<!--          {{ movie.fields.name }}-->
<!--        </el-col>-->

<!--         </div>-->
<!--       <el-divider v-if="checkString(movie) == true" />-->
<!--    </el-row>-->

<!--  </template>-->

</template>

<script lang="ts" setup>
import {createApp, onBeforeMount, ref} from 'vue'
import {Search} from '@element-plus/icons-vue'
import {onMounted} from "vue";

import axios from "axios";

interface Movie {
  name: string;
  genre: string;
  region: string;
  lasting: string;
  image: string;
}

const movies = ref<Movie[]>([]);

onMounted(fetchData);

async function fetchData() {
  try {
    const response = await axios.get('/movie/index');
    movies.value = response.data.data;
    console.log(movies.value[length - 1].image);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

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
  let genre = movie.genre
  let region = movie.region
  let lasting = movie.lasting

  let r1 = false
  let r2 = false
  let r3 = false
  if (radio1.value == 1) {
    // 全部
    r1 = true
  } else if (radio1.value == 2) {
    // 悬疑
    if (genre.indexOf("悬疑") != -1) {
      r1 = true;
    }
  } else if (radio1.value == 3) {
    // 动作
    if (genre.indexOf("动作") != -1) {
      r1 = true;
    }
  } else if (radio1.value == 4) {
    // 爱情
    if (genre.indexOf("爱情") != -1) {
      r1 = true;
    }
  }

  if (radio2.value == 1) {
    // 全部
    r2 = true
  } else if (radio2.value == 2) {
    // 中国大陆
    if (region.indexOf("中国大陆") != -1) {
      r2 = true;
    }
  } else if (radio2.value == 3) {
    // 港台
    if (region.indexOf("中国香港") != -1 || region.indexOf("中国台湾") != -1) {
      r2 = true;
    }
  } else if (radio2.value == 4) {
    // 日韩
    if (region.indexOf("日本") != -1 || region.indexOf("韩国") != -1) {
      r2 = true;
    }
  } else if (radio2.value == 5) {
    // 欧美
    if (region.indexOf("美国") != -1 || region.indexOf("法国") != -1 ||
        region.indexOf("英国") != -1 || region.indexOf("意大利") != -1 ||
        region.indexOf("澳大利亚") != -1) {
      r2 = true;
    }
  }

  let lasting_num = parseInt(lasting)
  if (radio3.value == 1) {
    // 全部
    r3 = true
  } else if (radio3.value == 2) {
    // <60
    if (lasting_num <= 60) {
      r3 = true;
    }
  } else if (radio3.value == 3) {
    // 60-120
    if (lasting_num > 60 && lasting_num <= 120) {
      r3 = true;
    }
  } else if (radio3.value == 4) {
    // >120
    if (lasting_num > 120) {
      r3 = true;
    }
  }
  return r1 && r2 && r3;
}

</script>