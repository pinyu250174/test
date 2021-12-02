#! /usr/bin/env python
import rospy
import random
rospy.init_node('lesson2')

origin =[[[None for i in range(3)] for j in range(3)] for k in range(3)]
binar = [[[None for i in range(3)] for j in range(3)] for k in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            a = random.randint(0,255)
            origin[i][j][k]=a
            if a<125:
                binar[i][j][k]=0
            else:
                binar[i][j][k]=1

print(origin)
print(binar)

