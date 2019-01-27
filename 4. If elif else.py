# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 18:24:51 2019

@author: MSI
"""

nilai = 50

if nilai == 75: #equal
    print("nilai anda: ", nilai)
    
if nilai != 75: #not equal
    print("nilai anda: ", nilai)
    
if nilai is 60: #equal
    print("nilai anda: ", nilai)
    
if nilai is not 60: #not equal
    print("nilai anda: ", nilai)
    
print(20*"=")

nilai = 65

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")
    
print("\n" + 10*"=" + " Operator logika untuk list dan string " + 10*"=")

gorengan = ["bakwan", "cireng", "bala-bala", "gehu", "combro", "pisang goreng", "pukis", "risoles"]
beli = "sepatu"

if beli in gorengan:
    print('Mamang bilang, "ya, saya jual', beli, '"')
    
if not beli in gorengan:
    print('"saya gak jual', beli, '"')
    
karakter = "z"

if karakter in beli:
    print("ada", karakter, "di", beli)
else:
    print("tidak ada", karakter, "di", beli)










