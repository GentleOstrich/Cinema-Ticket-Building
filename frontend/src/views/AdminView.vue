<template>
    <AdminHeader></AdminHeader>
    <router-view></router-view>
</template>

<script lang="ts" setup>
import AdminHeader from '../components/AdminHeader.vue'
</script>

<style>
  * {
    background: lightyellow;
  }
</style>