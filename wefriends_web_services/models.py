from django.db import models
from mongoengine import *

# Create your models here.
 
class Users(Document):
	phone = StringField()
	email = StringField()
	password = StringField()
	gender = IntField()
	wefriendsid = StringField()
	nickname = StringField()
	intro = StringField()
	region = StringField()
	registertime = LongField()
	collegeid = StringField()
	avatar = StringField()

class Friends(Document):
	wefriendsid = StringField()
	friends = ListField()

class Tags(Document):
	wefriendsid = StringField()
	tags = ListField()

class Whatsup(Document):
	wefriendsid = StringField()
	whatsup = StringField()

class Message(Document):
	sender = StringField()
	receiver = StringField()
	message = StringField()
	timestramp = LongField()
	messagetype = StringField()

class Colleges(Document):
	collegeid = StringField()
	collegename = StringField()

class AccessToken(Document):
	token = StringField()
	wefriendsid = StringField()
	expires = LongField()
