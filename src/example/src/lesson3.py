#! /usr/bin/env python
import rospy
rospy.init_node("lesson3")
 
a = 't','u','p','l','e'
b = tuple(a)
print(b)

tuple5 = ('Red','Green','Blue')
(R,G,B) = tuple5
print(R)
print(G)
print(B)

tpl_index = (13,1,23,6,45,7,7,45,5,123,1)
y = tpl_index.index(5)
print(y)

dict_example = {'a':'apple','b':'banana','c':'cat'}
X = dict(a='apple',b='banana',c='cat')
print(dict_example)
print(X)

list_ex1 = [['math',100],['englis',98]]
print(dict(list_ex1))

list_ex2 = ['ab','cd','ef']
print(dict(list_ex2))

key = ('key1','key2','key3')
value = 1
keydict = dict.fromkeys(key,value)
print(keydict)

Gender = {'man':'Bob','female':'Mary'}
Gender['?'] = 'Nancy'
print(Gender)
Gender.update({'??':'banana'})
print(Gender)

print(Gender.get('??'))
print(Gender.keys())

delthisdict = {'trash':'deleted files','space':'installation file'}
print(delthisdict)
delthisdict.clear()
print(delthisdict)

s = "HELLO_WORLD"
for S in s:
    if S == "O":
        continue
    print(S)
