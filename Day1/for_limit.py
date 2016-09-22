#!/usr/bin/env python3
#coding:utf-8

lucky_num = 19
input_num = -1

for guess_count in range (3):
    input_num = int(input("Please input a number:"))
    if lucky_num > input_num:
        print ("You should guess bigger")
    elif lucky_num < input_num:
        print ("You should guess smaller")
    else:
        print ("Bingo!")
        break
else:
    print ("Too many retries.")