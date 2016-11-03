#!/usr/bin/env python3
__author__ = 'dmmjy9'

import queue

q = queue.Queue(maxsize=3)
q.put([1,2,3])
print(q.get_nowait())
print(type(q.get_nowait()))