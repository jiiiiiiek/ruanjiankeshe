<template>

<el-row class="mb-4">
    <el-button color="#62c8ef" size="large" type="整句情感分析模块" plain @click="Port1Show">整句情感分析模块</el-button>
    <el-button color="#626aef" size="large" type="B站评论情感分析模块" plain @click="Port2Show">B站评论情感分析模块</el-button>
  </el-row>
<div v-show="isPort1Showing==true">
<Result1></Result1>
</div>

<div v-show="isPort2Showing==true">
<Result2></Result2>
</div>

</template>

<script>
import Hello from './components/ohayo.vue'
import Button from './components/button.vue'
import Input from './components/input.vue'
import Result1 from './components/result1.vue'
import Test from './components/test1.vue'
import Result2 from './components/result2.vue'

export default {
  name: 'App',
  components: {
    Hello,
    Button,
    Input,
    Result1,
    Test,
    Result2
  },
  data(){
    return{
      isPort1Showing:false,
      isPort2Showing:false
    }
  },
  methods:{
    Port1Show(){
      this.isPort1Showing=true;
      this.isPort2Showing=false;
    },
    Port2Show(){
      this.isPort1Showing=false;
      this.isPort2Showing=true;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.mb-4{
    margin-left: 50%;
    transform: translateX(-25%);
}
</style>
