#!/bin/env python3
"""
Example script for dynamic loading during runtime
"""
from pprint import pprint
import examplepackage

print("!!!")
print("^C for exit")
print("!!!")
print()
print("Initial import status:")
print("======================")
pprint(examplepackage.REGISTRY)
print()
while True:
    print("You can dinamically import some of these:")
    print("=========================================")
    print(examplepackage.REGISTRY.keys())
    print()
    toimport = input("Type one name to dynamically import: ")
    print()
    if not examplepackage.REGISTRY.get(toimport):
        print("Check your spelling and try again!")
        print()
        continue
    exec(f'examplepackage.{toimport}')
    print("Current import status:")
    print("======================")
    pprint(examplepackage.REGISTRY)
    print()
