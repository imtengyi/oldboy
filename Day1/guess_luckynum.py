#!/usr/bin/env python3
#coding:utf-8

lucky_num = 19
input_num = -1
guess_count = 0

while guess_count < 3:
    input_num = int(input("Please input a number:"))
    if lucky_num > input_num:
        print ("You should guess bigger")
    elif lucky_num < input_num:
        print ("You should guess smaller")
    else:
        print ("Bingo!")
        break
    guess_count += 1
else:
    print ("Too many retries.")