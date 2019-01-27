# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:33:41 2019

@author: MSI
"""

#Set itu datanya tidak berurutan, makanya tidak punya indeks
#Set akan menganggap data yang sama sebagai satu data

superhero = set()

superhero.add("wiro sableng")
superhero.add("gundala")
superhero.add("saras 008")
superhero.add(212)

print(superhero)
#print(sorted(superhero))

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))
print(ganjil.intersection(prima))