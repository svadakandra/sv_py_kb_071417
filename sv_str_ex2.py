#!/usr/bin/env python
ip_addr = raw_input("Please enter IP address: ")
ip_addr = ip_addr.split(".")

print ("{:<12} {:<12} {:<12} {:<12}".format(*ip_addr))

