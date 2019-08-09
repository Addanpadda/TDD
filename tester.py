#!/bin/python3.7
import os

if os.popen('./a.out').read() == 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\n':
    print('Works')
else:
    print("Doesn't work")
