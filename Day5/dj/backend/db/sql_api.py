#!/usr/bin/env python3
import os
import sys
bash_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(bash_path)
from configs import settings

def db_auth(configs):
    if configs.DATABASE["user"] == "root" and configs.DATABASE["password"] == "123":
        print("db_authentication passed")
        return True
    else:
        print("db login error")

def select(table,column):
    if db_auth(settings):
        if table == 'user':
            user_info = {
                "001":['alex',22,'engineer'],
                "002":['longGe',43,'chef'],
                "003":['xiaoyun',23,'baoan']
            }
            return user_info