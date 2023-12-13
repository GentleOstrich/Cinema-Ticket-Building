<script lang="ts" setup>
import {onMounted, ref} from "vue";

import {useRoute} from "vue-router";

const route = useRoute()

let movie_name = ref(null)

interface Broadcast {
  name: string;
  genre: string;
  region: string;
  lasting: string;
  image: string;
}

const broadcasts = ref<Broadcast[]>([])

onMounted(() => {
  movie_name.value = route.query.movie_name
})

const getBroadcast = () => {

}


</script>

<template>
  <div>{{ movie_name }}</div>
  <div>场次信息</div>
  <!-- 卡片风格 -->
  <el-row justify="start" :gutter="20" style="margin: 20px">
    <el-col
        v-for="broadcast in broadcasts"
        :span="6"
        style="margin-top: 10px">

      <router-link>
        <el-card>
          {{ movie.name }}
          <img :src=" 'data:image/jpeg;base64,' + movie.image"/>
        </el-card>
      </router-link>

    </el-col>
  </el-row>
  <div>订票</div>
  <router-link to="/movies/index">
    back
  </router-link>
</template>


<style scoped>

</style>