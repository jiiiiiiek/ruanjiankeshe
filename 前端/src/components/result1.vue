<template>
<div class="mt-4">
  <el-input 
    class="input"
    v-model="input"
    placeholder="请输入要分析的句子..."
    clearable
    size="large"
    style="width: 600px;"
    @keyup.enter.native="toFilterData"
     >
     <template #append>
      <el-button type="primary" @click="toFilterData" v-loading.fullscreen.lock="fullscreenLoading">分析</el-button>
      </template>
    </el-input>
</div>
  

    <el-card class="box-card">
    <div type="情感分型柱状图" class="text item">{{ '情感分析柱状图' }}</div>
    <div class="echart" id="mychart" :style="myChartStyle"></div>
  </el-card>
</template>

<script>
import * as echarts from "echarts";
import Axios from 'axios'
import { ref } from 'vue'
import { Loading } from "element-plus/es/components/loading/src/service";
  
  export default {
    data() {
      return {
        input : '',
        xData: ["感动","震惊","搞笑","悲伤","新奇","愤怒"], //横坐标
        yData: [], //数据
        fullscreenLoading:false,
        myChartStyle: { double: "left", width: "100%", height: "400px" } //图表样式
      };
    },
    mounted() {
    },
    methods: {
      initEcharts() {
        // 基本柱状图
        const option = {
          tooltip: {
          trigger: 'axis',
          axisPointer: {
          type: 'shadow'
          }
        },
          xAxis: {
            data: this.xData
          },
          yAxis: {},
          series: [
            {
              type: "bar", //形状为柱状图
              data: this.yData
            }
          ]
        };
        const myChart = echarts.init(document.getElementById("mychart"));
        myChart.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
          myChart.resize();
        });
      },
      toFilterData(){
            if(this.input == '') {
             return
        } else {
          this.fullscreenLoading=true;
            Axios.post("http://localhost:8081/AnaContent",JSON.stringify({"content":this.input}),{
              headers:{
                ' content-type':'application/json'
              }
            }).then((response)=> {
              
              this.yData[0]=parseFloat(response.data[0]["touch"]);
              this.yData[1]=parseFloat(response.data[1]["surprise"]);
              this.yData[2]=parseFloat(response.data[2]["amusement"]);
              this.yData[3]=parseFloat(response.data[3]["sadness"]);
              this.yData[4]=parseFloat(response.data[4]["curiosity"]);
              this.yData[5]=parseFloat(response.data[5]["anger"]);
              this.initEcharts();
              this.fullscreenLoading=false;
          })
           
            
         }
        }
    }
  };
</script>

<style scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
  margin-top: 20px;
  margin-left: 33%;
}
</style>