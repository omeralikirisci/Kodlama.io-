print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
# string = metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)
# int, integer => tam sayı
vade = 36
ekVade = 6
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => True veya False
yukselisteMi = False

# matematiksel operatorler

# +
print(5+5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5-5)
print(vade-12)
print(vade - ekVade)
print(36-6)

# /
print(5/5)
print(vade / 2)
print(vade / ekVade)
print(10/2)

# *
print(5*5)
print(vade * 2)
print(vade / ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


# mantiksal operatorler
print(1 == 1)
print(1 == 2)

# CTRL K + CTRL C
print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and


print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)


# karar yapilari
# if else
sayi1 = 10
sayi2 = 15
# sayi1 sayi2 den buyukse ekrana sayi1 daha buyuk yazdir
# condition

# indent
if sayi1 > sayi2:
    print("Sayi 1 Sayi 2'den buyuktur")
elif sayi1 == sayi2:
    print("Iki sayi esittir")
# eger if ve else if bloklarinda hic birine ise
else:
    print("sayi 1 Sayi 2'den buyuktur")

print("Burasi if blogunun disidir.")
