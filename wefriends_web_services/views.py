from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from wefriends_web_services.users import *
from django.views.decorators.csrf import csrf_exempt
from wefriends_web_services.upload import *

@csrf_exempt
def view_createUser(request):
	return createUser(request)

@csrf_exempt
def view_login(request):
	return login(request)

def view_getUserInfoByToken(request):
	return getUserInfoByToken(request)

def view_getUserInfoByWefriendsId(request):
	return getUserInfoByWefriendsId(request)

@csrf_exempt
def view_uploadFile(request):
	return uploadFile(request)

@csrf_exempt
def view_updateUserInfo(request):
	return updateUserInfo(request)

@csrf_exempt
def view_updateWhatsup(request):
	return updateWhatsup(request)

def view_getWhatsup(request):
	return getWhatsup(request)

def view_getFriendList(request):
	return getFriendList(request)

def view_getWhatsupByWefriendsId(request):
	return getWhatsupByWefriendsId(request)
