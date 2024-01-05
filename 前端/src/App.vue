<template>

<div class="back">
    <el-container>

      <el-header>
        <el-row class="mb-4">
    <el-button color="#62c8ef" size="large" type="整句情感分析模块" plain @click="Port1Show">整句情感分析模块</el-button>
    <el-button color="#626aef" size="large" type="B站评论情感分析模块" plain @click="Port2Show">B站评论情感分析模块</el-button>
        </el-row>
      </el-header>

      <el-main>
        <div v-show="isPort1Showing==true">
        <Result1></Result1>
        </div>

        <div v-show="isPort2Showing==true">
        <Result2></Result2>
        </div>
      </el-main>

    </el-container>

    <video autoplay muted loop src="./assets/back.mp4" class="video"></video>
  </div>

  


<!-- <div class="backg">
  <img :src="imgUrl" ref="img">
</div> -->


</template>

<script>
import Hello from './components/ohayo.vue'
import Button from './components/button.vue'
import Input from './components/input.vue'
import Result1 from './components/result1.vue'
import Test from './components/test1.vue'
import Result2 from './components/result2.vue'
import { ref } from 'vue'

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
      isPort1Showing:true,
      isPort2Showing:false,
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
  },
  // setup(){
  //   let timer;
  //   let imgUrl=ref(require('./assets/1.jpg'));
  //   let index=1;

  //   function setTimer(){
  //     this.timer=setInterval(()=>{
  //       this.$refs.img.style.opacity=1;
  //       index=index<2?index+1:1;
  //       this.imgUrl=require(`./assets/${index}.jpg`);
  //       setTimeout(()=>{
  //         this.$refs.img.style.opacity=0.8;
  //       },4000)
  //     },5000)
  //   }
    
  //   return{
  //     imgUrl,
  //     setTimer
  //   }
  // },
  // mounted(){
  //   this.setTimer();
  // }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align:center;
  color: #4b0533;
  margin-top: 20px;
  width: 100%;
}
.mb-4{
    margin-left: 50%;
    transform: translateX(-25%);
    margin-top: 20px;
}

.back{
  height: 100%;
  width: 100%;
}
.video{
  width: 100%;
  height: 100%;
  object-fit: fill;
  
  position: fixed;
  top: 0;
  left: 0;
  z-index: -1;
}
</style>
