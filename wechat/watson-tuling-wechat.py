#!/usr/bin/env python 
#-*- coding:utf-8 -*- 

import itchat, time, re
from itchat.content import *
import urllib2, urllib
import json
from watson_developer_cloud import ConversationV1

response={'context':{}}    
conversation_server ='#TURING'

@itchat.msg_register([TEXT])
def text_reply(msg):
 global conversation_server, request_text, response, response_text
 request_text = msg['Text'].encode('UTF-8')

 if request_text == '#IBM':
    conversation_server ='#IBM'
    response={'context':{}}
    itchat.send( 'Greetings from IBM Waston', msg['FromUserName'])
 
 if request_text == '#':
    conversation_server ='#TURING'
 
 # IBM Waston Conversation
 if conversation_server =='#IBM': 
    conversation = ConversationV1(
      username='9c359fba-0692-4afa-afb1-bd5bf4d7e367',
      password='5Id2zfapBV6e',
      version='2017-04-21')

    workspace_id = 'd3e50587-f36a-4bdf-bf3e-38c382e8d63a'

    response = conversation.message(workspace_id=workspace_id, message_input={
                                    'text': request_text}, context=response['context'])
 
    if len( response['output']['text']) >0:
       response_text =  response['output']['text'][0]
    else: 
       response_text =  "No message"  

    itchat.send( response_text, msg['FromUserName'])
 
 # Turling Robot
 if conversation_server =='#TURING': 
    url ='http://www.tuling123.com/openapi/api'
    request = urllib.urlencode({
      u"key":"d83cddc3894946338cccd9bb752b497e", 
      "info":request_text, 
      u"loc":r"北京市中关村", 
      "userid":""})

    url2 = urllib2.Request(url,request) 
    response = urllib2.urlopen(url2)
    apicontent = response.read()
    s = json.loads( apicontent, encoding='utf-8')

    if s['code'] == 100000:
       response_text = s['text']
    else:
       response_text = r'问住我了？你太牛啦！'
    
    itchat.send( response_text, msg['FromUserName'])
 
  
itchat.auto_login()
itchat.run(debug=True)
