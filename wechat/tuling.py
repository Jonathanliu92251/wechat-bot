import itchat, time, re
from itchat.content import *
import urllib2, urllib
import json

@itchat.msg_register([TEXT])
def text_reply(msg):
 info = msg['Text'].encode('UTF-8')
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
itchat.run(debug=True)
