#!/usr/bin/python3
print(*(__import__('this').d.get(k) for k in __import__('this').d), sep='\n')
