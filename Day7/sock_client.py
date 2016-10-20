#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

ip_port = ('127.0.0.1',8888)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('client sent','utf-8'))

server_reply = sk.recv(1024)
print(server_reply)
while True:
    user_input = input(">>:").strip()
    sk.send(bytes(user_input,'utf-8'))
    server_reply = sk.recv(1024)
    print(str(server_reply,'utf-8'))
sk.close()