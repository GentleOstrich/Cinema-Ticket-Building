<template>
    <div class="center">
        <el-container>
            <el-header>
                Header
                <HomeHeader></HomeHeader>
            </el-header>
            <el-main>
                Main
                <router-view></router-view>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import HomeHeader from "@/components/HomeHeader.vue";
export default {
    name: "MainHome",
    components: {
        HomeHeader
    }
}
</script>