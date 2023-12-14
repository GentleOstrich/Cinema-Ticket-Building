<template>

  <div v-if="movies.length > 0">
    <!-- 卡片风格 -->
    <el-row justify="start" :gutter="20" style="margin: 20px">
    <el-col
        v-for="movie in movies"
        :span="4"
        style="margin-top: 20px"
    >
      <div>
        <router-link :to="{path:'/movies/index/movie_info', query:{movie_name:movie.name, movie_image:movie.image}}"
                     style="text-decoration: none; color: inherit">
          <el-card :body-style="{ padding: '0px' }" style="width: 190px">
            <el-image
                :src=" 'data:image/jpeg;base64,' + movie.image"
                class="image"
                slot="error"
                style="height: 266px"
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
  <div v-else style="text-align: center">
    <el-empty description="抱歉，当前尚未收藏电影">
            <router-link to="/movies/index">
              <el-button type="primary">前往首页</el-button>
            </router-link>
          </el-empty>
        </div>
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
    const response = await axios.get('/favorite/index/');
    movies.value = response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

interface Movie {
  name: string;
  genre: string;
  region: string;
  lasting: string;
  image: string;
}

const movies = ref<Movie[]>([]);

</script>

<style>
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