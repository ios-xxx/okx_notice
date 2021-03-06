from pyquery import PyQuery as pq
import time,pytz,datetime
import json

import fileOp as fOp



currentTime = int(time.time());

mainUrl = 'https://www.okx.com';
url = mainUrl +'/v2/support/home/web?t='+str(currentTime);
proxy = {'http':'127.0.0.1:1080'};

headers = { 
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "cookie":'first_ref=https%3A%2F%2Fwww.google.com%2F; _gcl_au=1.1.1261197483.1654319563; _ga=GA1.2.1673855962.1654319566; u_pid=D6D6lm9rEC5jB70; _gid=GA1.2.814265221.1654684447; locale=zh_CN; defaultLocale=zh_CN; amp_56bf9d=DUHNWARGMJuJM9ctn3Fzts...1g52ti76o.1g52tps3h.m.2.o',
            "accept-language":'zh-CN'
           };
# res = requests.get(url);
doc = pq(url,encoding='utf-8',headers=headers);

noticeArray =  json.loads(doc.text())['data']['notices'];

readNoticeArray = fOp.readFileNoice();

if readNoticeArray ==False : 
    
        fOp.writeToNoticeFile(noticeArray)
    
# 记录是否有新的公告
isNewNotice = False;

currentDate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime());
currentDateStr = time.mktime(datetime.datetime.strptime(currentDate,'%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.timezone('Asia/Shanghai')).timetuple());
currentDateStr =  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(currentDateStr));  
length = len(noticeArray);

for i in range(0,length) :
    obj = noticeArray[i];
    title = obj['title'];
    publishTime = obj['publishDate']/1000;
    publishDate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(publishTime));
    fileObj = None;
    fileTime = 0.0;
    
    if readNoticeArray != False and len(readNoticeArray) > 0:
        fileObj = readNoticeArray[0];
        fileTime = fileObj['publishDate']/1000;
    
    # fCurrentTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(fileTime));
    
    if publishTime != fileTime :
        print(title,'\n',publishDate);
        
        isNewNotice = True;
        
        msg = '公告:\t\n\t{}\n\t{}\n\t发送:{}\n\t上线:{}\n\t'.format(title,mainUrl+obj['link'],currentDateStr,publishDate);
        fOp.rebot(msg,False);
    break;    
 
if isNewNotice == False:
    msg = "\t没有新公告\n\t";
    print(msg) ;
    fOp.rebot(msg,True) ;
# exit(0);
fOp.writeToNoticeFile(noticeArray); 


           
        
        