from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib
from sympy.ntheory.modular import crt

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

	
#HOSTはIPアドレスでも可
HOST, PORT = "crt.cry.wanictf.org", 50000
s, f = sock(HOST, PORT)
mod = []
val = []
for i in range(2,301):
	print(i)
	read_until(f,"Mod > ")
	s.send(str(i).encode()+b"\n")
	recv = int(read_until(f).strip())
	mod.append(i)
	val.append(recv)
m,_ = crt(mod,val)
print(long_to_bytes(m))


#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

