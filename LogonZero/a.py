from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long
from os import urandom
from pwn import remote
from json import dumps

choices = {1: "authenticate", 2:"reset_connection", 3:"reset_password"}
def sendreq(choice, s = ""):
	payload = {"option" : choices[choice]}
	if choice == 1:
		payload["password"] = s
	elif choice == 3:
		payload["token"] = s
	r.sendline(dumps(payload))

r = remote("socket.cryptohack.org", 13399)
print(r.recvline().decode())

msg = "00" * 28
password = ""
while True:
	try:
		sendreq(3, msg)
		print(r.recv(4096))
		sendreq(1, password)
		res = r.recv(4096)
		print (res)
		if b"crypto" in res:
			break
		sendreq(2)
		print(r.recv(4096))
	except:
		r = remote("socket.cryptohack.org", 13399)
		print(r.recvline().decode())