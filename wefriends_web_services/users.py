from django.http import HttpResponse
from mongoengine import *
from wefriends_web_services.models import * 
import time
from wefriends_web_services.validator import *
from wefriends_web_services.shortcuts import *
from wefriends_webserver.settings import ACCESS_TOKEN_EXPIRES
import random
import json

PHONE_EXISTS = 0
EMAIL_EXISTS = 1
COLLEGEID_INVALID = 2
OK = 200

def createUser(request):
	phone = urlencode(request.POST.get("phone"))
	email = urlencode(request.POST.get("email"))
	password = urlencode(request.POST.get("password"))
	gender = urlencode(request.POST.get("gender"))
	wefriendsId = urlencode(request.POST.get("wefriendsid"))
	nickname = urlencode(request.POST.get("nickname"))
	intro = urlencode(request.POST.get("intro"))
	region = urlencode(request.POST.get("region"))
	registerTime = long(time.time())
	collegeId = urlencode(request.POST.get("collegeid"))
	avatar = "/static/avatars/default.png"

	if ( (not validateParam(phone)) or (not validateParam(wefriendsId)) or (not validateParam(password)) or (not validateParam(nickname)) or (not validateParam(region)) or (not validateParam(collegeId)) or (not validateParam(gender)) or (gender!='0' and gender!='1')):
		return HttpResponse('{"status": -1, "message": "Invalid input."}')

	if (Users.objects(wefriendsid=wefriendsId).count() > 0):
		return HttpResponse('{"status": 0, "message": "WeFriends ID exists."}')

	if (Users.objects(phone=phone).count() > 0 or Users.objects(email=email).count() > 0):
		return HttpResponse('{"status": 1, "message": "Phone number or E-mail address exists."}')

	if (not Colleges.objects(collegeid=collegeId).count() > 0):
		return HttpResponse('{"status": 2, "message": "College ID invalid."}')

	DBUsers = Users()
	DBFriends = Friends()
	DBTags = Tags()
	DBWhatsup = Whatsup()

	DBUsers.phone = phone
	DBUsers.email = email
	DBUsers.password = str_md5(password)
	DBUsers.gender = int(gender)
	DBUsers.wefriendsid = wefriendsId
	DBUsers.nickname = nickname
	DBUsers.intro = intro
	DBUsers.region = region
	DBUsers.registertime = registerTime
	DBUsers.collegeid = collegeId
	DBUsers.avatar = avatar
	DBUsers.save()

	DBFriends.wefriendsid = wefriendsId
	DBFriends.friends = []
	DBFriends.save()

	DBTags.wefriendsid = wefriendsId
	DBTags.tags = []
	DBTags.save()

	DBWhatsup.wefriendsid = wefriendsId
	DBWhatsup.whatsup = ''
	DBWhatsup.save()

	accessToken = generateAndSaveAccessToken(wefriendsId)
	return HttpResponse('{"status": 200, "accesstoken": "%s", "message": "User successfully created."}' % accessToken)

def login(request):
	phone=urlencode(request.POST.get("phone"))
	email=urlencode(request.POST.get("email"))
	wefriendsId=urlencode(request.POST.get("wefriendsid"))
	password=urlencode(request.POST.get("password"))
	
	if (((not validateParam(phone)) and (not validateParam(email)) and (not validateParam(wefriendsId))) or (not validateParam(password))):
		return HttpResponse('{"status": -1, "message": "Invalid input."}')
	
	if (phone != None):
		objUsers = Users.objects(phone=phone)
	elif (wefriendsId != None):
		objUsers = Users.objects(wefriendsid=wefriendsId)
	else:
		objUsers = Users.objects(email=email)
	
	if (objUsers.count() == 0):
		return HttpResponse('{"status": 404, "message": "Phone number or E-mail address or WeFriends ID doesn\'t exist."}')
	
	if (str_md5(password) != objUsers.first().password):
		return HttpResponse('{"status": 403, "message": "Password incorrect."}')

	wefriendsId = objUsers.first().wefriendsid
	token = generateAndSaveAccessToken(wefriendsId)
	userInfo = json.loads(Users.objects(wefriendsid=wefriendsId).only("gender","wefriendsid","nickname","intro","region","collegeid", "phone", "email", "avatar").first().to_json())
	userInfo["whatsup"] = Whatsup.objects(wefriendsid=wefriendsId).first().whatsup
	return HttpResponse('{"status": 200, "accesstoken": "%s", "message": "Successfully logged in.", "userinfo": %s}' % (token, json.dumps(userInfo)))

