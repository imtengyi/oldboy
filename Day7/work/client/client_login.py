#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket
import sys

def auth():
    while True:
        ip = input("Host Address:")
        ip_port = (ip,9000)
        sk = socket.socket()
        sk.connect(ip_port)
        user = input("username:")
        password = input("password:")
        sk.send(bytes('%s|%s'%(user,password),'utf-8'))
        auth_res_recv = sk.recv(1024)
        auth_res = str(auth_res_recv,'utf-8')
        if auth_res == '1':
            print("succeed")
            return sk
        elif auth_res == '0':
            print("username or password error")
            sk.close()
            continue