from django.http import HttpResponse
from mongoengine import *
from wefriends_web_services.models import * 
import time
from wefriends_web_services.validator import *
from wefriends_web_services.shortcuts import *
import random
import json
from wefriends_web_services.users import *

def sendInstantMessage(request):
	if (not authenticateAccessToken(request.POST.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = getWefriendsIdByToken(request.POST.get("accesstoken"))
	messageType = request.POST.get("messagetype")
	timeStramp = long(time.time())
	receivers = request.POST.get("receivers").split('|')
	message = urlencode(request.POST.get("message"))
	chatGroup = urlencode(request.POST.get("chatgroup"))
	if (messageType==None or messageType=='' or receivers==None):
		return HttpResponse('{"status": -1, "message": "Invalid input."}')
	if (chatGroup == None):
		chatGroup=""
	msgDb = Messages()
	msgDb.sender = wefriendsId
	receiverList = []
	for receiver in receivers:
		receiverList.append(urlencode(receiver))
	msgDb.receivers = receiverList
	msgDb.message = message
	msgDb.timestramp = timeStramp
	msgDb.messagetype = messageType
	msgDb.chatgroup = chatGroup
	msgDb.ishandled = []
	msgDb.save()
	return HttpResponse('{"status":200,"message":"OK"}')

def getNewMessages(request):
	if (not authenticateAccessToken(request.GET.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = getWefriendsIdByToken(request.GET.get("accesstoken"))
	wefriendsIdList = []
	wefriendsIdList.append(wefriendsId)
	msgDb = Messages.objects(receivers=wefriendsId,ishandled__nin=wefriendsIdList)
	messageCount = msgDb.count()
	resultList = []
	for msg in msgDb.all():
		msgJSON = json.loads(msg.to_json())
		userObj = Users.objects(wefriendsid=msg.sender)
		if (userObj.count() > 0):
			msgJSON['sendernickname'] = userObj.first().nickname
			msgJSON['senderavatar'] = userObj.first().avatar
		else:
			msgJSON['sendernickname'] = '[User deleted]'
			msgJSON['senderavatar'] = 'static/avatars/default.png'		
		resultList.append(msgJSON)
	response = HttpResponse('{"status": 200,"count": %d,"messages" : %s }' % (messageCount,json.dumps(resultList)))
	msgDb.update(push__ishandled=wefriendsId)
	return response
