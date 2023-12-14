<template>

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
              <span style="font-size: 0.4cm; margin-top: 5px">{{ movie.name }}<br/></span>
              <span style="font-size: 0.2cm; color: rgb(128,128,128)">时长：{{ movie.lasting }}<br/></span>
              <span style="font-size: 0.2cm; color: rgb(128,128,128)">国家/地区：{{ movie.region }}</span>
            </div>
          </el-card>
        </router-link>
      </div>
    </el-col>
  </el-row>

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