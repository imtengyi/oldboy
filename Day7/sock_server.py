#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket
import subprocess

ip_port = ('127.0.0.1',8888)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
	print("server waiting...")
	conn,addr = sk.accept()

	while True:
		client_data = conn.recv(1024)
		if not client_data:break
		print("recv:",str(client_data,'utf-8'))
		cmd = str(client_data,'utf-8').strip()
		cmd_call = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
		cmd_result = cmd_call.stdout.read()
		if len(cmd_result) == 0:
			cmd_result = b"cmd execution has no output..."
		ack_msg = bytes('CMD_RESULT_SIZE|%s'%len(cmd_result),'utf-8')
		conn.send(ack_msg)
		client_ack = conn.recv(50)
		if client_ack.decode() == 'CLIENT_READY_TO_RECV':
			conn.send(cmd_result)
	conn.close()