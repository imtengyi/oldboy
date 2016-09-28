#!/usr/bin/env python3
def login(func):
    def inner():
        print("Passed user verification.")
        return func()
    return inner

@login
def tv():
    print("Welcome to TV page!")

tv()