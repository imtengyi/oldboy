#!/usr/bin/env python3

iter_1 = iter(['a','b','c'])
print(iter_1.__next__())
print(iter_1.__next__())
print(iter_1.__next__())


def gen_1(amount):
    while amount > 0:
        amount -= 100
        yield 100
        print("get")
get_money = gen_1(500)
print(get_money.__next__())
print(get_money.__next__())
print(get_money.__next__())
# print(get_money.__next__())
# print(get_money.__next__())
# print(get_money.__next__())
# print(get_money.__next__())

'''生产者消费者模型'''
import time

def consumer(name):
    print("[%s] is ready to buy goods"%name)
    while True:
        goods = yield
        print("good [%s] came,bought by [%s]"%(goods,name))

def producer(name):
    c1 = consumer('A')
    c2 = consumer('B')
    c1.__next__()
    c2.__next__()
    print("Start making goods")
    for i in range(5):
        time.sleep(2)
        print("made 2 goods")
        c1.send(i)
        c2.send(i)

producer('mumu')