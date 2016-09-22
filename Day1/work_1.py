#!/usr/bin/env python3
#coding:utf-8

msg = '''
1.Register
2.Login
3.Quit
'''#The output when start

while True:
    break_flag = False
    break_flag2 = False
    print (msg)
    choice_1 = input()

    if choice_1 == "1":                         #Register step
        username = input("Username:")
        password = input("Password:")
        f = open("login.txt", "a")
        f.write(username+','+password+'\n')
        f.close()
        print('User "%s" has been registered!'%(username))

    if choice_1 == "2":     #Login step
        for err_count in range (3):
            username = input("Username:")       #input username
            f2 = open("locked.txt","r")         #check if this user locked
            for line in f2:
                check_username = line.strip()
                if check_username == username:
                    print("This user has been locked,please connect with administrator!")
                    break_flag2 = True
            if break_flag2:
                break
            password = input("Password:")       #input password
            f = open("login.txt", "r")
            for line in f:
                get_username = line.split(",")[0]
                if username == get_username:
                    get_password = line.split(",")[1].strip()
                    if get_password == password:
                        print ("Welcome!")
                        break_flag = True
                        break
                    else:
                        print("Failed!")
                        break
            if break_flag == True:
                break
        else:
            f2 = open("locked.txt","a")
            f2.write(username+'\n')
            f2.close()
            print('User "%s" is locked.Please connect with administrator!'%(username))
            break

    if choice_1 == "3":     #Exit
        break

    if break_flag:
        break