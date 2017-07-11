#!/usr/bin/env python
from __future__ import print_function

a = ("siva")
b = ("network")
c = ("security")
#d = raw_input("enter a name:")


try:
    # PY2
    d = raw_input("Enter fourth name: ")
except NameError:
    # PY3
    d= input("Enter fourth name: ")

print()
print("{:>30}".format(a))
print("{:>30}".format(b))
print("{:>30}".format(c))
print("{:>30}".format(d))
print()
