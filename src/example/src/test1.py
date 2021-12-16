#! /usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
rospy.init_node("test1")

def forward(left,right,now,start):
    forward = {'left':left,'right':right,'now':now}
    if start:
        if forward['left']>forward['now']:
            angle = '輸出右轉'
        elif forward['right']<forward['now']:
            angle = '輸出左轉'
        else:
            angle = '輸出直走'
    return angle

turn_left = 20
turn_right = 80
start = False
start = int(input('是否開始:'))
turn_now = int(input('請輸入目前imu值:'))


print(forward(turn_left,turn_right,turn_now,start))
