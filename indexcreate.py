#coding:utf-8
 
import webbrowser
import json
 
#命名生成的html
GEN_HTML = "index.html" 
 
#打开文件，准备写入
f = open(GEN_HTML,'w',encoding="utf-8")
 
#准备相关变量

class Read():
    def read_json(self):
        return json.load(open('hot.json',encoding="utf-8"))
jsonData = Read().read_json()
#  <html>
# <head></head>
# <body>
# <p>%s</p>
# <p>%s</p>
# </body>
# </html>
# 写入HTML界面中
message = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>demo</title>
</head>

<body>
    <div id="box">
    """
message2 = """"""
for item in jsonData:
    str1 = item['onboard_time']
    str2 = item['word']
    message2 = message2 + """
        <ul>
            <li style="padding-top: 10px;">
                time:%s<br> Popular first1:%s
            </li>
        </ul>
    """%(str1,str2)

message3 = """
    </div>
</body>
<script type="text/javascript">
</script>
<style>
</style>
</html>
"""
messageEnd = message + message2 + message3
#写入文件
f.write(messageEnd) 
 
#关闭文件
f.close()