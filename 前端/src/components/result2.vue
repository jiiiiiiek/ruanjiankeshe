<template>
    <div class="mt-4">
  <el-input 
    class="input"
    v-model="input"
    placeholder="请输入要分析的视频地址..."
    clearable
    size="large"
    style="width: 600px;"
    @keyup.enter.native="toFilterData"
     >
     <template #append>
      <el-button type="primary" @click="toFilterData" v-loading.fullscreen="fullscreenLoading">分析</el-button>
      </template>
    </el-input>

    <el-descriptions
    title="视频信息"
    direction="vertical"
    :column="2"
    :size="large"
    border
  >
    <el-descriptions-item label="视频标题">{{ videotitle }}</el-descriptions-item>
    <el-descriptions-item label="发布时间">{{videotime}}</el-descriptions-item>
    <el-descriptions-item label="播放量">{{videoview}}</el-descriptions-item>
    <el-descriptions-item label="点赞">{{videolike}}</el-descriptions-item>
    <el-descriptions-item label="硬币">{{videocoin}}</el-descriptions-item>
    <el-descriptions-item label="收藏">{{videofavorite}}</el-descriptions-item>
    <el-descriptions-item label="分享">{{videoshare}}</el-descriptions-item>
  </el-descriptions>

  <div class="Table">
    <div>评论信息</div>
      <!-- 表格 -->
      <el-table :data="tableData" border stripe style="width: 100%">
        <el-table-column prop="commid" label="用户ID" width="180" />
    <el-table-column prop="commgender" label="性别" width="70" />
    <el-table-column prop="commip" label="IP地址" width="130" />
    <el-table-column prop="commtime" label="发布时间" width="180" />
    <el-table-column prop="commcontent" label="评论内容" width="180" />
    <el-table-column prop="touch" label="感动概率" width="150" />
    <el-table-column prop="surprise" label="震惊概率" width="150" />
    <el-table-column prop="amusement" label="搞笑概率" width="150" />
    <el-table-column prop="sadness" label="悲伤概率" width="150" />
    <el-table-column prop="curiosity" label="新奇概率" width="150" />
    <el-table-column prop="anger" label="愤怒概率" width="150" />
      </el-table>
      <!-- 分页器 -->
      <div class="block" style="margin-top:15px;">
        <el-pagination align='center'  @current-change="handleCurrentChange" 
          v-model:current-page="currentPage" 
          :hide-on-single-page="false"
          v-model:page-size="pageSize" 
          layout="total, prev, pager, next, jumper" 
          :page-count="total">
          </el-pagination>
      </div>
  </div>


</div>

<div class="Charts">
  <el-button type="success" size="large" @click="ShowChart" @mouseleave="(event)=>event.target.blur()">数据可视化</el-button>
  <div></div>
  <div class="mychartall" v-show="isShowing==true">
    <el-space wrap>

    <el-card style="width: 400px">
      <template #header>
        <div class="card-header">
          <span>平均情感指数</span>
        </div>
      </template>
      <div class="echart1" id="mychart1" :style="myChartStyle1"></div>
      
    </el-card>

    <el-card style="width: 500px">
      <template #header>
        <div class="card-header">
          <span>评论男女性别比例</span>
        </div>
      </template>
      <div class="echart2" id="mychart2" :style="myChartStyle2"></div>
    </el-card>

    <el-card style="width: 700px">
      <template #header>
        <div class="card-header">
          <span>评论IP地区比例</span>
        </div>
      </template>
      <div class="echart3" id="mychart3" :style="myChartStyle3"></div>
    </el-card>

  </el-space>
  </div>
  

</div>

</template>

<script>
import Axios from 'axios'
import * as echarts from "echarts";


