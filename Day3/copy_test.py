#!/usr/bin/env python3
import copy

dict_1 = {
    'cpu':[80,],
    'mem':[80,],
    'disk':[80,]
}
print(dict_1)

# new_dict_1 = copy.copy(dict_1)
new_dict_1 = copy.deepcopy(dict_1)
new_dict_1['cpu'][0] = 50
print(dict_1)
print(new_dict_1)