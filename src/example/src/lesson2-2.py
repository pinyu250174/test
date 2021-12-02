#! /usr/bin/env python
import rospy

rospy.init_node('lesson2')

a = []
for i in range(3):
    x = int(input())
    a.append(x)
a.sort()
print(a)
