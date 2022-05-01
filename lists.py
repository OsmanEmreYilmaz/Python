# -*- coding: utf-8 -*-
ogrenciler = ['Emre','Derin','Carla']

ogrenciler.append('Ahmet')

ogrenciler.remove('Carla')

print(ogrenciler[2]) #baştaki 0 unutma!
print(ogrenciler)


sehirler = list(('Ankara','İstanbul','İzmir'))
print(sehirler)
print(len(sehirler))

# diğer fonksiyonlar
#print(sehirler.clear())
print('Ankara sayısı =' + str(sehirler.count('Ankara')))
print('Ankara indexi =' + str(sehirler.index('Ankara'))) #kaçıncı sırada?
sehirler.pop(1)              #çıkarma komutu 
sehirler.insert(0,'İstanbul')  # istediğimiz sıraya ekleme yaparız
sehirler.reverse()            #liste sıralamasını tam tersi yapar
print(sehirler)

sehirler3 = sehirler.copy()
sehirler2 = sehirler
sehirler2[0]= 'İstanbul'
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3) # İki listeyi birbirine ekler.
sehirler.sort()            #A'dan Z'ye sıralar
print(sehirler)
 

