#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

ip_port = ('127.0.0.1',9000)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
	print("server waiting...")
	conn,addr = sk.accept()
	client_data = conn.recv(1024)
	conn.sendall(bytes('connection succeed','utf-8'))
	print(str(client_data,'utf-8'))
	while True:
		client_data = conn.recv(1024)
		print(str(client_data,'utf-8'))
		server_input = input("->>")
		conn.sendall(bytes(server_input,'utf-8'))
	conn.close()