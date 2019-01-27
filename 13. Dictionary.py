# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 20:55:01 2019

@author: MSI
"""

member1 = {"ID":101,
           "Nama":"Faqihza Mukhlish",
           "Pekerjaan":"Mahasiswa",
           "Status member":"Gold"
           }

member2 = {"ID":102,
           "Nama":"Ujang Pintu",
           "Pekerjaan":"reparasi pintu",
           "Status member":"Berlian"}

memberlist = {101:member1,102:member2}

print(member1["Pekerjaan"])
print(member1.keys())
print(member1.values())
print(member1.items())
print(memberlist[101])