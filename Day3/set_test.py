#!/usr/bin/env python3

#old db
old_dict = {
    "#1":{'hostname':'c1','cpu_count':2,'mem_capicity':80},
    "#2":{'hostname':'c1','cpu_count':2,'mem_capicity':80},
    "#3":{'hostname':'c1','cpu_count':2,'mem_capicity':80}
}

#cmdb new data
new_dict = {
    "#1":{'hostname':'c1','cpu_count':2,'mem_capicity':800},
    "#3":{'hostname':'c1','cpu_count':2,'mem_capicity':80},
    "#4":{'hostname':'c2','cpu_count':2,'mem_capicity':80}
}

old = set(old_dict.keys())
new = set(new_dict.keys())

#data need to be update
update_set = old.intersection(new)
#data need to be deleted
delete_set = old.symmetric_difference(update_set)
#data need to be added
add_set = new.symmetric_difference(update_set)

print(update_set)
print(delete_set)
print(add_set)