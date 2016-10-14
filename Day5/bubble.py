#!/usr/bin/env python3

# import random
#
# data = []
# count = 0
# while count < 10:
#     data.append(random.randrange(1,100))
#     count += 1
# print("Old:",data)

data = [79,30,4,63,61,41,35,94,62,45]

for j in range(1,len(data)-1):
    for i in range(len(data)-1):
        if data[i+1] < data[i]:
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp
    print(data)