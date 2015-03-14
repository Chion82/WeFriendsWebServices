import pyDes
import base64
import md5

def str_md5(src):
	m = md5.new()
	m.update(src)
	return m.hexdigest()

print("Enter sender ID")
sender = raw_input()
print("Enter message")
message = raw_input()
key = (str_md5(sender))[0:8]
des = pyDes.des(key,padmode=pyDes.PAD_PKCS5)
result = base64.b64encode(des.encrypt(message))
print("Encrypted message:")
print(result)
