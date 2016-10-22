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
        elif int(user_choice) in [1,2,3,4,5,6,7]:
            conn.send(bytes(user_choice,'utf-8'))
        else:
            print("Input error,please choose again!")
            continue