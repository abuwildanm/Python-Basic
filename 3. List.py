# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 21:04:04 2019

@author: MSI
"""

data = [1,4,9,16,25,36,49,64]

#mengakses elemen list
subdata1 = data[3]
subdata2 = data[-3]

#memotong (slicing) list
subdata3 = data[2:4]
subdata4 = data[:4]

data2 = [100,200,300,400,500,600,700,800]

#menambah list
data3 = data + data2

#mengubah elemen list
data[4] = 87

#mengcopy isi list ke variabel baru
a = data[:]
#a = data.copy()
a[7] = 90

#merubah elemen list dengan menggunakan slicing
data[3:5] = [11,12]

#list dalam list
x = [data, data2]

#mengakses elemen multidimensional list
y = x[1][4]

#menambah elemen list
data.append(30)

#menghitung banyaknya elemen di dalam list
length = len(data)

print(data, length)

print("\n" + 10*"=" + " Method-method dalam List " + 10*"=")

Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

# beberapa method yang bisa digunakan untuk memanipulasi list
# method untuk menambah data kedalam list
# nambah data dari belakang
Barang.append('sepeda')
print(Barang)

# nambah iterable data dari belakang
Barang.extend('dompet')
print(Barang)

Barang.insert(3,'sepeda')
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda')
print("Jumlah sepeda adalah: ",jumlahSepeda)

# meremove data
Barang.remove('sepeda')
print(Barang)

Barang.reverse()
print(Barang)

print("="*20)
Stuff = Barang.copy()
Stuff.append('gelas')
print(Stuff)
print(Barang)