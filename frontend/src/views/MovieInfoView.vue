<script lang="ts" setup>
import {onMounted, ref} from "vue";
import {ElMessage, ElMessageBox} from "element-plus";
import {useRoute, useRouter} from "vue-router";
import axios, {get} from "axios";
import SideColomn from "../components/SideColomn.vue";
import boolean from "async-validator/dist-types/validator/boolean";

const route = useRoute()
const router = useRouter()
let movie_name = ref('')
let movie_image = ref('')

const goBack = () => {
  router.back()
}
const getScore = () => {

}
const value = ref(3.7)


const addFavorite = () => {
  axios
      .post(`favorite/create/${movie_name.value}/`)
      .then((res) => {
        if (res.data.errno === 0) {
          isFavorite.value = !isFavorite.value
          ElMessage({
            message: '收藏成功！',
            type: 'success',
          })

        } else {

        }
      })
      .catch((error) => {
        console.error(error);
        ElMessage.error('系统错误');
      });
}

interface Broadcast {
  id: BigInt;
  hall_name: string;
  beginTime: string;
  endTime: string;
  seats: string;
}


const broadcasts = ref<Broadcast[]>([]);
const aim_broadcast = ref<Broadcast>();
const isFavorite = ref(false);

async function fetchBroadcast() {
  try {
    movie_image.value = route.query.movie_image as string
    movie_name.value = route.query.movie_name as string
    const response = await axios.get(`/broadcast/index/${movie_name.value}/`);
    const response1 = await axios.get(`/favorite/isFavorite/${movie_name.value}/`);
    broadcasts.value = response.data.data;
    isFavorite.value = response1.data.code !== '0';
    console.log(isFavorite.value)
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}


onMounted(() => {
  fetchBroadcast();
  getScore();
})


const ifshow = ref(false)


const seat = ref(null);

const buy = (index) => {
  // 新建影票并传给后端
  // 修改放映座位信息
  if (aim_broadcast.value) {
    axios
        .post(`/ticket/create/${aim_broadcast.value.id}/${index}/`)
        .then((res) => {
          if (res.data.errno === 0) {
            ElMessage.success('购票成功');
            const arr = aim_broadcast.value!.seats.split("");
            arr[index] = "1";
            aim_broadcast.value!.seats = arr.join("");
          } else {

          }
        })
        .catch((error) => {
          console.error(error);
          ElMessage.error('系统错误');
        });
  }
}

interface Ticket {
  id: BigInt;
  movie_name: string;
  beginTime: string;
  endTime: string;
  time: string;
  seat: BigInt;
}

const form = ref({
  beginTime: '',
  endTime: '',
  seats: ''
})

const rating = ref(0);
const content = ref("");
const comments = ref([]);

function getComments() {
  axios.get("/api/comments")
      .then((response) => {
        // 获取评论数据
        this.comments = response.data;
      })
      .catch((error) => {
        // 获取评论数据失败
      });
}

function onSubmit() {
  // 获取评分和评论内容
  const rating = rating.value;
  const content = content.value;

  // 发送评论数据
  axios.post("/api/comments", {
    rating,
    content,
  }).then((response) => {
    // 评论提交成功
  }).catch((error) => {
    // 评论提交失败
  });
}

function onRatingChange(value) {
  this.rating = value;
}

function star() {

}

let isStarred = false;

</script>

<template>

  <el-drawer v-model="ifshow" title="I am the title" :with-header="false">
    <el-divider style="background: black">屏幕</el-divider>
    <el-row justify="start">
      <el-col
          v-for="(i, index) in aim_broadcast.seats"
          :span="6"
      >
        <div>
          <el-button v-if="i == 0" style="background-color: navajowhite" @click="buy(index)"></el-button>
          <el-button v-else style="background-color: orangered"
                     @click="evt => ElMessageBox.alert('抱歉，此座位已售出')">
          </el-button>

        </div>
      </el-col>
    </el-row>
  </el-drawer>

  <el-page-header @back="goBack" style="margin: 30px 0 0 20px;"></el-page-header>

  <el-card class="box-card" style="margin: 10px">
    <div style="text-align: center; margin: 30px">
      <el-image
          :src=" 'data:image/jpeg;base64,' + movie_image"
          class="image"
          slot="error"
          fit="cover"
          style="max-width: 80%;max-height: 80%;width: auto;height: auto"
      />
    </div>
    <el-header style="font-size: 1cm; text-align: center">{{ movie_name }}<br/></el-header>
    <div style="text-align: center">
      <el-rate
          v-model="value"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value} points"
      />
    </div>
    <!-- 收藏按钮 -->
    <div style="text-align: center" v-if="!isFavorite">
      <el-button star size="mini" style="margin-top: 10px" @click="addFavorite">
        收藏
      </el-button>
    </div>
    <div style="font-size: 0.7cm">电影详情:</div>
    <div class="movieInfo" style="font-size: 0.4cm; margin:14px; color: gray">
      <div>年份：<br/></div>
      <div>类型：<br/></div>
      <div>语言：<br/></div>
      <div>电影简介：</div>
    </div>
  </el-card>

  <el-card class="box-card" style="margin: 10px">
    <div v-if="broadcasts.length > 0">
      <div style="margin-left: 30px; font-size: 0.5cm">场次信息：</div>
      <!-- 卡片风格 -->
      <el-row justify="start" :gutter="30" style="margin-left: 50px;margin-right: 50px">
        <el-col
            v-for="broadcast in broadcasts"
            :span="6"
            style="flex: auto">
          <el-card style="height: 100px; margin: 30px 0 30px 0">
            <el-text>场馆名：{{ broadcast.hall_name }}<br/></el-text>
            <el-text>开始时间：{{ broadcast.beginTime }}<br/></el-text>
            <el-text>结束时间：{{ broadcast.endTime }}</el-text>
            <el-button style="margin-left: 100px" @click="ifshow=!ifshow, aim_broadcast=broadcast">
              订票
            </el-button>
          </el-card>
        </el-col>
      </el-row>
    </div>
    <div v-else>
      <el-empty description="抱歉，当前电影尚未安排场次">
        <router-link to="/movies/index">
          <el-button type="primary">返回首页</el-button>
        </router-link>
      </el-empty>
    </div>
  </el-card>

  <el-card class="box-card" style="margin: 10px">
    <div class="comment-container">
      <div>为电影打分吧：</div>
      <el-rate
          v-model="rating"
          :max="5"
          show-score
          show-text
          @change="onRatingChange"
      />
      <el-input
          v-model="content"
          placeholder="请输入评论内容"
      />
      <el-button style="margin-top: 14px" type="primary" @click="onSubmit">提交评论</el-button>

      <div class="comments">
        <div class="comment" v-for="comment in comments" :key="comment.id">
          <span class="rating">评分：{{ comment.rating }}</span>
          <span class="content">{{ comment.content }}</span>
        </div>
      </div>
    </div>
  </el-card>
</template>


<style>
.el-header {
  background-color: #ffffff;
  color: #333;
  line-height: 60px;
}

.el-aside {
  background-color: #ffffff;
  color: #333;
  text-align: center;
  line-height: 100px;
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


