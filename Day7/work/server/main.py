#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import sys
import subprocess
import socket
import functions
from server_login import auth

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
        abs_user_dir = '/home/dmmjy9/ftp_user/'
        user_dir = abs_user_dir + user
        print("user directory is:",user_dir)
        conn.sendall(bytes("Welcome [%s] to our ftp server!"%user,'utf-8'))

        while True:
            user_choice_recv = conn.recv(1024)
            user_choice = str(user_choice_recv, 'utf-8')
            if user_choice == '0':
                conn.close()
                print("user [%s] disconnected"%user)
                break
            elif user_choice == '1':
                print("user [%s] command:list_dir"%user)
                list_dir_res = functions.list_dir(user_dir)
                conn.sendall(bytes(list_dir_res,'utf-8'))
            elif user_choice == '2':
                dir_name = str(conn.recv(1024),'utf-8')
                mkdir_res = functions.mkdir(user_dir,dir_name)
                if mkdir_res:
                    conn.sendall(bytes('1','utf-8'))
                else:
                    conn.sendall(bytes('0','utf-8'))
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