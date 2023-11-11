#后续开发：
#可以将输入的视频的网址传入url变量中完成对应视频的评论的爬取
#可以对page变量进行赋值来改变获取的评论的页数，一般视频一页有20个评论
#若需要更多视频相关的信息，可以在获取视频标题的函数中，对info变量进行取值，info变量有视频的大部分信息，可直接打印查看，根据需要获取
#cookie需要定期更换，否则ip地址无法爬取出来


import requests
import re
import time
from time import sleep  # 设置等待，防止反爬
import asyncio
from bilibili_api import video
import pymysql

def Getoid(url):#获取视频的oid
   page_text=requests.get(url=url,headers=headers).text
   ex = '</script><script>window.__INITIAL_STATE__={"aid":(.*?),"bvid":'
   oid = re.findall(ex , page_text , re.S)[0]
   #print(oid)
   return oid

with open('评论.txt',mode='a',encoding='utf-8')as f:#清除上次获取的评论内容
    f.truncate(0)

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'cookie':'buvid3=6DDC9267-E037-4F57-8FD3-437F51293F4734769infoc; LIVE_BUVID=AUTO1816237618723804; CURRENT_BLACKGAP=0; blackside_state=0; buvid_fp_plain=undefined; buvid4=3D358013-A7B6-77DC-0209-C33C1CE086BC26813-022012016-qfnIW1did5Qq6LyyZbud3A%3D%3D; balh_is_closed=; balh_server_inner=__custom__; balh_mode=replace; balh_server_custom=https://repost.98e.org; i-wanna-go-back=-1; is-2022-channel=1; rpdid=|(umJmYJmJmu0J\'uYY)l)YYJR; balh_server_custom_tw=https://atri.ink; balh_server_custom_hk=https://atri.ink; nostalgia_conf=-1; CURRENT_PID=b75e3c40-cd1f-11ed-afb7-f10c75ab9c0f; hit-dyn-v2=1; _uuid=231474E3-D142-2ED1-1011E-105B8D22D339261176infoc; home_feed_column=5; browser_resolution=1707-924; i-wanna-go-feeds=-1; FEED_LIVE_VERSION=V8; hit-new-style-dyn=1; DedeUserID=32270804; DedeUserID__ckMd5=e108b290f40194d9; b_ut=5; header_theme_version=CLOSE; b_nut=100; bp_article_offset_32270804=846348650546200614; fingerprint=74a594c9034cfd39c2940079ebf76c66; SESSDATA=3153349c%2C1712039573%2C7c269%2Aa1CjCwHh6_phfuinpxjplRF3aMKfCSOLKDIDb3Gir3mDjrBG22IxwsFm3zbErWIzhWlL8SVkhYeXVqN0hTTW5ERG1hdHlYZEhjemJKUDY4cjViNFA3TDc2Sm8zbWk3Q3l5Qm5JMmJGTml0Vmd2OXo1S2tia3l2bC1lUHNyY2dubVNkUTNVZE9Fdnp3IIEC; bili_jct=727fd333e51116a2537799b22765df31; sid=8ccwn6eu; CURRENT_QUALITY=120; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY4MTgwNDgsImlhdCI6MTY5NjU1ODc4OCwicGx0IjotMX0.s8Ixk88ZDNAQJAk4wKqBH4uOYTy7yyKfYne9mmmj0tQ; bili_ticket_expires=1696817988; CURRENT_FNVAL=4048; PVID=22; bp_video_offset_32270804=849379222170370097; innersign=0; b_lsid=AB9638E4_18B0562ED38; buvid_fp=74a594c9034cfd39c2940079ebf76c66'
    }#请求头
url='https://www.bilibili.com/video/BV1JV411c7bE/?spm_id_from=333.851.b_7265636f6d6d656e64.1&vd_source=079901b9e6fa8d7726d21181e17a22b2'#视频网页地址

#主函数

bvid=re.search(r"BV.*?/",url).group()#将url中的BV号提取出来
bvid=bvid.replace('/','')#删去最后的'/'符号

async def main() -> None:#获取视频标题
    # 实例化 Video 类
    v = video.Video(bvid)
    # 获取信息
    info = await v.get_info()
    title=info['title']
    return title
if __name__ == '__main__':
    title=asyncio.get_event_loop().run_until_complete(main())

oid=Getoid(url)#获取视频oid

for page in range(5):#根据视频的oid获取视频评论

    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid='+oid+'&pn='+ str(page)#根据page的值加载不同页面的评论

    response=requests.get(url=url,headers=headers)
    for index in response.json()['data']['replies']:
        Content=index['content']['message']#评论内容

        Ctime=index['ctime']#评论时间
        ContTime=time.localtime(Ctime)#将评论时间由时间戳转换为正常计时
        FileTime=time.strftime("%Y-%m-%d %H:%M:%S",ContTime)#时间表示改为如:2023-6-3 20:15:20

        Memname=index['member']['uname']#用户名

        Memgender=index['member']['sex']#用户性别

        Memip=index['reply_control']['location']#用户ip属地
        Fileip=Memip.replace('IP属地：','')#去除获取的数据中的“IP属地”的前缀,只留下最后的实际ip属地，如湖南

        ContLike=str(index['like'])#用户评论点赞数
        with open('评论.txt',mode='a',encoding='utf-8')as f:
            f.write(Content)
            f.write('\n')
            f.write(FileTime)
            f.write('\n')
            f.write(Memname)
            f.write('\n')
            f.write(Memgender)
            f.write('\n')
            f.write(Fileip)
            f.write('\n')
            f.write(ContLike)
            f.write('\n')
    if(page%5==0):#睡眠绕过反爬
        time.sleep(1)  
      