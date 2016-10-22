#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import sys
import subprocess
import socket
from server_login import auth
from functions.list_dir import list_dir

if __name__ == '__main__':
    ip_port = ('127.0.0.1',9000)
    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(5)
    while True:
        auth_return = auth(sk)
        user = auth_return[0]
        conn = auth_return[1]
        addr = auth_return[2]
        conn.sendall(bytes("Welcome [%s] to our ftp server!"%user,'utf-8'))

        while True:
            user_choice_recv = conn.recv(10)
            user_choice = str(user_choice_recv, 'utf-8')
            print(user_choice)
            if user_choice == '0':
                conn.close()
                print("user [%s] disconnected"%user)
                break
            elif user_choice == '1':
                list_dir_res = list_dir()
                conn.sendall(bytes(list_dir_res,'utf-8'))
            elif user_choice == '2':
                mkdir()
            elif user_choice == '3':
                enter_dir()
            elif user_choice == '4':
                quit_dir()
            elif user_choice == '5':
                up_file()
            elif user_choice == '6':
                down_file()
            elif user_choice == '7':
                del_file()