import itchat, time, re
from itchat.content import *
import urllib2, urllib
import json
from watson_developer_cloud import ConversationV1

response={'context':{}}
@itchat.msg_register([TEXT])
def text_reply(msg):
 global response
 request_text = msg['Text'].encode('UTF-8')
 conversation = ConversationV1(
    username='9c359fba-0692-4afa-afb1-bd5bf4d7e367',
    password='5Id2zfapBV6e',
    version='2017-04-21')

 # replace with your own workspace_id
 workspace_id = 'd3e50587-f36a-4bdf-bf3e-38c382e8d63a'

 print "request ==>", request_text

 try:
	 type(eval(response))
 except:
   print "first call"
   response = conversation.message(workspace_id=workspace_id, message_input={
      'text': request_text}, context=response['context'])
 else:
   print "continue call"
   response = conversation.message(workspace_id=workspace_id, message_input={
      'text': request_text}, context=response['context'])
 
 if len( response['output']['text']) >0:
   response_text =  response['output']['text'][0]
 else: 
   response_text =  "No message"

 itchat.send( response_text, msg['FromUserName'])
  
itchat.auto_login()
itchat.run(debug=True)
