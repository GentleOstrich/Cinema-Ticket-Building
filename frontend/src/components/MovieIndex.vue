<template>
    <div v-for="(movie,index) in movies">
        
        <el-row style=" margin-left: 30px;">
            <el-col :span="24" ><div class="grid-content ep-bg-purple" />{{ movie.fields.name }}</el-col>
        </el-row>
    </div>
</template>

<script> 
    import axios from "axios"
    export default {
        data(){
            movies:[]//等待存放后端数据的接收数组
        },
        mounted(){
            this.update();//在html加载完成后进行，相当于在页面上同步显示后端数据
        },
        methods:{
            update(){
                axios
                .get("/movie/index/")
                .then((res) => {
                    if (res.data.errno === 0) {
                        this.movies = res.data.data
                    }
                })
                .catch((error) => {
                    console.log(error)
                })
            },
        },
    };
</script>

<style>
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>