#coding:utf-8
# print 5
# f = lambda x : x * x
# print f(5)
import os
import time
import sys
import re

if __name__ == '__main__':
    patt = re.compile('w{3}\.([a-zA-Z]+\.)+com')
    temp = re.findall(patt,'wwbaidu.com') 
    print temp