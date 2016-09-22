#!/usr/bin/env python3
#coding:utf-8

for i in range(5):
    for j in range(10):
        if j<5:
            continue
        if i>3:
            break
        print ("i=%s,j=%s"%(i,j))