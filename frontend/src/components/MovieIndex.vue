<template>
    <div v-for="(item, index) in items">
        <el-row style=" margin-left: 30px;">
            <el-col :span="24" ><div class="grid-content ep-bg-purple" />{{ item.index }}</el-col>
        </el-row>
    </div>
</template>

<script lang="ts" setup> 
const items = [
        {
            index: 1,
        },
        {
            index: 2
        },
        {
            index: 3
        },
        {
            index: 4
        },
        {  
            index: 5
        }
    ]
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