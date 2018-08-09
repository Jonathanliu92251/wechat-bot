import json
from watson_developer_cloud import ConversationV1

#########################
# message
#########################

conversation = ConversationV1(
    username='9c359fba-0692-4afa-afb1-bd5bf4d7e367',
    password='5Id2zfapBV6e',
    version='2017-04-21')

# replace with your own workspace_id
workspace_id = 'd3e50587-f36a-4bdf-bf3e-38c382e8d63a'
try:
	type(eval(reponse['context']))
except:
   response = conversation.message(workspace_id=workspace_id, message_input={'text': 'Hello'})
   print "not defined"
else:
   response = conversation.message(workspace_id=workspace_id, message_input={'text': 'Hello'}, context=response['context'])
   print "define response"

respMsg = response['output']['text']
print 'response==', response
if len(response['output']['text']) > 0:
   print response['output']['text'][0]
else:
   print "no message"


# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))
