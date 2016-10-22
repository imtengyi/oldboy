#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

def auth(sk):
    while True:
        print("server waiting...")
        conn,addr = sk.accept()
        print("link coming",addr)
        auth_msg_recv = conn.recv(1024)
        auth_msg = str(auth_msg_recv,'utf-8').split('|')
        user = auth_msg[0]
        password = auth_msg[1]

        with open('auth_msg', 'r') as f:
            for read_file in f:
                true_user = read_file.split('|')[0]
                if user == true_user:
                    true_password = read_file.split('|')[1].strip('\r\n')
                    if password == true_password:
                        conn.sendall(bytes('1', 'utf-8'))
                        print("user [%s] connected"%user)
                        return list((user,conn,addr))
                    else:
                        conn.sendall(bytes('0', 'utf-8'))
                        continue
            else:
                conn.sendall(bytes('0', 'utf-8'))