def getUserInfoByToken(request):
	if (not authenticateAccessToken(request.GET.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = getWefriendsIdByToken(request.GET.get("accesstoken"))
	userInfo = json.loads(Users.objects(wefriendsid=wefriendsId).only("gender","wefriendsid","nickname","intro","region","collegeid", "phone", "email", "avatar").first().to_json())
	userInfo["whatsup"] = Whatsup.objects(wefriendsid=wefriendsId).first().whatsup
	return HttpResponse('{"status": 200, "message": "OK", "userinfo": %s}' % json.dumps(userInfo))

def getUserInfoByWefriendsId(request):
	if (not authenticateAccessToken(request.GET.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = urlencode(request.GET.get("wefriendsid"))
	if (not validateParam(wefriendsId)):
		return HttpResponse('{"status": -1, "message": "Wefriends ID not specified."}')
	if (Users.objects(wefriendsid=wefriendsId).count() == 0):
		return HttpResponse('{"status": 404, "message": "Wefriends ID not found."}')
	userInfo = getUserInfo(wefriendsId)
	return HttpResponse('{"status": 200, "message": "OK", "userinfo": %s}' % json.dumps(userInfo))

def updateUserInfo(request):
	if (not authenticateAccessToken(request.POST.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	userInfoRaw = request.POST.get("userinfo")
	if (not validateParam(userInfoRaw)):
		return HttpResponse('{"status": -1, "message": "Invalid input."}')
	userInfo = json.loads(userInfoRaw)
	print(userInfo)
	wefriendsId = getWefriendsIdByToken(request.POST.get("accesstoken"))
	status = updateUserInfoByDict(userInfo,wefriendsId)
	if (status == PHONE_EXISTS):
		return HttpResponse('{"status": 0, "message": "Phone number exists."}')
	elif (status == EMAIL_EXISTS):
		return HttpResponse('{"status": 1, "message": "E-mail address exists."}')
	elif (status == COLLEGEID_INVALID):
		return HttpResponse('{"status": 2, "message": "College ID invalid."}')
	return HttpResponse('{"status": 200, "message": "User info successfully updated."}')

def updateWhatsup(request):
	if (not authenticateAccessToken(request.POST.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	whatsup = urlencode(request.POST.get("whatsup"))
	if (whatsup==None):
		whatsup=""
	wefriendsId = getWefriendsIdByToken(request.POST.get("accesstoken"))
	Whatsup.objects(wefriendsid=wefriendsId).update(set__whatsup=whatsup)
	return HttpResponse('{"status": 200, "message": "What\'s up successfully updated."}')

def getWhatsup(request):
	if (not authenticateAccessToken(request.GET.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = getWefriendsIdByToken(request.GET.get("accesstoken"))
	whatsup = Whatsup.objects(wefriendsid=wefriendsId).first().whatsup
	return HttpResponse('{"status":200,"message":"OK","whatsup":"%s"}' % whatsup)

def getFriendList(request):
	if (not authenticateAccessToken(request.GET.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = getWefriendsIdByToken(request.GET.get("accesstoken"))
	friendListObj = Friends.objects(wefriendsid=wefriendsId).first().friends
	friendList = []
	for friend in friendListObj:
		if (Users.objects(wefriendsid=friend["wefriendsid"]).count() != 0):
			friendDetails = getUserInfo(friend["wefriendsid"])
			friendDetails["friendgroup"] = friend["friendgroup"]
			friendList.append(friendDetails)
	return HttpResponse('{"status":200,"message":"OK","friendlist":%s}' % json.dumps(friendList))

def getWhatsupByWefriendsId(request):
	if (not authenticateAccessToken(request.GET.get("accesstoken"))):
		return HttpResponse('{"status": 403, "message": "Access token invalid."}')
	wefriendsId = urlencode(request.GET.get("wefriendsid"))
	if (not validateParam(wefriendsId)):
		return HttpResponse('{"status": -1, "message": "Invalid input."}')
	if (Users.objects(wefriendsid=wefriendsId).count() == 0):
		return HttpResponse('{"status": 404, "message": "Wefriends ID not found."}')
	whatsup = Whatsup.objects(wefriendsid=wefriendsId).first().whatsup
	return HttpResponse('{"status":200,"message":"OK","whatsup":"%s"}' % whatsup)

######################################################################
####################	Internal-call Methonds	######################
######################################################################


def generateAndSaveAccessToken(wefriendsId):
	if (AccessToken.objects(wefriendsid=wefriendsId).count()>0):
		AccessToken.objects(wefriendsid=wefriendsId).delete()
	source = str(long(time.time())) + str(random.randint(1000000,9999999))
	token = str_md5(source)
	DBToken = AccessToken()
	DBToken.token = token
	DBToken.wefriendsid = wefriendsId
	DBToken.expires = long(time.time()) + ACCESS_TOKEN_EXPIRES
	DBToken.save()
	return token

def getUserInfo(wefriendsId):
	userInfo = json.loads(Users.objects(wefriendsid=wefriendsId).only("gender","wefriendsid","nickname","intro","region","collegeid", "avatar").first().to_json())
	userInfo["whatsup"] = Whatsup.objects(wefriendsid=wefriendsId).first().whatsup
	return userInfo

def getWefriendsIdByToken(token):
	return AccessToken.objects(token=token).first().wefriendsid

def authenticateAccessToken(token):
	if (token == None or token == ""):
		return False
	if (AccessToken.objects(token=token).count() == 0):
		return False
	if (AccessToken.objects(token=token).first().expires < int(time.time())):
		return False
	if (Users.objects(wefriendsid=getWefriendsIdByToken(token)).count() == 0):
		return False
	return True

def updateUserInfoByDict(userInfo, wefriendsId):
	db = Users.objects(wefriendsid=wefriendsId)
	if ("phone" in userInfo):
		if (Users.objects(phone=urlencode(userInfo["phone"])).count() > 0):
			return PHONE_EXISTS
		db.update(set__phone=urlencode(userInfo["phone"]))
	if ("email" in userInfo):
		if (Users.objects(email=urlencode(userInfo["email"])).count() > 0):
			return EMAIL_EXISTS
		db.update(set__email=urlencode(userInfo["email"]))
	if ("gender" in userInfo):
		if (int(urlencode(userInfo["gender"])) == 0):
			db.update(set__gender=0)
		else:
			db.update(set__gender=1)
	if ("nickname" in userInfo):
		db.update(set__nickname=urlencode(userInfo["nickname"]))
	if ("intro" in userInfo):
		db.update(set__intro=urlencode(userInfo["intro"]))
	if ("region" in userInfo):
		db.update(set__region=urlencode(userInfo["region"]))
	if ("collegeid" in userInfo):
		if (Colleges.objects(collegeid=urlencode(userInfo["collegeid"])).count()==0):
			return COLLEGEID_INVALID
		db.update(set__collegeid=urlencode(userInfo["collegeid"]))
	if ("avatar" in userInfo):
		db.update(set__avatar=urlencode(userInfo["avatar"]))
	return OK

