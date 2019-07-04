#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:46:37 2019

@author: frankhu
"""
import random

#fundamental setting of the program
List=[["0","1","2","3","4"],["-","-","-","-","-"],["o","o","o","o","o"],["o","o","o","o","o"],["o","o","o","o","o"],["o","o","o","o","o"],["o","o","o","o","o"]]
print("game starts ::")
l=random.randint(0,4)
n=random.randint(0,4)
t=0
m=0
l=True


while t in range(5):
    #Time count
    print("Your Time Left: "+str(5-t))
    r,c=input("please input the guess of the row and column: \n").split(',')
    r=int(r)
    c=int(c)
    #loop to record the input until it is in right format
    while (r not in range(5)) or (c not in range(5)):
        print("Input error !")
        r,c=input("please input the guess of the row and column:").split(',')
        r=int(r)
        c=int(c)
    #If the guess is right
    if (l==r) and (n==c):
        print("Congrats bro lalalallalalalalal ^ ^")
        List[r+2][c]="A"
        for i in List:
            print(i)
        l=False
        break
    #iteneraton increment
    elif t>=2:
        flag=True
        t+=1
    else:
        t+=1
        flag=False
    #after two wrong guess    
    if flag:
        print("You've got wrong for more than twice. Try harder ^ ^")
        dx=abs(l-r)
        dy=abs(n-c)
        #hint on distance
        print("The x distance is "+str(dx)+" from you","\n")
        print("The y distance is "+str(dy)+" from you","\n")
        List[r+2][c]="X"
        for i in List: 
            print(i) 
    else:
        dx=abs(l-r)
        dy=abs(n-c)
        print("The x distance is "+str(dx)+" from you","\n")
        print("The y distance is "+str(dy)+" from you","\n")
        List[r+2][c]="X"
        for i in List: 
            print(i) 
#lose game         
if l:
     print("Im sorry you lose  ")
     
#print(List)