#!/usr/bin/env python3

def binary_search(data_source,find_n):
    mid = int(len(data_source)/2)
    if mid > 1:
        if data_source[mid] > find_n:
            print("data in left of [%s]"%data_source)
            binary_search(data_source[:mid],find_n)
        elif data_source[mid] < find_n:
            print("data in right of [%s]"%data_source)
            binary_search(data_source[mid:],find_n)
        else:
            print("found find_s",data_source[mid])
    else:
        print("cannot find")

if __name__ == '__main__':
    data = list(range(1,600,3))
    print(data)
    binary_search(data,400)