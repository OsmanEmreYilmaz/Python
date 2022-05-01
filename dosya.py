# -*- coding: utf-8 -*-

f = open('musteriler.txt')
# print(f.read())
print('***')
print(f.readline())
for l in f:
    print(l)

f.close

fileToAppend = open('ogrenciler.txt','a')
fileToAppend.write('\n')
fileToAppend.write('kamil')
fileToAppend.close()

# w bulunan veriyi silerek yazar dikkat!!

import os
os.remove('ogrenciler.txt')
