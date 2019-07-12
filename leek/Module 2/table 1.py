# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:54:45 2019

@author: tilee
"""

#Create table
conn.execute('''CREATE TABLE COMPANY(ID INT PRIMARY KEY     NOT NULL,
                                     NAME           TEXT    NOT NULL,
                                     AGE            INT     NOT NULL,
                                     ADDRESS        CHAR(50),
                                     SALARY         REAL);''')
                                     print "Table created successfully";
                                     conn.close()