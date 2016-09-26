#!/usr/bin/env python3

import collections
import queue

'''Counter_test'''
str_1 = 'abcdabcaba'
counter_1 = collections.Counter(str_1)
print(counter_1.most_common(4))

for i in counter_1.elements():
    print(i)

for k,v in counter_1.items():
    print(k,v)

counter_1.update('aef')
print(counter_1)
counter_1.subtract('ac')
print(counter_1)


'''OrderedDict_test'''
dict_1 = {'k1':'v1','k2':'v2','k3':'v3'}
list_1 = ['k1','k2','k3']
for i in list_1:
    print(dict_1[i])

dict_2 = collections.OrderedDict()
dict_2['k1'] = 'v1'
dict_2['k2'] = 'v2'
dict_2['k3'] = 'v3'
print(dict_2)
dict_2.move_to_end('k2')
print(dict_2)
dict_2.popitem()
print(dict_2)


'''defaultdict_test'''
dict_2 = collections.defaultdict(list)
all_list = [11,22,33,44,55,66,77,88,99]
for i in all_list:
    if i>60:
        dict_2['k1'].append(i)
    else:
        dict_2['k2'].append(i)
print(dict_2)

'''namedtuple_test'''
NamedtupleClass = collections.namedtuple('NamedtupleClass',['x','y','z'])
tuple_1 = NamedtupleClass(11,22,33)
print(tuple_1.x)
print(tuple_1.y)
print(tuple_1.z)
print(tuple_1._asdict())


'''deque_test'''
deque_1 = collections.deque([11,22,33])
print(deque_1)
deque_1.append('44')
print(deque_1)


'''queue_test'''
queue_1 = queue.Queue()
queue_1.put([11,22,33])
print(queue_1.get())

'''See more functions,please go to http://blog.csdn.net/dmmjy9'''