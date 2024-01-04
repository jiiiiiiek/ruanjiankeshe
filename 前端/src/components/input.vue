<template>
  <div class="Table">
      <!-- 表格 -->
      <el-table :data="tableData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border stripe style="width: 100%">
        <el-table-column prop="commid" label="用户ID" width="180" />
    <el-table-column prop="commgender" label="性别" width="180" />
    <el-table-column prop="commip" label="IP地址" width="180" />
    <el-table-column prop="commtime" label="发布时间" width="180" />
    <el-table-column prop="commcontent" label="评论内容" width="180" />
    <el-table-column prop="touch" label="感动概率" width="180" />
    <el-table-column prop="surprise" label="震惊概率" width="180" />
    <el-table-column prop="amusement" label="搞笑概率" width="180" />
    <el-table-column prop="sadness" label="悲伤概率" width="180" />
    <el-table-column prop="curiosity" label="新奇概率" width="180" />
    <el-table-column prop="anger" label="愤怒概率" width="180" />
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

</template>

<script>
      export default {
          data() {
              return {
                  tableData: [{"commid":"哗啦划拉啦","commgender":"保密","commip":"四川","commtime":"2024-01-02 14:44:22","commcontent":"我现在直接把有摇一摇广告的app卸载了来一个卸载一个我长期用bili的app也是可以关如果关不了我汤姆直接不用艹","touch":0.06237911805510521,"surprise":0.3626896142959595,"amusement":0.34351396560668945,"sadness":0.06954412162303925,"curiosity":0.05925437808036804,"anger":0.10261881351470947},{"commid":"AGUAP","commgender":"保密","commip":"上海","commtime":"2023-12-31 17:59:55","commcontent":"iPad端b站还有摇一摇广告服了","touch":0.13709062337875366,"surprise":0.17743436992168427,"amusement":0.40865179896354675,"sadness":0.07215864956378937,"curiosity":0.09343279898166656,"anger":0.11123176664113998},{"commid":"bili_251976623","commgender":"男","commip":"江苏","commtime":"2023-12-27 22:19:32","commcontent":"我们这一块确实遥遥领先","touch":0.22160600125789642,"surprise":0.21782146394252777,"amusement":0.17248736321926117,"sadness":0.19006606936454773,"curiosity":0.08921424299478531,"anger":0.10880487412214279},{"commid":"Cackt","commgender":"保密","commip":"江苏","commtime":"2023-12-22 13:08:47","commcontent":"陀螺仪在我手机就没开过方向锁定我一直都是锁住的","touch":0.03910812363028526,"surprise":0.2800072431564331,"amusement":0.44617730379104614,"sadness":0.08105837553739548,"curiosity":0.04618331044912338,"anger":0.10746560990810394},{"commid":"天廻龙的净虹瞳","commgender":"女","commip":"辽宁","commtime":"2023-12-21 22:57:57","commcontent":"这就是我买手机之前必须先看能不能刷rom的理由","touch":0.09509989619255066,"surprise":0.31080636382102966,"amusement":0.33607563376426697,"sadness":0.0969628244638443,"curiosity":0.05646073818206787,"anger":0.10459452122449875},{"commid":"老实人是吗","commgender":"保密","commip":"广西","commtime":"2023-12-21 19:16:07","commcontent":"对于广告投送方来说这手段太好用了怎么可能放弃怪我咯","touch":0.07426490634679794,"surprise":0.23261196911334991,"amusement":0.3348705470561981,"sadness":0.1365470141172409,"curiosity":0.08527348935604095,"anger":0.13643209636211395},{"commid":"ケチャップソース","commgender":"女","commip":"北京","commtime":"2023-12-21 15:13:57","commcontent":"高情商舆论太温和低情商这届网友攻击性太低小电视笑","touch":0.040524162352085114,"surprise":0.06847875565290451,"amusement":0.5361341238021851,"sadness":0.04865262284874916,"curiosity":0.15946485102176666,"anger":0.14674551784992218},{"commid":"安德斯蛋","commgender":"保密","commip":"河南","commtime":"2023-12-21 07:49:54","commcontent":"这种人就是应该在春晚现场表演腰斩的","touch":0.054664719849824905,"surprise":0.23874159157276154,"amusement":0.39746370911598206,"sadness":0.12258253246545792,"curiosity":0.06784184277057648,"anger":0.11870556324720383},{"commid":"左眼桃花开","commgender":"男","commip":"黑龙江","commtime":"2023-12-20 22:04:50","commcontent":"别的不说菜鸟就很执着","touch":0.26480424404144287,"surprise":0.24340514838695526,"amusement":0.20163539052009583,"sadness":0.14432619512081146,"curiosity":0.05092553049325943,"anger":0.09490349143743515},{"commid":"奶茶额度不足","commgender":"保密","commip":"北京","commtime":"2023-12-20 20:14:00","commcontent":"都什么app会摇一摇跳转啊我好像很久没遇到过了但总看到有人玩梗","touch":0.32212868332862854,"surprise":0.08895064145326614,"amusement":0.2774287760257721,"sadness":0.14632338285446167,"curiosity":0.0725092738866806,"anger":0.09265925735235214},{"commid":"千年老疯","commgender":"保密","commip":"江苏","commtime":"2023-12-20 15:55:18","commcontent":"等到有一天某人把自家广告的跳过换成跳转doge","touch":0.11303138732910156,"surprise":0.2036343812942505,"amusement":0.4042099416255951,"sadness":0.10370802879333496,"curiosity":0.07765820622444153,"anger":0.097757987678051},{"commid":"Myronlyn","commgender":"保密","commip":"江西","commtime":"2023-12-20 15:20:42","commcontent":"现在不是摇一摇现在是屏幕前倾一下就跳转了","touch":0.06506872177124023,"surprise":0.2280251383781433,"amusement":0.4309203624725342,"sadness":0.09365181624889374,"curiosity":0.07023606449365616,"anger":0.11209779977798462},{"commid":"非常坏四叶草","commgender":"保密","commip":"湖南","commtime":"2023-12-20 12:56:50","commcontent":"扣一复活牢大扣二复活陈超扣25获得一半小布丁","touch":0.1570451557636261,"surprise":0.17860835790634155,"amusement":0.19071824848651886,"sadness":0.1483822613954544,"curiosity":0.11255393177270889,"anger":0.2126920372247696},{"commid":"チーズマン","commgender":"保密","commip":"江苏","commtime":"2023-12-20 12:55:59","commcontent":"现在又有了","touch":0.06584296375513077,"surprise":0.2081499993801117,"amusement":0.329511433839798,"sadness":0.11546320468187332,"curiosity":0.1208314299583435,"anger":0.16020096838474274},{"commid":"波仔想去海边","commgender":"男","commip":"四川","commtime":"2023-12-20 12:47:09","commcontent":"吃瓜说白了大家伙容忍度太高了只要没做得太绝都还能忍一手而且国内像这类的问题没有什么高效的反馈处理渠道藏狐有意见也就只能网上发发牢骚","touch":0.08471380174160004,"surprise":0.14279833436012268,"amusement":0.4761071503162384,"sadness":0.08768027275800705,"curiosity":0.09387832880020142,"anger":0.1148221418261528},{"commid":"比利稥","commgender":"男","commip":"安徽","commtime":"2023-12-20 09:55:08","commcontent":"遥遥领先","touch":0.47176340222358704,"surprise":0.04350151866674423,"amusement":0.12998661398887634,"sadness":0.15242403745651245,"curiosity":0.08254296332597733,"anger":0.11978152394294739},{"commid":"Andrew阿霖","commgender":"保密","commip":"海南","commtime":"2023-12-20 08:20:31","commcontent":"已经快一月份了ios广告满天都是是","touch":0.556593656539917,"surprise":0.02001151442527771,"amusement":0.1986868977546692,"sadness":0.026071660220623016,"curiosity":0.14068195223808289,"anger":0.05795436352491379},{"commid":"他们叫我凶手","commgender":"保密","commip":"安徽","commtime":"2023-12-19 20:22:43","commcontent":"小米表示我笑了","touch":0.0790143683552742,"surprise":0.20351096987724304,"amusement":0.5081331133842468,"sadness":0.03799186646938324,"curiosity":0.09637448191642761,"anger":0.07497519999742508},{"commid":"清炖鸽子精","commgender":"保密","commip":"福建","commtime":"2023-12-19 16:08:03","commcontent":"今天又中招了是这两个老登寻道大千京东","touch":0.22107762098312378,"surprise":0.1984795480966568,"amusement":0.26005974411964417,"sadness":0.14775076508522034,"curiosity":0.067497119307518,"anger":0.10513525456190109},{"commid":"魔幻实现","commgender":"男","commip":"河北","commtime":"2023-12-19 15:24:02","commcontent":"总结没有监管法律不管","touch":0.04639821499586105,"surprise":0.4540770649909973,"amusement":0.2719624638557434,"sadness":0.08564415574073792,"curiosity":0.052917201071977615,"anger":0.0890008732676506}],
                  currentPage: 1, // 当前页码
                  total: 20, // 总条数
                  pageSize: 400 // 每页的数据条数
              };
          },
          methods: {
              //每页条数改变时触发 选择一页显示多少行
              
              //当前页改变时触发 跳转其他页
              handleCurrentChange(val) {
                  console.log(`当前页: ${val}`);
                  this.currentPage = val;
              }
          }
      };
</script>

