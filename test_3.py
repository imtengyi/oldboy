#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

ip_port = ('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip_port)
sk.sendall(bytes('connection succeed','utf-8'))
server_reply = sk.recv(1024)
print(str(server_reply,'utf-8'))
while True:
	client_input = input("->>")
	sk.sendall(bytes(client_input,'utf-8'))
	server_reply = sk.recv(1024)
	print(str(server_reply,'utf-8'))