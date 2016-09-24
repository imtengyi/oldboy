#!/usr/bin/env python3

all_list = [11,22,33,44,55,66,77,88,99,100]

l1 = []
l2 = []
dic = {}

# for i in all_list:
#     if i>66:
#         l1.append(i)
#     else:
#         l2.append(i)
# dic['k1'] = l1
# dic['k2'] = l2

for i in all_list:
    if i>66:
        if "k1" in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i,]
    else:
        if "k2" in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i,]

print(dic)