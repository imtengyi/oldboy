#!/usr/bin/env python3
__author__ = 'dmmjy9'

class MyTCPHandler(SocketServer.BaseRequestHandler):
    print('\033[32;1mStarting CrazyFTP server on %s:%s......\n\033[Om'%(main.))
    response_code_list = {
        '200':"Pass authentication!",
        '201':"Wrong username or password",
        '202':"Invalid username or password",
        '300':"Ready to send file to client",
        '301':"Client ready to receive file data",
        '302':"File doesn't exist"
    }

    def handle(self):
        while True:
            data = self.request.recv(1024)
            print("---->data:",data)
            if not data:
                print("\033[31;1mHas lost client\033[0m",self.client_address)
                break
            self.instruction_allowcation(data)

    def instructon_allowcation(self,instructions):
        instructions = instructions.split("|")
        function_str = instructions[0]
        if hasattr(self,function_str):
            func = getatr(self,function_str)
            func(instructions)
        else:
            print("\033[31;1mReceived invalid instruction [%")

    def file_get(self,user_data):
        print("\033[32;1m---client get file----\033[0m")
        if self.login_user:
            filename_with_path = json.loads(user_data[1])
            file_abs_path = "%s/%s/%s"%(settings.USER_HOME,slef)