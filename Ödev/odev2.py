
ogrenciler = ["ali", "veli", "deli", "selami"]
print(ogrenciler)
# 1. soru
ogrenciEkle = input("Eklemek istediginiz ismi giriniz:")
ogrenciler.append(ogrenciEkle)
print(ogrenciler)
# 2. soru

ogrenciKaldir = input("Cikarmak istediginiz ismi giriniz:")
ogrenciler.remove(ogrenciKaldir)
print(ogrenciler)

# 3. soru


def cokluEkle():
    sayi = int(input("Kac tane ogrenci eklemek istersiniz?"))
    i = 0
    while i < sayi:
        ogrenciIsim = input("Eklemek istediginiz ismi giriniz:")
        ogrenciler.append(ogrenciIsim)
        i += 1


cokluEkle()
print(ogrenciler)


# 4. Soru

for ogrenci in ogrenciler:
    print(ogrenci)

# i = 0
# while i < len(ogrenciler):
#     print(ogrenciler[i])
#     i += 1

# 5. Soru

for ogrenci in ogrenciler:
    print(f"{ogrenci} adli ogrencinin numarasi {ogrenciler.index(ogrenci)}")

# 6.soru


def cokluCikar():
    sayi = int(input("Kac tane ogrenci cikarmak istersiniz?"))
    i = 0
    while i < sayi:
        ogrenciIsim = input("Cikarmak istediginiz ismi giriniz:")
        ogrenciler.remove(ogrenciIsim)
        i += 1


cokluCikar()
print(ogrenciler)
