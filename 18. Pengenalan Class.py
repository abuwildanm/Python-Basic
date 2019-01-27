# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 22:54:48 2019

@author: MSI
"""

class Mahasiswa():
	nama = 'nama'

	def belajar(self, kondisi): #self itu kaya this
		print(self.nama,'sedang belajar', kondisi)

	def tidur(self):
		print(self.nama,'tidur di kelas')

# main programnya

otong = Mahasiswa()
ucup = Mahasiswa()

otong.nama = "otong surotong"
ucup.nama = "michael ucup"

print(otong.nama)
print(ucup.nama)

otong.belajar('dengan giat')
ucup.tidur()