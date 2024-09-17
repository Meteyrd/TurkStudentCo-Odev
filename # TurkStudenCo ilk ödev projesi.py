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



   