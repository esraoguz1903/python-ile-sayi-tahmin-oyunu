import random
sayi = random.randint(1,30)
sayac = 0
tahmin = ""
hak = 5
while hak > 0:
    sayac += 1
    try:
        tahmin = int(input("Bir sayı girin: "))
        hak -= 1
        print(f"kalan hak {hak}")
    except ValueError:
        print("geçersiz değer lütfen sayı girin")
    if int(tahmin) < sayi:
        print("Daha yukarı")
    elif int(tahmin) > sayi:
        print("Daha aşağı")
    elif int(tahmin) == sayi:
        print("tebrikler sayıyı buldunuz")
        break

    if hak == 0:
        print(f"KAYBETTİNİZ!!Hakkınız bitmiştir.Tutulan sayı {sayi}")






























