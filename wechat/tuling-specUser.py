#http://www.tuling123.com/member/center/, 2497427853@qq.com/Passw0rd
#layout: http://blog.csdn.net/thx9537/article/details/54850038
#itchat: http://www.cnblogs.com/hzpythoner/p/7099022.html
#sample source: https://pan.baidu.com/s/1bpAJk0B

#!/usr/bin/env python
# coding:utf8

import itchat, time, re
from itchat.content import *
import urllib2, urllib
import json

@itchat.msg_register([TEXT,SHARING], isGroupChat=True)
def text_reply(msg):

 # 消息来自于哪个群聊
 chatroom_id = msg['FromUserName']
 # 发送者的昵称
 username = msg['ActualNickName']

 if msg['Type'] == TEXT:
  info = msg['Content'].encode('UTF-8')
 elif msg['Type'] == SHARING:
  info = msg['Text'].encode('UTF-8')


 # 消息并不是来自于需要同步的群
 if chatroom_id !=  chatroom_ids:
  print 'not monitored'
  print msg
  return


# info = msg['Text'].encode('UTF-8')
 url ='http://www.tuling123.com/openapi/api'
 data={u"key":"d83cddc3894946338cccd9bb752b497e", "info":info, u"loc":"", "userid":""}
 data = urllib.urlencode(data)

 url2 = urllib2.Request(url,data)
 
 response = urllib2.urlopen(url2)

 apicontent = response.read()
 s = json.loads( apicontent, encoding='utf-8')
 print 's==',s
 if s['code'] == 100000:
  itchat.send( s['text'], msg['FromUserName'])

  
itchat.auto_login()

chatrooms = itchat.get_chatrooms()
chatrooms_ids = '' 

for item in chatrooms:
 if item['NickName'] == u'家人':
  chatroom_ids = item['UserName']
  print item['NickName']
  print chatroom_ids
 
itchat.run(debug=True)
