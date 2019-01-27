# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:09:27 2019

@author: MSI
"""

#list sebagai iterable
gorengan = ["bakwan", "cireng", "tahu isi", "tempe goreng", "ubi goreng"]

for g in gorengan:
    print(g)
    print(len(g))

#string sebagai iterable
bakwan = "bakwan"

for i in bakwan:
    print(i)

#for di dalam for
gorengan = ["bakwan", "cireng", "tahu isi", "tempe goreng", "ubi goreng"]
buah = ["semangka", "jeruk", "apel", "anggur"]
sayur = ["kangkung", "wortel", "tomat", "kentang"]

daftarBelanja = [gorengan, buah, sayur]

for subDaftarBelanja in daftarBelanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

print("\n" + 10*"=" + " For-else " + 10*"=")

number = 50

#range(start, stop, step)
for i in range(0, 100, 10):
    
    if i is number:
        print("angka ditemukan", i)
#        break #untuk mengakhiri for / terminasi
        continue #untuk menskip step looping
#        pass #dummy argument, bisa digunakan dalam if, for, function
        print("cek cek")
    print("angka saat ini adalah", i)
else:
    print("angka tidak ditemukan")

#else akan dieksekusi ketika for mencapai batas akhir
#dalam hal ini else tidak dieksekusi karena for tidak mencapai batas akhir, kena break duluan

print("space di luar for")