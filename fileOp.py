import json;
import requests;

# 写入公告到本地文件
# data 要写入的内容
def writeToNoticeFile(data):
    with open('notice.txt','w',encoding='utf-8') as f: 
        result = f.write(str(data));
        f.close();
        msg = '写入成功';
        if result == False :
            msg = '写入失败';
        print (msg);   
# 读取本地文件内容
# resault 返回存储在本地的文件内容
def readFileNoice():
    f=open('notice.txt','r',encoding='utf-8')
    readText = f.read();
    f.close();
     
    readText = readText.replace('\'','\"');
    readText = readText.replace('\n','');
    if len(readText) < 1:
        return False;
    
    readNoticeArray = json.loads(readText);
   
    return readNoticeArray;

def rebot(msg):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    url='https://oapi.dingtalk.com/robot/send?access_token=ed67643de366bb6d9a917a87707fa1dbcd038d5933df99c7b7fc7de70a5571a5';
    data = {
        'msgtype':'text',
        'conversationType':'2',
        'text':{
            'content':msg,
        },
        "at": {
            "atMobiles": [
                "18609263478"
            ],
            "isInAtList": True,
            "isAtAll": False
        }
        
        
    };
    requests.post(url,json.dumps(data),headers=headers);

# rebot('公告小狗');