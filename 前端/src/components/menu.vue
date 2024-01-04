<template>
    <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >

    <el-menu-item index="0">
      <img
        style="width: 100px"
        src=""
        alt="Element logo"
      />
    </el-menu-item>

    <div class="flex-grow" />
    <el-menu-item index="1">整句情感分析模块</el-menu-item>
    <el-menu-item index="2">B站评论情感分析模块</el-menu-item>
    <el-menu-item index="3">表格功能</el-menu-item>

  </el-menu>
</template>

<script>
import { ref } from 'vue'
export default{
    data(){
        return{
            activeIndex : ref('1'),
            handleSelect : (key: string, keyPath: string[]) => {console.log(key, keyPath)}
        }
    }
}
</script>