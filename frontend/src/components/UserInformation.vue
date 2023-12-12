<template>
  TODO: 这里应该有用户信息
  <div>
    {{ username }}
  </div>
</template>

<script lang="ts" setup>
import {onMounted, ref} from "vue";
import axios from "axios";


onMounted(() => {
  setTimeout(() => askName(), 500)
})

let username = ref(null)

function askName() {
  axios
      .post("/user/askName/")
      .then((res) => {
        if (res.data.errno === 0) {
          username.value = res.data.username
        } else {
          username.value = '大傻逼'
        }
      }).catch((error) => {
    console.log(error)
  })
}

</script>