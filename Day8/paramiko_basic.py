#!/usr/bin/env python3
__author__ = 'dmmjy9'

import paramiko

# private_key = paramiko.RSAKey.from_private_key_file('/home/dmmjy9/.ssh/id_rsa')

ssh = paramiko.SSHClient()		#create a 'ssh' object
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())	#allow to connect hosts not in 'know_hosts' file
ssh.connect(hostname='localhost',port=22,username='dmmjy9',password='123')	#connect to server
stdin,stdout,stderr = ssh.exec_command('df')	#send command
result = stdout.read()		#get result
ssh.close()		#close connection