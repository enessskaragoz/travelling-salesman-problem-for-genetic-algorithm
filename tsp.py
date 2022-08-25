# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:57:25 2022

@author: Enes
"""
import numpy as np
import random
from datetime import datetime 

#parametreler
sehir_sayisi = 10
populasyon_sayisi = 100
mutasyon_orani = 0.3



#şehirleri temsil eden koordinat listesi oluşturma
koordinat_listesi = [[x,y] for x,y in zip(np.random.randint(0,100,sehir_sayisi),np.random.randint(0,100,sehir_sayisi))]
sehirler = np.array(["Edirne","Istanbul","Bursa","Izmir","Denizli","Afyon","Ankara","Konya,","Antalya","Kayseri"])
sehirler_sozluk = {x:y for x,y in zip(sehirler,koordinat_listesi)}  #sözlük olarak sehir isimlerini ve koordinatlarını listeledik.


    
#2 nokta arası mesafe hesaplama işlemi
def sehirler_arasi_uzaklik_koordinatlari(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

def sehirler_arasi_uzaklik_isimleri(sehir_a, sehir_b, sehirler_sozluk):
    return sehirler_arasi_uzaklik_koordinatlari(sehirler_sozluk[sehir_a], sehirler_sozluk[sehir_b])
print("Şehirler sözlük şeklinde yazdırıldı")
print(sehirler_sozluk)
print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")



#ilk populasyon kumemizi olusturduk
def genetic(sehir_listesi, populasyon_sayisi):
    populasyon_kumesi = []
    for i in range(populasyon_sayisi):
        #rastgele yeni bir çözüm üretme
        cozum_i = sehir_listesi[np.random.choice(list(range(sehir_sayisi)), sehir_sayisi, replace= False)]
        populasyon_kumesi.append(cozum_i)
    return np.array(populasyon_kumesi)

populasyon_kumesi = genetic(sehirler, populasyon_sayisi)
print("populasyon kümesi yazdırıldı.") 
print(populasyon_kumesi)   #print ile 100 tane sehirler arası gidilecek yolları sıraladık.
print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
#Çözümler, listedeki ilk öğenin ziyaret edilecek ilk şehir, ardından ikincisi vb. olacak şekilde tanımlanır ve son şehir birinciye bağlanır. 
#Uygunluk fonksiyonunun sonraki şehirler arasındaki mesafeyi hesaplaması gerekir.

def fitness_hesaplama(sehir_listesi, sehirler_sozluk):
    toplam = 0
    for i in range(sehir_sayisi - 1):
        a = sehir_listesi[i]
        b = sehir_listesi[i+1]
        toplam += sehirler_arasi_uzaklik_isimleri(a, b, sehirler_sozluk)
    return toplam    
        
      
        
def tum_fitnes(populasyon_kumesi, sehirler_sozluk):
    fitnes_listesi = np.zeros(populasyon_sayisi)         
    #çözümler için uygunluk hesaplayan döngü
    for i in range(populasyon_sayisi):
        fitnes_listesi[i] = fitness_hesaplama(populasyon_kumesi[i], sehirler_sozluk)
    return fitnes_listesi
fitnes_listesi = tum_fitnes(populasyon_kumesi, sehirler_sozluk)
print("Fitness listesi yazdırıldı")
print(fitnes_listesi)
print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")

#SELECTION
#Rulet Tekerleği Seçimini kullanarak yeni bir dizi ata seçtim. N= len(populasyon_kumesi) olan bir ata çiftleri listesi oluşturur, 
#ancak her konumda birleştirilecek iki çözüm vardır

def ata_secimi(populasyon_kumesi, fitnes_listesi):
    toplam_fit = fitnes_listesi.sum()
    olasilik_listesi = fitnes_listesi/toplam_fit
    
    ata_listesi_a = np.random.choice(list(range(len(populasyon_kumesi))), len(populasyon_kumesi), p=olasilik_listesi, replace=True)
    ata_listesi_b = np.random.choice(list(range(len(populasyon_kumesi))), len(populasyon_kumesi), p=olasilik_listesi, replace=True)
    
    ata_listesi_a = populasyon_kumesi[ata_listesi_a]
    ata_listesi_b = populasyon_kumesi[ata_listesi_b]
    
    return np.array([ata_listesi_a, ata_listesi_b])


ata_listesi = ata_secimi(populasyon_kumesi, fitnes_listesi)
ata_listesi[0][2]  
print("Ata listesi yazdırıldı.")
print(ata_listesi)  
print("╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")

#CROSSOVER
#Her ebeveyn çifti için bir yavru çifti oluşturacağız. 
#Şehirleri tekrarlayamayacağımız için yapacağımız şey, bir atadan rastgele bir parça kopyalayıp boşlukları diğer ata ile doldurmaktır.
def ciftlestir_ata(ata_a, ata_b):
    yavru = ata_a[0:5]
    
    for sehir in ata_b:
        if not sehir in yavru:
            yavru = np.concatenate((yavru, [sehir]))
    return yavru


        
def ciftlestir_populasyon(ata_listesi):
    yeni_populasyon_kumesi = []
    for i in range(ata_listesi.shape[1]):
        ata_a, ata_b = ata_listesi[0][i], ata_listesi[1][i]
        yavru = ciftlestir_ata(ata_a, ata_b)
        yeni_populasyon_kumesi.append(yavru)
        
    return yeni_populasyon_kumesi    

yeni_populasyon_kumesi = ciftlestir_populasyon(ata_listesi)
yeni_populasyon_kumesi[0]


#MUTATITON
#Şimdi yeni popülasyonun her bir öğesi için rastgele bir değiş tokuş şansı ekliyoruz.
def mutasyon_yavru(yavru):
    for i in range(int(sehir_sayisi * mutasyon_orani)):
        a = np.random.randint(0, sehir_sayisi)
        b = np.random.randint(0, sehir_sayisi)
        
        yavru[a], yavru[b] = yavru[b], yavru[a]
        
    return yavru 


def mutasyon_populasyon(yeni_populasyon_kumesi):
    mutasyonlu_populasyon = []
    for yavru in yeni_populasyon_kumesi:
        mutasyonlu_populasyon.append(mutasyon_yavru(yavru))
    return mutasyonlu_populasyon

mutasyonlu_populasyon = mutasyon_populasyon(yeni_populasyon_kumesi)
mutasyonlu_populasyon[0]


#Durdurma kriterlerini seçmek için önce duracak bir döngü oluşturdum. Sonra 1000 yinelemede döngü ayarladım.
eniyi_sonuc = [-1, np.inf, np.array([])]
for i in range(1000):
    #aşağıda, fitnes listesinin minimum değerini, fitnes listesinin ortalamasını yazdırdık.
    if i%100==0: print(i, fitnes_listesi.min(), fitnes_listesi.mean(), datetime.now().strftime("%d/%m/%y %H:%M"))
        
    fitnes_listesi = tum_fitnes(mutasyonlu_populasyon, sehirler_sozluk)
    #en iyi sonucu kaydettim.    
    if fitnes_listesi.min() < eniyi_sonuc[1]:
        eniyi_sonuc[0] = i
        eniyi_sonuc[1] = fitnes_listesi.min()
        eniyi_sonuc[2] = np.array(mutasyonlu_populasyon)[fitnes_listesi.min() == fitnes_listesi]
            
    ata_listesi = ata_secimi(populasyon_kumesi, fitnes_listesi)  
    yeni_populasyon_kumesi = ciftlestir_populasyon(ata_listesi)

print("En iyi sonuç yazdırıldı.")        
print(eniyi_sonuc)    
    