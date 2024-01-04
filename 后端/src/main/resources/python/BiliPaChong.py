#cookie需要定期更换，否则ip地址无法爬取出来

import requests
import re
import time
import asyncio
import pymysql
from TesanNLP import TeNLP
from bilibili_api import video


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'cookie':'buvid3=6DDC9267-E037-4F57-8FD3-437F51293F4734769infoc; LIVE_BUVID=AUTO1816237618723804; CURRENT_BLACKGAP=0; blackside_state=0; buvid_fp_plain=undefined; buvid4=3D358013-A7B6-77DC-0209-C33C1CE086BC26813-022012016-qfnIW1did5Qq6LyyZbud3A%3D%3D; balh_is_closed=; balh_server_inner=__custom__; balh_server_custom=https://repost.98e.org; i-wanna-go-back=-1; is-2022-channel=1; nostalgia_conf=-1; CURRENT_PID=b75e3c40-cd1f-11ed-afb7-f10c75ab9c0f; hit-dyn-v2=1; _uuid=231474E3-D142-2ED1-1011E-105B8D22D339261176infoc; i-wanna-go-feeds=-1; FEED_LIVE_VERSION=V8; hit-new-style-dyn=1; DedeUserID=32270804; DedeUserID__ckMd5=e108b290f40194d9; b_ut=5; b_nut=100; enable_web_push=DISABLE; header_theme_version=CLOSE; balh_mode=default; balh_server_custom_tw=https://atri.ink; balh_server_custom_hk=https://atri.ink; home_feed_column=5; fingerprint=3f36e1bdf272f979054c73f8ce68e91a; rpdid=|(umJmYJmluk0J\'u~|Julum|~; CURRENT_QUALITY=120; browser_resolution=1707-906; CURRENT_FNVAL=4048; SESSDATA=c0d32180%2C1719659596%2C2d7a7%2A11CjCR9wxEPZVpZ794hgI_6jr_wLRg5E5ZMq61y4ZKPbqOet_eAJzBRMj3KT0MCWII_AgSVmlxTWZKS0hUM3hybUM4NkZ3RjdOT1VsSW9rSkd5M1lIRmd2MG1PY2p3ZUJNMEVVZUhNUUgyUFVmUGdQUVRIQW13OEZlYlJkOXFJVS02dEZKYjdJek13IIEC; bili_jct=d38e3b9a8b611383f16e48ebb6c59726; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ0MjE3MDIsImlhdCI6MTcwNDE2MjQ0MiwicGx0IjotMX0.pKCA9VqIgXSujhFC42HdYO-fGfEa6-2reNIzQpAVyAQ; bili_ticket_expires=1704421642; PVID=2; bp_video_offset_32270804=882654176374423593; b_lsid=A27B7655_18CD3554F2F; sid=p3u03n75; buvid_fp=6DDC9267-E037-4F57-8FD3-437F51293F4734769infoc'
}
def Getoid(url):#获取视频的oid
    page_text=requests.get(url=url,headers=headers).text
    ex = '</script><script>window.__INITIAL_STATE__={"aid":(.*?),"bvid":'
    oid = re.findall(ex , page_text , re.S)[0]
    return oid

#主函数

f=open("F:\\testweb\\demo\\src\\main\\resources\\python\\url.txt",'r')
url=f.readline()
f.close()
bvid=re.search(r"BV.*?/",url).group()#将url中的BV号提取出来
bvid=bvid.replace('/','')#删去最后的'/'符号

async def main() -> None:#获取视频标题
    # 实例化 Video 类
    v = video.Video(bvid)
    # 获取信息
    info = await v.get_info()
    return info
if __name__ == '__main__':
    info=asyncio.get_event_loop().run_until_complete(main())
    vtitle=info['title']#视频标题
    vtime=info['ctime']#视频时间
    vtime=time.localtime(vtime)
    vtime=time.strftime("%Y-%m-%d %H:%M:%S",vtime)#视频时间转换
    vdesc=info['desc']
    vview=info['stat']['view']#视频播放量
    vlike=info['stat']['like']#视频点赞数
    vcoin=info['stat']['coin']#视频投币数
    vfavor=info['stat']['favorite']#视频收藏数
    vshare=info['stat']['share']#视频转发数

db=pymysql.connect(host='localhost',user='root',password='root',database='test',charset='utf8')#连接数据库的video表
cursor=db.cursor()
sql="truncate table video"
cursor.execute(sql)#清除表中全部数据
sql="insert into video value(%s,%s,%s,%s,%s,%s,%s)"
value=(str(vtitle),str(vtime),int(vview),int(vlike),int(vcoin),int(vfavor),int(vshare))
cursor.execute(sql,value)
db.commit()
db.close()#关闭数据库

oid=Getoid(url)#获取视频oid

touch=float(0.1)
surprise=float(0.2)
amusement=float(0.3)
sadness=float(0.4)
curiosity=float(0.5)
anger=float(0.6)


res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")


db=pymysql.connect(host='localhost',user='root',password='root',database='test',charset='utf8')#连接数据库
cursor=db.cursor()
sql="truncate table comment"
cursor.execute(sql)#清除表中全部数据

content=[]
comtime=[]
commid=[]
commgender=[]
comip=[]

for page in range(1,21):#根据视频的oid获取视频评论

    url = 'https://api.bilibili.com/x/v2/reply?type=1&oid='+oid+'&pn='+ str(page)#根据page的值加载不同页面的评论

    response=requests.get(url=url,headers=headers)
    for index in response.json()['data']['replies']:
        Commcontent=index['content']['message']#评论内容
        commcontent=re.sub(res,'',Commcontent)
        content.append(commcontent)


        Commtime=index['ctime']#评论时间
        ContTime=time.localtime(Commtime)#将评论时间由时间戳转换为正常计时
        commTime=time.strftime("%Y-%m-%d %H:%M:%S",ContTime)#时间表示改为如:2023-6-3 20:15:20
        comtime.append(commTime)

        commid.append(index['member']['uname'])#用户名

        commgender.append(index['member']['sex'])#用户性别

        Memip=index['reply_control']['location']#用户ip属地
        commip=Memip.replace('IP属地：','')#去除获取的数据中的“IP属地”的前缀,只留下最后的实际ip属地，如湖南

        comip.append(commip)



num=len(content)
out=TeNLP(content)
for i in range(num):
    touch=out[i][0]
    surprise=out[i][1]
    amusement=out[i][2]
    sadness=out[i][3]
    curiosity=out[i][4]
    anger=out[i][5]
    sql="insert into comment value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value=(str(commid[i]),str(commgender[i]),str(comip[i]),str(comtime[i]),str(content[i]),float(touch),float(surprise),float((amusement)),float(sadness),float(curiosity),float(anger))
    cursor.execute(sql,value)#将爬到的数据插入数据库中
    db.commit()
db.close()#关闭数据库

