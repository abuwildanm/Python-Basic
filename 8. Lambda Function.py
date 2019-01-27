# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 03:36:08 2019

@author: MSI
"""

def jumlah(a,b):
    c = a+b
    return c

hasil = jumlah(4,5)
print(hasil)

#membuat anonymous function dengan lambda
kali = lambda x,y: x*y
hasil = kali(3,4)
print(hasil)