#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:28:12 2018

@author: isaaclera
"""
import sys

#FROM https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

if len(sys.argv)>0:
    print("Storing result on folder: %s"%sys.argv[2])
    f = open(sys.argv[2],"w")
    print("Running F(%s)"%sys.argv[1])
    value = F(int(sys.argv[1]))
    f.write(str(value))
    f.close()
    print("\tDone")
else:
    print ("Nothing to do")
    f = open(sys.argv[2], "w")
    f.close()