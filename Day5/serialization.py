#!/usr/bin/env python3
import pickle

def login():
	print("login")

f = open("user_acc.txt","wb")
user_info = {
	'jack':'123',
	'alex':'456'
	'func':login
}
f.write(pickle.dumps(user_info))
f.close()


f = open("user_acc.txt","rb")
data_from_atm = pickle.loads(f.read())
print(data_from_atm)