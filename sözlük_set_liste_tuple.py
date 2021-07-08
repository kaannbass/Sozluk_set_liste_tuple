
#indekse göre eleman ekleme insert - pop eleman silme 

liste =["ali","veli","isik"]

liste.insert(0,"ayse") #['ayse', 'ali', 'veli', 'isik']

liste[0]

liste.insert(2,"mehmet")

liste

liste.insert(5,"kaan")
liste

len(liste)

liste.insert(len(liste),"beren")#listenin sonuna beren yazdı 
liste

liste.pop(0) # ayşe sildi

liste
# count eleman frekanslarını verıyor

liste.count("ali") 
liste.count("mehmet")

liste_yedek = liste.copy()

#extend iki listeyi birleştiriyor daha oncede gordum ama bu daha kısa
#değiştirerek birleştirme yapıyor kalıcı şekilde

liste.extend(["a","b",10])
liste

#index kaçıncı indexde oldugunu gosterir
liste.index("ali")
#reverse() elemanları terse çevirir
liste.reverse()
liste


#sort sıralama yapar

liste2 = [10,20,80,20,30,50]

liste2.sort()

liste2
liste2.count(20)

#listeyi komple siler
liste2.clear()
#/////////////////////////////////////////////////////////////////////////////////////////////


#Veri Yapıları tuple
#tuple liste ile aynı farkı tuple degiştirilemez!!! 
#2. bir olayı index işlemleri ve sıralı olmasıdır.
t = ("ali","veli",1,2,3,2,[1,2,3,4])

##tuple()
# tek elemanlı tuplelarda str anlayabılır sonuna bir "," koydugunda tuple oluyor

t = ("eleman",)

t = ("ali","veli",1,2,3,[1,2,3,4])

t[1]

#t[2] = 99
#t[0] + "ali"
#t[0] = t[0] + "ali"

#Sözlük yapıları Dictionary 

# Sozluk oluşturma 
sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}

len(sozluk)

sozluk["REG"]

#Eleman ekleme ve cıkarma

sozluk ["GBM"] = "Gradient Boosting Mac"

sozluk
sozluk["REG"] = " coklu Dogrusal Regresyok "

sozluk

sozluk[1] = "Yapay Sinir Agları"
sozluk

l = [1]

sozluk[l] = "yeni bir sey"

t = ("tuple",)
sozluk[t] = "yeni bir sey"

sozluk


#Setler
#özellikleri :
#sirasizdir,değerleri essizdir,değistirilebilirdir,Farklı tipleri barındırabırabilir

#Set oluşturma

s = set()
l = (1,"a","ali",123)

s = set(t)

ali = "lutfen_ata_bakma_uazaya_git"

s = set(ali)
s
l = ["ali","lutfen","uzaya","bakma","git","ali","git"] 

s = set(l)

s


len(s)

l[0]
s[0]

# Eleman ekleme & cikarma

l = ["gelecegi","yazanlar"]

s = set(l)

dir(s)

s.add("ile")
s

s.add("gelecege_git")

s


s.add("ile")
s

s.remove("ali")

s
#hata bulup kod akısını kesmesın dıye discard kullanılıyor

s.discard("ali")

#Setler - Klasik Kume Islemleri
#
# =============================================================================
# difference() ile iki kumenin farkını ya da "-" ifadesi ile aynı sonucu verir
# intersection () iki kume kesimi ya da & ifadesi 
# union () iki kumenın birlesimi
# symmetric_difference() ikisinde de olmayan 
# 
# =============================================================================


set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # 5 gelir
set1 - set2 # 5 gelir

set2.difference(set1) # 2 gelir
set2 - set1 # 2 gelir

set1.symmetric_difference(set2) # 2 ve 5 degerlerını verdı 
set2.symmetric_difference(set1) # 2 ve 5 degerlerını verdı 

#Kesişim ve Birleşimler

# intersection () iki kume kesimi ya da & ifadesi 

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2) # 1 ve 3 

set1 & set2 # 1 ve 3 

kesisim = set1 & set2
kesisim

birlesim = set1.union(set2) #1,2,3,5 birlesim

birlesim

set1.intersection_update(set2) # yeni set1 1 ve 3 olarak değiştirdi
set1

#Setlerde sorgu islemleri 

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# iki kumenin kesisiminin bos olup 
# olmadiginin sorgulanması ?

set1.isdisjoint(set2) # iki kumenin kesisimi bos değil 

#bir kumenin butun elemanlarinin baska bir kume 
#içerisinde yer alip almadigi

set1.issubset(set2) # set1 set 2 nin alt kumesimidir diye sorguladi

#  kümeler kapsayıp-kapsamama sorgusu

set2.issuperset(set1) 


