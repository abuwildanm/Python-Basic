# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:10:08 2019

@author: MSI
"""

#Tuple itu nilainya fix, tidak bisa diubah-ubah ataupun ditambah

import sys, timeit

# List
Ganjil = [1,3,5,7,9]

# Tuple
Genap = (2,4,6,6,8,10)

#cek tipe data
print("Tipe dari Ganjil:", type(Ganjil))
print("Tipe dari Genap:", type(Genap))

#cek method-method yang bisa digunakan
print("Method yang bisa digunakan oleh Ganjil (list): ", dir(Ganjil))
print("Method yang bisa digunakan oleh Genap (tuple): ", dir(Genap))

print("Isi Ganjil (list): ",Ganjil)
print("Isi Genap (tuple): ",Genap)

print("\n" + 10*"=" + " Cek Penggunaan Data Antara List & Tuple " + 10*"=")

data_list = [1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14]
data_tuple = (1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print("besar data list:", besar_datalist)
print("besar data tuple:", besar_datatuple)

print("\n" + 10*"=" + " Cek Waktu Pemrosesan Antara List & Tuple " + 10*"=")

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

print("waktu untuk memproses list:",data_list)
print("waktu untuk memproses tuple:",data_tuple)