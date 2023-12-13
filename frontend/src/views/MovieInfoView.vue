<script lang="ts" setup>
import {onMounted, ref} from "vue";

import {useRoute, useRouter} from "vue-router";
import axios from "axios";
import SideColomn from "../components/SideColomn.vue";

const route = useRoute()
const router = useRouter()
let movie_name = ref(null)
const goBack = () => {
  router.back()
}

interface Broadcast {
  beginTime: String,
  endTime: String
}

const broadcasts = ref<Broadcast[]>([])

async function fetchData() {
  try {
    const response = await axios.get('/abababaabab');
    broadcasts.value = response.data.data;
    console.log(broadcasts.value[length - 1].image);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}


onMounted(() => {
  movie_name.value = route.query.movie_name
})

const getBroadcast = () => {

}
const ifshow = ref(false)

const tests = ['星期一6点', '星期二8点', '星期三10点', '星期四9点', '星期五12点']

</script>

<template>

  <el-container>
    <el-aside width="200px" v-if="ifshow">
      显示信息
    </el-aside>
    <el-container>
      <el-header>
        <el-page-header @back="goBack" style="margin: 30px 0 0 20px;">

        </el-page-header>
      </el-header>

      <el-main>
        <el-text size="large">
          {{ movie_name }}
        </el-text>
        <!-- 卡片风格 -->
        <el-row justify="start" :gutter="30" style="margin-left: 50px;margin-right: 50px">
          <el-col
              v-for="test in tests"
              :span="6">
            <el-card>
              <el-text>
                {{ test }}
              </el-text>
              <el-button style="margin-left: 100px" @click="ifshow=!ifshow">
                订票
              </el-button>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </el-container>
</template>


<style>
.el-header {
  background-color: #ffffff;
  color: #333;
  line-height: 60px;
}

.el-aside {
  background-color: #fffff;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #ffffff;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>

<!--  <template>-->
<!--  <el-container>-->
<!--    <el-aside width="200px">-->
<!--      {{ movie_name }}-->
<!--    </el-aside>-->
<!--    <el-container>-->
<!--      <el-page-header @back="goBack" style="margin: 30px 0 0 20px;">-->
<!--        <template #content>-->
<!--          <span class="text-large font-600 mr-3"> 返回电影列表 </span>-->
<!--        </template>-->
<!--      </el-page-header>-->
<!--      -->
<!--      <el-main>-->
<!--        <el-row justify="start" :gutter="30" style="margin-left: 50px;margin-right: 50px">-->
<!--          <el-col-->
<!--              v-for="test in tests"-->
<!--              :span="6">-->
<!--            <el-card>-->
<!--              <el-text>-->
<!--                {{ test }}-->
<!--              </el-text>-->
<!--              <router-link :to="{path:'/movies/index'}">-->
<!--                <el-button style="margin-left: 100px">-->
<!--                  订票-->
<!--                </el-button>-->
<!--              </router-link>-->
<!--            </el-card>-->
<!--          </el-col>-->
<!--        </el-row>-->
<!--      </el-main>-->
<!--    </el-container>-->
<!--  </el-container>-->

