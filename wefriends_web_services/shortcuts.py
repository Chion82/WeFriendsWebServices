import md5
from django.utils.http import urlquote,urlunquote

def str_md5(src):
	m = md5.new()
	m.update(src)
	return m.hexdigest()

def urlencode(str):
	if (str == None):
		return None
	return urlquote(str)

def urldecode(str):
	if (str == None):
		return None
	return urlunquote(str)
