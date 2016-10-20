#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import socket

ip_port = ('127.0.0.1',9000)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)