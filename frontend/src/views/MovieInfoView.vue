<script lang="ts" setup>
import {onMounted, ref} from "vue";
import {ElMessage, ElMessageBox} from "element-plus";
import {useRoute, useRouter} from "vue-router";
import axios from "axios";
import SideColomn from "../components/SideColomn.vue";

const route = useRoute()
const router = useRouter()
let movie_name = ref(null)
let movie_image = ref(null)

const goBack = () => {
  router.back()
}

interface Broadcast {
  id: BigInt;
  beginTime: string;
  endTime: string;
  seats: string;
}


const broadcasts = ref<Broadcast[]>([]);
const aim_broadcast = ref<Broadcast>();

async function fetchBroadcast() {
  try {
    movie_image.value = route.query.movie_image as string
    movie_name.value = route.query.movie_name as string
    const response = await axios.get(`/broadcast/index/${movie_name.value}`);
    broadcasts.value = response.data.data;
  } catch (error) {
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
  if(aim_broadcast.value){
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

// const updateBroadcast = () => {
//   const id = aim_broadcast.value.id
//   const formData = new FormData();
//   for (const key in form.value) {
//     formData.append(key, form.value[key]);
//   }
//   axios
//       .post(`/broadcast/update/${id}/`, formData)
//       .then((res) => {
//         if (res.data.errno === 0) {
//           ElMessage.success('您已成功购票');
//           router.go(0)
//         } else {
//           form.value.beginTime = ''
//           form.value.endTime = ''
//           form.value.seats = ''
//         }
//       })
//       .catch((error) => {
//         console.error(error);
//         ElMessage.error('系统错误');
//       });
// }


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
    <el-container>
      <el-header>
        <el-page-header @back="goBack" style="margin: 30px 0 0 20px;">

        </el-page-header>
      </el-header>

      <el-main>
        <el-image
            :src=" 'data:image/jpeg;base64,' + movie_image"
            class="image"
            slot="error"
            style="max-width: 100%;max-height: 100%;width: auto;height: auto"
        />
        <el-header style="font-size: 60px">{{ movie_name }}</el-header>

        <!-- 卡片风格 -->
        <el-row justify="start" :gutter="30" style="margin-left: 50px;margin-right: 50px">
          <el-col
              v-for="broadcast in broadcasts"
              :span="6"
              style="flex: auto">
            <el-card>
              <el-text>
                开始时间：{{ broadcast.beginTime }}
              </el-text>
              <el-text>
                结束时间：{{ broadcast.endTime }}
              </el-text>
              <el-button v-if="!ifshow" style="margin-left: 100px" @click="ifshow=!ifshow, aim_broadcast=broadcast">
                订票
              </el-button>
              <el-button v-else style="margin-left: 100px" @click="ifshow=!ifshow">
                取消
              </el-button>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
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

