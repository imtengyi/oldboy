#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket
import sys

from client_login import auth

if __name__ == '__main__':
    conn = auth()
    print("Waiting welcome message...")
    welcome_msg = conn.recv(1024)
    print(str(welcome_msg,'utf-8'))

    while True:
        user_choice = input('''
        0:Quit
        1:List
        2:Make Directory
        3:Enter Directory
        4:Quit Directory
        5:Upload File
        6:Download File
        7:Delete File
    Please input your choice:''')
        if user_choice == '0':
            conn.send(bytes('0','utf-8'))
            sys.exit()
        elif user_choice == '1':
            conn.send(bytes('1','utf-8'))
            get_res = conn.recv(1024)
            print(str(get_res,'utf-8'))
            input("Press Enter to continue...")
        elif user_choice == '2':
            conn.send(bytes('2','utf-8'))
            mk_dir_name = input("Directory name:")
            conn.send(bytes(mk_dir_name,'utf-8'))
            get_res = conn.recv(1024)
            if str(get_res,'utf-8') == '1':
                print("success")
            elif str(get_res,'utf-8') == '0':
                print("failure")
            input("Press Enter to continue...")