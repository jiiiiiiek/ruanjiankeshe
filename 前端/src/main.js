import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import Echarts from 'echarts'


const app = createApp(App)

app.use(ElementPlus)
app.use(Echarts)
app.mount('#app')

