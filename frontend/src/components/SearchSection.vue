<template>
  <el-backtop :right="100" :bottom="100"/>
  <div class="demo-collapse">
    <el-collapse v-model="activeNames" @change="handleChange" style="margin: 0 10px 0 10px">
      <el-collapse-item title="类型" name="1">
        <div style="margin-top: 0px">
          <el-radio-group v-model="radio1" size="small" @change="findMovies">
            <el-radio label="1" border="true">全部</el-radio>
            <el-radio label="2" border="true">悬疑</el-radio>
            <el-radio label="3" border="true">动作</el-radio>
            <el-radio label="4" border="true">爱情</el-radio>
          </el-radio-group>
        </div>
      </el-collapse-item>
      <el-collapse-item title="地区" name="2">
        <div style="margin-top: 0px">
          <el-radio-group v-model="radio2" size="small" @change="findMovies">
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
          <el-radio-group v-model="radio3" size="small" @change="findMovies">
            <el-radio label="1" border="true">全部</el-radio>
            <el-radio label="2" border="true">小于60分钟</el-radio>
            <el-radio label="3" border="true">60分钟-120分钟</el-radio>
            <el-radio label="4" border="true">大于120分钟</el-radio>
          </el-radio-group>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>

  <div style="position: relative;">
  <div v-loading="loading" style="position: absolute; top: 100px; left: 0; right: 0; z-index: 10;">
    <!-- 加载动画的容器，可能需要根据实际情况调整宽度和高度 -->
  </div>
  <!-- 卡片风格 -->
  <el-row justify="start" :gutter="20" style="margin: 20px; padding-top: 20px;">
    <el-col
        v-for="movie in temp"
        :span="4"
        style="margin-top: 20px"
    >
      <div>
        <router-link :to="{path:'/movies/index/movie_info', query:{movie_name:movie.name, movie_image:movie.image}}"
                     style="text-decoration: none; color: inherit">
          <el-card :body-style="{ padding: '0px' }" style="width: 200px">
            <el-image
                :src=" 'data:image/jpeg;base64,' + movie.image"
                class="image"
                slot="error"
                style="height: 280px"
            />
            <div style="padding: 14px">
              <span style="font-size: 0.45cm; margin-top: 5px">{{ movie.name }}<br/></span>
              <span style="font-size: 0.25cm; color: rgb(128,128,128)">时长：{{ movie.lasting }}<br/></span>
              <span style="font-size: 0.25cm; color: rgb(128,128,128)">国家/地区：{{ movie.region }}</span>
            </div>
          </el-card>
        </router-link>
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

const loading = ref(true);

interface Movie {
  name: string;
  genre: string;
  region: string;
  lasting: string;
  image: string;
}

const movies = ref<Movie[]>([]);
const myMovies = ref<Movie[]>([])
let temp = myMovies
onMounted(fetchData);

async function fetchData() {
  try {
    loading.value = true;
    const response = await axios.get('/movie/index');
    movies.value = response.data.data;
    myMovies.value = movies.value
    loading.value = false
  } catch (error) {
    loading.value = false
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

const findMovies = () => {
  temp.value = []
  for (let i = 0; i < movies.value.length; i++) {
    checkString(movies.value[i])
  }
  console.log(temp.value.length)
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
    if (region.indexOf("中国大陆") != -1 || region.indexOf("中国") != -1) {
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
  if (r1 && r2 && r3) {
    temp.value.push(movie)
  }
}


</script>

<style>
body {
  margin: 0;
}
.example-showcase .el-loading-mask {
  z-index: 9;
}

.demo-image__error .block {
  padding: 30px 0;
  text-align: center;
  border-right: solid 1px var(--el-border-color);
  display: inline-block;
  width: 49%;
  box-sizing: border-box;
  vertical-align: top;
}

.demo-image__error .demonstration {
  display: block;
  color: var(--el-text-color-secondary);
  font-size: 14px;
  margin-bottom: 20px;
}

.demo-image__error .el-image {
  padding: 0 5px;
  max-width: 300px;
  max-height: 200px;
  width: 100%;
  height: 200px;
}

.demo-image__error .image-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: var(--el-fill-color-light);
  color: var(--el-text-color-secondary);
  font-size: 30px;
}

.demo-image__error .image-slot .el-icon {
  font-size: 30px;
}

.image {
  width: 100%;
  display: block;
}
</style>