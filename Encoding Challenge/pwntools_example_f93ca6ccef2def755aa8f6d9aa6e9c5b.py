from pwn import * # pip install pwntools
import json
import base64
from binascii import*
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

          
received = json_recv()
    
to_send = {
    
    }
json_send(to_send)




