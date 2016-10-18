#!/usr/bin/env python3

import pickle


def login():
    pass
f = open("user_acc.txt", "rb")
data = pickle.loads(f.read())
data["func"]()
