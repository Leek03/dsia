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
outcome=True

def guess_input():
    r,c=input("please input the guess of row and column: ").split(",")
    r=int(r)
    c=int(c)

def obtain_distance():
    dx=abs(l-r)
    dy=abs(n-c)
    #hint on distance
    print("the x distance is "+str(dx)+" from you ", "\n")
    print("the y distance is "+str(dy)+" from you ", "\n") 
    List[r+2][c]="X"
    print(l,n,r,c)
    for i in List: 
        print(i)
        
def win_display():
    List[r+2][c]="A"
    for i in List:
        print(i)
    
        
def wrong_display():
    List[r+2][c]="X"
    for i in List:
        print(i)    
    
    
while t in range(5):#could use outcome:
    #Time count
    print("Your Time Left: "+str(5-t))
    guess_input()
    #loop to record the input until it is in right format
    while (r not in range(5)) or (c not in range(5)):
        print("Input error !")
        guess_input()
    #If the guess is right
    if (l==r) and (n==c):
        print("Congrats bro lalalallalalalalal ^ ^")
        win_display()
        outcome=False
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
        obtain_distance()
        wrong_display()
    else:
        obtain_distance()
        wrong_display() 
#lose game         
if outcome:
     print("Im sorry you lose  ")
     
#print(List)