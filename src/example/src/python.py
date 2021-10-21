#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
from time import sleep
n=0
while n<10:
    print(n)
    n+=1
    sleep(1)
print("時間到")
