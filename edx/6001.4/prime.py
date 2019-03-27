# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 09:32:50 2018

@author: faza
"""

def genPrimes():
    p=2
    while True:
        i=1
        x=0
        while i<=p:
            if p%i==0:
                x+=1
            i+=1
        if x is 2:
            yield p
        p+=1
    