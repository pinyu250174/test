#! /usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
rospy.init_node("lesson4")

def welcome(name):
    print('Hi!',name,',Good Morning')
welcome('everyone')

print('-----')

def interest(interest_type,subject):
    print('我喜歡'+interest_type+'的活動')
    print('在'+interest_type+'的活動中，我最喜歡'+subject)
interest(interest_type = '動態',subject = '籃球')

print('-----')
'''
def subtract(X1,X2):
    ''''''減法''''''
    return X1-X2
def addition(X1,X2):
    ''''''加法''''''
    return X1+X2
op = int(input('輸入1或2:'))
a = int(input('a= '))
b = int(input('b= '))
if op==1:
    print('a+b=',addition(a,b))
elif op==2:
    print('a-b=',subtract(a,b))
else:
    print('輸入錯誤')

print('-----')

def list_trans(num):
    a = list(range(len(num)))
    for i in range(len(num)):
        num[i]=num[i]+30
number = [0,20,40]
list_trans(number)
print(number)

print('-----')

def build_member(name,gender,tel):
    member = {'Name':name,'Gender':gender}
    if tel:
        member['tel']=tel
    return member
member_name = input('請輸入姓名:')
member_gender = input('請輸入性別:')
member_tel = input('請輸入電話號碼:')
print(build_member(member_name,member_gender,member_tel))

print('-----')
'''
x = 1
def increase():
    global x
    x+=1
print('before +1:',x)
increase()
print('after +1:',x)
