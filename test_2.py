#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

ip_port = ('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('client sent','utf-8'))
server_reply = sk.recv(1024)
print(str(server_reply,'utf-8'))