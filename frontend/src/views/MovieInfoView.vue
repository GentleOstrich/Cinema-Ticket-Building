<script lang="ts" setup>
import {onMounted, ref} from "vue";
import {ElMessage, ElMessageBox} from "element-plus";
import {useRoute, useRouter} from "vue-router";
import axios, {get} from "axios";

const route = useRoute()
const router = useRouter()
let movie_name = ref('')
let movie_image = ref('')

const goBack = () => {
  router.back()
}
const score = ref(0.0)
const myScore = score.value.toFixed()

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

const deleteFavorite = () => {
  axios
      .post(`favorite/delete/${movie_name.value}/`)
      .then((res) => {
        if (res.data.errno === 0) {
          isFavorite.value = !isFavorite.value
          ElMessage({
            message: '已取消收藏！',
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
  price: BigInt;
}

interface Movie {
  name: string;
  description: string;
  year: string;
  region: string;
  language: string;
  genre: string;
  lasting: string;
}

const broadcasts = ref<Broadcast[]>([]);
const aim_broadcast = ref<Broadcast>();
const movie = ref<Movie>();
const isFavorite = ref(false);
const fullscreenLoading = ref(true);

async function fetchBroadcast() {
  try {
    fullscreenLoading.value = true;
    movie_image.value = route.query.movie_image as string
    movie_name.value = route.query.movie_name as string
    const response = await axios.get(`/broadcast/index/${movie_name.value}/`);
    const response1 = await axios.get(`/favorite/isFavorite/${movie_name.value}/`);
    const response2 = await axios.get(`/comment/index/${movie_name.value}/`)
    const response3 = await axios.get(`/movie/show/${movie_name.value}/`);
    const response4 = await axios.get(`/comment/score/${movie_name.value}/`);
    broadcasts.value = response.data.data;
    comments.value = response2.data.data;
    movie.value = response3.data.data;
    score.value = response4.data.score;
    score.value = Number(score.value.toFixed(2));
    isFavorite.value = response1.data.code !== 0;
    fullscreenLoading.value = false;
  } catch (error) {
    fullscreenLoading.value = false;
    console.error('Error fetching data:', error);
  }
}


onMounted(() => {
  fetchBroadcast();
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

const comment_form = ref({
  content: '',
  rating: 0
})

function onSubmit() {
  // 获取评分和评论内容
  const formData = new FormData();
  for (const key in comment_form.value) {
    formData.append(key, comment_form.value[key])
  }
  console.log(comment_form.value)
  // 发送评论数据
  axios.post(`/comment/create/${movie_name.value}/`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
  ).then((response) => {
    if (response.data.errno === 0) {
      ElMessage.success('评论成功')
    } else {
      ElMessage.success('评论失败')
      comment_form.value.content = ''
      comment_form.value.rating = 0
    }
    // 评论提交成功
  }).catch((error) => {
    // 评论提交失败
    console.error(error);
    ElMessage.error('系统错误');
  });
  window.location.reload();
}

function onRatingChange() {
  comment_form.value.rating = rating.value;
  console.log(comment_form.value.rating)
}

function onContentChange() {
  comment_form.value.content = content.value;
  console.log(comment_form.value.content)
}

</script>

<template>

  <el-drawer v-model="ifshow" title="I am the title" :with-header="false">
    <el-divider style="background: black">屏幕</el-divider>
    <el-row justify="center">
      <el-col
          v-for="(i, index) in aim_broadcast.seats"
          :span="3"
      >
        <div style="margin-top: 10px">
          <el-button v-if="i == 0" style="background-color: navajowhite; margin-left: 10px"
                     @click="buy(index)"></el-button>
          <el-button v-else style="background-color: orangered; margin-left: 10px"
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
          v-model="score"
          disabled
          show-score
          text-color="#ff9900"
          score-template="{value} points"
      />
    </div>
    <!-- 收藏按钮 -->
    <div v-loading.fullscreen.lock="fullscreenLoading">
      <div style="text-align: center" v-if="!isFavorite">
        <el-button star size="mini" style="margin-top: 10px" @click="addFavorite">
          收藏
        </el-button>
      </div>
      <div style="text-align: center" v-if="isFavorite">
        <el-button star size="mini" style="margin-top: 10px" @click="deleteFavorite">
          取消收藏
        </el-button>
      </div>
    </div>
    <div style="font-size: 0.7cm">电影详情</div>
    <div class="movieInfo" style="font-size: 0.4cm; margin:14px; color: gray">
      <div>年份：{{ movie?.year }}<br/></div>
      <div>类型：{{ movie?.genre }}<br/></div>
      <div>语言：{{ movie?.language }}<br/></div>
      <div>电影简介：{{ movie?.description }}</div>
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
          <el-card style="height: 150px; margin: 30px 0 30px 0">
            <el-text>场馆名：{{ broadcast.hall_name }}<br/></el-text>
            <el-text>开始时间：{{ broadcast.beginTime }}<br/></el-text>
            <el-text>结束时间：{{ broadcast.endTime }}</el-text>
            <el-text style="margin-left: 60px; color:orangered; font-size: 0.5cm">￥{{ broadcast.price }}<br/></el-text>
            <el-button type="success" style="margin-left: 100px; margin-top: 10px"
                       @click="ifshow=!ifshow, aim_broadcast=broadcast">
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
          @change="onContentChange"
      />
      <el-button style="margin-top: 14px;" type="primary" @click="onSubmit">提交评论</el-button>

      <div class="comments" style="margin-top: 30px">
        <div class="comment" v-for="comment in comments" :key="comment.id">
          <span style="font-size: 0.5cm;"><strong>{{ comment.username }}</strong></span>
          <span style="font-size: 0.25cm; color: gray; margin-left: 100px">{{ comment.time }}<br/></span>
          <div style="margin-top: 5px; font-size: 0.3cm">评分：{{ comment.rating }}<br/></div>
          <div style="margin-top: 15px;">&nbsp;&nbsp;&nbsp;&nbsp;{{ comment.content }}<br/></div>
          <el-divider />
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


