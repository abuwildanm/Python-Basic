# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 03:39:40 2019

@author: MSI
"""

class mahasiswa():

    jurusan = "ekonomi" # class variable, ini semacam kaya static variable
    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # instance variable (pokoknya yang ada self-nya)
        self.nim = input_nim  # instance variable
        mahasiswa.jumlah_mahasiswa += 1

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)
cassandra = mahasiswa("cassandra aja", 13317002)

mahasiswa.jurusan = "ekonomi mikro"
otong.jurusan = "peternakan" #ini sebenernya kaya override class variable jurusan menjadi instance variable
ucup.kegemaran = "renang" #dibuat kaya gini juga bisa

print(mahasiswa.jurusan)
print(otong.jurusan)
print(ucup.jurusan)
print(ucup.kegemaran)

print(mahasiswa.__dict__)
print(otong.__dict__)
print(ucup.__dict__)

print(mahasiswa.jumlah_mahasiswa)