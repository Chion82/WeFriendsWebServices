import socket
from mongoengine import *
import threading
import time
from wefriends_web_services.models import *

server_ip = '0.0.0.0'
server_port = 38700
server_max_conn = 512

def runClientThread(sock,addr):
	clientAddr = addr[0]
	print('New connection accepted: IP = '+clientAddr)
	wefriendsId = sock.recv(1024).replace('\r\n','')
	print('Update-request from ' + clientAddr + ' received. wefriendsId = '+wefriendsId)
	if (Users.objects(wefriendsid=wefriendsId).count()==0):
		print('Client Error: wefriendsId "' + wefriendsId + '" not exists. Dropping connection.')
		sock.close()
		return
	timeCount = 0
	while True:
		if (pushNotification(sock,wefriendsId)==False):
			dropConnection(sock,clientAddr)
			break;
		time.sleep(1)
		timeCount = timeCount + 1
		if (timeCount == 60):
			if (sendHeartBeatPackage(sock)==False):
				dropConnection(sock,clientAddr)
				break;
			timeCount = 0

def pushNotification(sock, wefriendsId):
	wefriendsIdList = []
	wefriendsIdList.append(wefriendsId)
	if (Messages.objects(receivers=wefriendsId,ishandled__nin=wefriendsIdList).count()>0):
		print('New message found. Pushing notification. wefriendsId = ' + wefriendsId)
		sock.send('1')
		if (not sock.recv(4)):
			return False
	return True

def sendHeartBeatPackage(sock):
	sock.send('0')
	if (not sock.recv(4)):
		return False
	else:
		return True

def dropConnection(sock,clientAddr):
	print('Connection from ' + clientAddr + ' closed. Exiting thread.')
	sock.close()	

def main():
	listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listeningSock.bind((server_ip,server_port))
	listeningSock.listen(server_max_conn)
	connect('wefriends')
	print('Server listening at ' + server_ip + ':' + str(server_port))
	while True:
		sock, clientAddr = listeningSock.accept()
		clientThread = threading.Thread(target=runClientThread,args=(sock, clientAddr))
		clientThread.start()

if __name__=='__main__' :
	main()
