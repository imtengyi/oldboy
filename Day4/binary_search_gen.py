#!/usr/bin/env python3

def bin_search(data_source,find_n):
    high = data_source[-1]
    low = data_source[0]
    while low < high:
        mid = int((low+high)/2)
        if data_source[mid] < find_n:
            low = mid + 1
        elif data_source[mid] > find_n:
            high = mid - 1
        else:
            return mid
    else:
        return -1

if __name__ == '__main__':
    data = list(range(1,600))
    print(bin_search(data,400))