export default{
    data(){
        return{
            input:'',
            videotitle:'',
            videotime:'',
            videoview:0,
            videolike:0,
            videocoin:0,
            videofavorite:0,
            videoshare:0,
            currentPage: 1, // 当前页码
            total: 20, // 总条数
            pageSize: 20, // 每页的数据条数
            tableData:[],
            fullscreenLoading:false,
            isShowing:false,
            myChartStyle1: { double: "left", width: "100%", height: "400px" },
            myChartStyle2: { double: "left", width: "100%", height: "400px" },
            myChartStyle3: { double: "left", width: "100%", height: "400px" },
            yData1:[],
            xData1:["感动","震惊","搞笑","悲伤","新奇","愤怒"],
            myChart1:{},
            myChart2:{},
            myChart3:{},
            piedata:[],
            piename:[],
            piedata2:[],
            piename2:[]
            


        }
    },
    methods:{
        toFilterData(){
            if(this.input == '') {
             return
        } else {
          this.fullscreenLoading=true;
            Axios.post("http://localhost:8081/PaChong",JSON.stringify({"url":this.input}),{
              headers:{
                ' content-type':'application/json'
              }
            }).then((response)=> {
              this.videotitle=response.data[0]["videotitle"];
              this.videotime=response.data[0]["videotime"];
              this.videoview=parseFloat(response.data[0]["videoview"]);
              this.videolike=parseFloat(response.data[0]["videolike"]);
              this.videocoin=parseFloat(response.data[0]["videocoin"]);
              this.videofavorite=parseFloat(response.data[0]["videofavorite"]);
              this.videoshare=parseFloat(response.data[0]["videoshare"]);
              this.fullscreenLoading=false;
              console.log(this.fullscreenLoading);
                for (let i = 0; i < response.data.length-1; i++) {
                    this.tableData[i]=response.data[i+1]
                }
                
          })
          
            
         }
        },
        
              //当前页改变时触发 跳转其他页
        handleCurrentChange(val) {
                  console.log(`当前页: ${val}`);
                  this.currentPage = val;
                  // this.fullscreenLoading=true;
                  console.log(JSON.stringify({"page0":this.currentPage}));
            Axios.post("http://localhost:8081/comm/findbypage",null,{
              params:{
                page0:val
              },
              headers:{
                ' content-type':'application/json'
              }
            }).then((response)=> {
              this.videotitle=response.data[0]["videotitle"];
              this.videotime=response.data[0]["videotime"];
              this.videoview=parseFloat(response.data[0]["videoview"]);
              this.videolike=parseFloat(response.data[0]["videolike"]);
              this.videocoin=parseFloat(response.data[0]["videocoin"]);
              this.videofavorite=parseFloat(response.data[0]["videofavorite"]);
              this.videoshare=parseFloat(response.data[0]["videoshare"]);

                for (let i = 0; i < response.data.length-1; i++) {
                    this.tableData[i]=response.data[i+1]
                }

              //  this.fullscreenLoading=false;
              console.log(this.tableData);
          })
              },
              ShowChart(){
                this.isShowing=!this.isShowing;
                this.fullscreenLoading=true;
            Axios.get("http://localhost:8081/comm/table",{
              headers:{
                ' content-type':'application/json'
              }
            }).then((response)=> {
              
              this.yData1[0]=parseFloat(response.data[0]["AVG(touch)"]);
              this.yData1[1]=parseFloat(response.data[1]["AVG(surprise)"]);
              this.yData1[2]=parseFloat(response.data[2]["AVG(amusement)"]);
              this.yData1[3]=parseFloat(response.data[3]["AVG(sadness)"]);
              this.yData1[4]=parseFloat(response.data[4]["AVG(curiosity)"]);
              this.yData1[5]=parseFloat(response.data[5]["AVG(anger)"]);
              // console.log(this.yData1)
              this.initEcharts1();

              this.piedata[0]={value:parseInt(response.data[6]["gendercount"]),name:response.data[6]["commgender"]};
              this.piedata[1]={value:parseInt(response.data[7]["gendercount"]),name:response.data[7]["commgender"]};
              this.piedata[2]={value:parseInt(response.data[8]["gendercount"]),name:response.data[8]["commgender"]};
              //console.log(this.piedata);
              this.initEcharts2();

              this.piedata2[0]={value:parseInt(response.data[9]["ipcount"]),name:response.data[9]["commip"]};
              this.piedata2[1]={value:parseInt(response.data[10]["ipcount"]),name:response.data[10]["commip"]};
              this.piedata2[2]={value:parseInt(response.data[11]["ipcount"]),name:response.data[11]["commip"]};
              this.piedata2[3]={value:parseInt(response.data[12]["ipcount"]),name:response.data[12]["commip"]};
              this.piedata2[4]={value:parseInt(response.data[13]["ipcount"]),name:response.data[13]["commip"]};
              this.piedata2[5]={value:parseInt(response.data[14]["ipcount"]),name:response.data[14]["commip"]};
              this.piedata2[6]={value:parseInt(response.data[15]["ipcount"]),name:response.data[15]["commip"]};
              this.piedata2[7]={value:parseInt(response.data[16]["ipcount"]),name:response.data[16]["commip"]};
              this.piedata2[8]={value:parseInt(response.data[17]["ipcount"]),name:response.data[17]["commip"]};
              this.piedata2[9]={value:parseInt(response.data[18]["ipcount"]),name:response.data[18]["commip"]};
              this.piedata2[10]={value:parseInt(response.data[19]["ipcount"]),name:response.data[19]["commip"]};
              this.initEcharts3();

              this.fullscreenLoading=false;
          })

              },
              initEcharts1() {
        // 基本柱状图
        const option = {
          tooltip: {
            trigger: 'axis',
            axisPointer: {
            type: 'shadow'
          }
        },
          xAxis: {
            data: this.xData1
          },
          yAxis: {},
          series: [
            {
              type: "bar", //形状为柱状图
              data: this.yData1
            }
          ]
        };
        const myChart1 = echarts.init(document.getElementById("mychart1"));
        myChart1.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
          myChart1.resize();
        });
      },
      initEcharts2(){
        // 饼图
      const option = {
         legend: {
           // 图例
           data: this.pieName,
           right: "10%",
           top: "30%",
           orient: "vertical"
         },
        series: [
          {
            type: "pie",
            label: {
              show: true,
              formatter: "{b} : {c} ({d}%)" // b代表名称，c代表对应值，d代表百分比
            },
            radius: [0,"30%"], //饼图半径
            data: this.piedata,

          }
        ]
      };
      
      this.myChart2 = echarts.init(document.getElementById("mychart2"));
      this.myChart2.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        this.myChart2.resize();
      });
      },
      initEcharts3(){
        // 饼图
      const option = {
         legend: {
           // 图例
           data: this.pieName,
           right: "10%",
           top: "30%",
           orient: "vertical"
         },
        series: [
          {
            type: "pie",
            label: {
              show: true,
              formatter: "{b} : {c} ({d}%)" // b代表名称，c代表对应值，d代表百分比
            },
            radius: [0,"40%"], //饼图半径
            data: this.piedata2,

          }
        ]
      };
      
      this.myChart3 = echarts.init(document.getElementById("mychart3"));
      this.myChart3.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        this.myChart3.resize();
      });
      }
    }
}
</script>

<style scoped>
.el-descriptions {
  margin-top: 20px;
  margin-left: 23%;
  width: 800px;
}

.Table{
    margin-top: 20px;
}

.mychartall{
  margin-top: 20px;
}
.input{
  margin-top: 20px;
}
</style>