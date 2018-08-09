## list of wechat
tuling.py | wechat robot, w/ Tuling backend API | http://www.tuling123.com
tuling-specUser.py | chat service, restricted for specific wechat-usergroup| https://github.com/littlecodersh/ItChat
watson-console.py | console-based example for waston-conversation
watson-wechat.py | wechat as client | https://github.com/watson-developer-cloud/python-sdk
watson-tuling-wechat.py | wechat client + 2*backends ( # for Tuling, #IBM for Watson )

## how to run
0. install python runtime
1. install itchat: pip install itchat
2. apply service from Tuling ( www.tuling123.com )
3. apply service & create conversation from IBM Bluemix ( bluemix.net )
4. install watson SDK: $ sudo -H pip install --ignore-installed six watson-developer-cloud
5. modify credentials
6. python xx.py 

## list of console
example1.js
example2.js
example3.js
example4.js

## how to run
npm install
modify credentials
nodejs exampleX.js

## list of nodered
watson-debugMode.json | waston-conversation, running in debug mode
watson-sockets.js | run in web mode, socket communication

## how to run
1. create node-red application in IBM Bluemix
2. create service watson conversion
3. launch node-red application -- web designer
4. import flow from above json
5. modifiy 'conversation' node property in these flow
debug: (1) click flow (left input node)
(2) https://nodered-jon001.eu-gb.mybluemix.net/testing
web: https://nodered-jon001.eu-gb.mybluemix.net/testing
web: https://nodered-jon001.eu-gb.mybluemix.net/testing
web: https://nodered-jon001.eu-gb.mybluemix.net/testing
