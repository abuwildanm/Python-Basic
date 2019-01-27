# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:34:18 2019

@author: MSI
"""

text1 = 'jalan - jalan di hari minggu'
text2 = 'jalan - jalan di hari jum\'at'
text3 = "jalan - jalan di hari jum'at"
text4 = 'mahmuy berkata, "kemaren kemana bro?"'
text5 = "hobloh menjawab, \"jalan - jalan bro\""
text6 = 'mahmuy: "kemaren kemana bro?" \nhobloh: "jalan - jalan bro"'

#multi-line string
text7 = """
mahmuy: "kemaren kemana bro?"
hobloh: "jalan - jalan bro"
mahmuy: "jalan - jalan kemana bro?"
hobloh: "ke Mang Uing bro!!!"
"""

#raw string
text8 = r'C:\nyoto'

print(text8)
print("wk"*5)
print('kue' 'pukis')
print(text1 + text2 + "\n")

text = "pisang goreng"
print(text[0])
print(text[5])
print(text[0:5])
print(text[-4])
print(text[7:])
