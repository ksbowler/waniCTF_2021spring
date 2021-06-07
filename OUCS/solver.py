from Crypto.Util.number import *
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

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
HOST, PORT = "oucs.cry.wanictf.org", 50010
s, f = sock(HOST, PORT)
for _ in range(10): read_until(f)
for _ in range(7): read_until(f)
read_until(f,"> ")
s.send(b"1\n")
recv_m = read_until(f).split()
c = int(recv_m[-1][2:],16)
for _ in range(8): read_until(f)
read_until(f,"> ")
s.send(b"4\n")
recv_m = read_until(f).split()
n = int(recv_m[-1][2:],16)
recv_m = read_until(f).split()
g = int(recv_m[-1][2:],16)
for _ in range(9): read_until(f)
c2 = pow(c,2,n)
read_until(f,"> ")
s.send(b"3\n")
read_until(f)
read_until(f,"> ")
s.send(str(c2).encode()+b"\n")
recv_m = read_until(f).split()
m2 = int(recv_m[-1][2:],16)
print(long_to_bytes(m2//2))
#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() or .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

