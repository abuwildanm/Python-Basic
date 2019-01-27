# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:10:10 2019

@author: MSI
"""

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             'Syahrini']

kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro',
        'Jodohku']

# enumerate akan return indeks dan datanya
for index,band in enumerate(nama_band):
    print(index,':',band)

# zip akan memasangkan dua (atau lebih) list secara linier
for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul:',lagu)

# set
playlist = {'baby baby', 'ada apa dengan cinta', 'cenat-cenut', 'jaran goyang', 'jaran goyang', 'gorgom', 'kuda', 'kucing'}

for lagu in sorted(playlist):
    print(lagu)

# dictionary

print('='*100)

playlist2 = {'Payung Teduh': 'akad',
             'Fourtwnty':'Zona Nyaman',
             'Dialog Dini Hari':'Rumahku',
             }

for i,v in playlist2.items():
    print(i,'lagunya:',v)

for i in reversed(range(1,10,1)):
    print(i)