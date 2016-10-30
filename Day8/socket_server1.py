#!/usr/bin/env python3

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New Conn:", self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data:break
            print("Client Says:",data.decode())
            self.request.send(data)

if __name__ == '__main__':
    HOST,PORT = 'localhost',50007
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()