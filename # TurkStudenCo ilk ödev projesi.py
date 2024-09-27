# TurkStudenCo ilk ödev projesi 

# Soru 1=Kulanıcıdan iki sayı alarak bu sayıları toplayan 
# bir programın pseudo kodunu yazın

sayi1=int(input("ilk sayiyi giriniz : \n"))
sayi2=int(input("ikinci sayiyi giriniz : \n"))

print("ilk sayiniz %d ikinci sayiniz %d "%(sayi1,sayi2))

toplam=sayi1+sayi2
print("aldigimiz iki sayinin toplami = %d"%(toplam))

# soru 2 : 1'den 100'e kadar olan sayıları
#  toplayan bir programın pseudo kodunu yazın

toplam=0

for i in range(1,101):
    toplam+=i

print("1 den 100e kadar olan sayilarin toplami = %d"%(toplam))

# soru 3: Kulanıcıdan alınan bir sayının asal olup olmadığını bulan bir programın pseudo kodunu yazın.

asal_sayi=int(input(" bir sayi giriniz"))

if(asal_sayi<=1):
    print("asal sayi degildir")
elif ( asal_sayi==2 or asal_sayi==3):
    print("asal sayidir")
elif (asal_sayi%2==0 or asal_sayi%3==0):
    print("asal sayı degildir")
else:
    print("asal sayidir")














# 2. ödevin kodları 

#  Sorular
#  1. Seviye: Basit
#  Soru:  Bir sayının tek mi çift mi olduğunu bulan programın akış diyagramını çizin
#  2. Seviye: Orta
#  Soru: Bir sayının asal olup olmadığını belirleyen bir programın akış diyagramını çizin.
#  Açıklama: Kulanıcı bir sayı girer ve program bu sayının asal olup olmadığını kontrol eder. Asal sayılar, yalnızca 1 ve kendisine bölünebilen
#  sayılardır. Algoritma, girilen sayının 2'den büyük olup olmadığını ve 2'den sayının kareköküne kadar olan sayılarla bölünüp bölünmediğini
#  kontrol etmelidir. Eğer bölünemiyorsa, sayı asaldır.
#  3. Seviye: İleri
#  Soru: Bir öğrencinin sınav notlarına göre harf notu belirleyen bir programın akış diyagramını çizin.
#  Açıklama: Kulanıcı bir öğrencinin 0 ile 100 arasında bir sınav notu girer ve program bu notun karşılık geldiği harf notunu belirler. Harf
#  notu belirleme kriterleri aşağıdaki gibidir:
#  90-100: A
#  80-89: B
#  70-79: C
#  60-69: D
#  0-59: F
#  Not :  Soru çözümleri pdf olarak istenmektedir

 #soru 1 : 

num1=int(input(" bir sayi giriniz : \n"))

if (num1 %2==0):
     print(" sayi cift")
else:
     print(" sayi tek ")



 #soru 2 :

sayi=int(input(" sayi gir \n"))
if sayi==1:
     print("asal degil")



for i in range(2,sayi):
     if sayi % i ==0:
         print("degil")
         break
     else:
         print("asal")
         break



 #soru 3 

harf_notu=int(input("harf notunuzu giriniz \n "))
if   harf_notu<=100 and harf_notu>=90:
     print("harf notunuz A")
     
     
elif harf_notu<=89 and harf_notu>=80:
     print("harf notunuz B")
elif harf_notu<=79 and harf_notu>=70:
     print("harf notunuz C")
elif harf_notu<=69 and harf_notu>=60:
     print("harf notununuz D")
elif harf_notu<=59 :
     print("harf notunuz F")
else:
     print("gecerli bir not gir ")
