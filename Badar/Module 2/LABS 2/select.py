# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:07:28 2019

@author: Owner
"""

#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('joins.db')
print("Opened database successfully")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3]),
    
print("Operation done successfully")
conn.close()