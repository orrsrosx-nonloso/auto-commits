import requests
import http.client
import json


import datetime
#系统当前时间
current_time = datetime.datetime.now()
#json文件读取
class Read():
    def read_json(self):
        return json.load(open('hot.json',encoding="utf-8"))
    
head = {"Content-Type":"application/json; charset=UTF-8", 'Connection': 'close'}

url_d = "https://weibo.com/ajax/side/hotSearch"

# json_d = json.dumps(real_data)

res_d = requests.get(url=url_d,headers=head)

read = Read()
textJson = read.read_json()

httpJson = res_d.json()
targetData = httpJson['data']
targetReaktime = targetData['realtime']
targetHotData = targetReaktime[00]
insterJson = {'onboard_time':str(current_time),'word':targetHotData['word']}
textJson.append(insterJson)
with open('hot.json', 'w',encoding="utf-8") as f:
    json.dump(textJson, f,ensure_ascii=False)
