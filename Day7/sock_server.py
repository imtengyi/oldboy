#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

ip_port = ('127.0.0.1',8888)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
	print("server waiting...")
	conn,addr = sk.accept()

	client_data = conn.recv(1024)
	print(str(client_data,'utf-8'))
	conn.sendall(bytes('server sent','utf-8'))
	while True:
		client_data = conn.recv(1024)
		print(str(client_data,'utf-8'))
		server_response = input("\033[31:1m>>:\033[0m").strip()
		conn.send(bytes(server_response,'utf-8'))
	conn.close()