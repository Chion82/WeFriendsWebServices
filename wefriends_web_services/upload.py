from django.http import HttpResponse
import time
import random
import os

def uploadFile(request):
	if (request.FILES.get("upfile")==None):
		return HttpResponse('{"status":-1,"message":"Invalid Input."}', {})
	fileObj = request.FILES.get("upfile")
	fileNameArr = fileObj.name.split(".")
	if (len(fileNameArr)>0):
		fileType = fileNameArr[len(fileNameArr)-1]
	else:
		fileType = ""
#	if (not fileType in ALLOWED_FILE_TYPES):
#		return HttpResponse('{"status":0,"message":"Unsupported file type."}', {})
	path = "static/upload/" + ("%d" % int(time.time())) + ("%d" % random.randint(100000,999999)) + '.' + fileType
	while (os.path.exists(os.path.split(os.path.realpath(__file__))[0] + "/" + path)):
		path = "static/upload/" + ("%d" % int(time.time())) + ("%d" % random.randint(100000,999999)) + '.' + fileType
	dest = open(os.path.split(os.path.realpath(__file__))[0] + "/" + path,'wb+')
	dest.write(fileObj.read())
	dest.close()
	return HttpResponse('{"status": 200, "message": "Success.","url": "%s"}' % path, {})
