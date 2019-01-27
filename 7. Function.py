# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 02:06:09 2019

@author: MSI
"""

print("\n" + 10*"=" + " Function " + 10*"=")

#hargaAyam() #==> tidak bisa, karena python itu interpreted lang, jadi dia cek dulu dari atas ke bawah

#membuat fungsi sederhana
def suaraAyam():
    print("kukuruyuk!!!")

def hargaAyam():
    suaraAyam()
    print("harga ayam per 1 kg adalah Rp. 20.000")

#membuat fungsi dengan input argumen
def hargaTotalAyam(kg):
    suaraAyam()
    harga = 20000
    hargaTotal = kg * harga
    print("harga", kg, "kg ayam adalah", hargaTotal)
   
hargaAyam()
hargaTotalAyam(2)
hargaTotalAyam(0.5)
hargaTotalAyam(1)
hargaTotalAyam(9)

print("\n" + 10*"=" + " Function & Arguments " + 10*"=")

#fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print("Siswa ini bernama:", nama)

siswa("mario")

#fungsi dengan menggunakan keyword argument
def guru(nama, pelajaran):
    print("Guru ini bernama:", nama)
    print("Mengajar:", pelajaran)

guru(nama="popong", pelajaran="seni rupa")
guru(pelajaran="olah raga", nama="endang")
guru("ipa", "raihan") #ini contoh yang salah

#fungsi dengan menggunakan default argument
def penjagaSekolah(nama, shift="siang", galak="tidak"):
    print("Penjaga sekolah ini bernama:", nama)
    print("Shiftnya:", shift)
    print("Galak?:", galak)

penjagaSekolah("Entis")
penjagaSekolah("Maman", shift="malam")
penjagaSekolah("Asep", galak="sangat")
#penjagaSekolah(shift="malam", galak="iya") #menghasilkan error, karena nama tidak ada defaultnya

print("\n" + 10*"=" + " Return Value " + 10*"=")

#fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print("Nilai kuadrat dari", argumen, "adalah", total)
    return total

a = kuadrat(4)
print(a)

#fungsi dengan return value dan multiple argumen
def tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1, "+", argumen2, "=", total)
    return total

def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1, "*", argumen2, "=", total)
    return total

b = kali(3, tambah(3,4))
print(b)