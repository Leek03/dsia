# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:05:45 2019

@author: sepid
"""

import random
import numpy as np

Mugwump_home = np.empty([5, 5],dtype= str)

Mugwump_x = random.randint(0,4)
Mugwump_y = random.randint(0,4)

for i in range(len(Mugwump_home)):
    Mugwump_home[i] ="O"


print(Mugwump_home)

def win(x,y):
    if x == Mugwump_x and y== Mugwump_y:
        return 1
    else:
        return 0
    
def out_of_range(x,y): 
    if x<0 or x>4 or y<0 or y>4:
        return 1
    else:
        return 0
    
def distance(x,y):
    dist = round(np.sqrt((Mugwump_x-x)**2+(Mugwump_y-y)**2))
    return dist

for i in range(5):
    x_in = int(input("input one integer between 0 to 4:"))
    y_in = int(input("input one integer between 0 to 4:"))
    if win(x_in,y_in):
        print("well done,you win!!!")
        break
    elif out_of_range(x_in,y_in):
        print("Ooopss!! your number is out of borders,try again")
    elif Mugwump_home[x_in][y_in] =="X":
        print("Be carefull!you input repetitive numbers")
    else:
        Mugwump_home[x_in][y_in]="X"
        print("keep trying,your distance to goal is: " , distance(x_in,y_in))
        print(Mugwump_home) 
        
        
Mugwump_home[Mugwump_x ,Mugwump_y] = "G"
print(Mugwump_home)        
print("Game Over!!you tried " + str(i+1) + " times! The Goal was:  " +   str(Mugwump_x) +"  " + str(Mugwump_y))       
        

    
        
      