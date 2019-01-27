# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 03:45:12 2019

@author: MSI
"""

namaKucing = 'cassandra'
makananKucing = 'royal canin'

def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru # variable global
    nama = namaBaru # variable local
    print('saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('ketie')

kasihMakanKucing('universal','alex')

print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)