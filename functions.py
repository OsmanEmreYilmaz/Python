# -*- coding: utf-8 -*-

# sehir = 'Ankara'

# print(sehir.endswith('a')) #Hangi harfle bittiği (true-false)

def selamVer(isim = 'ziyaretçi'):
    print('Merhaba '+isim)
    
selamVer('Kamil')
selamVer('Salih')
selamVer('Veli')
selamVer('Rıza')
selamVer()

def selamVer2(isim = 'ziyaretçi', soyIsim = 'arkadaş'):
    print('Merhaba '+ isim +' '+soyIsim)
selamVer2('Engin')


def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)
print(alan)

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlaniHesapla2(5, 7))