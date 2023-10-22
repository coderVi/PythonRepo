import random

print("\u2764\ufe0f"*3,"Selam Dostum Sayı Tahmin Oyununa Hogeldin","\u2764\ufe0f"*3)

sayi = random.randint(1,100)

for i in range(1,4):
    deger = int(input("Lütfen bir Değer Giriniz :"))
    if(sayi > deger):
        print("Seçtiğiniz sayı Bilgisayarın tuttuğu değerden daha küçük")
    elif(sayi < deger):
        print("Seçtiğiniz sayı Bilgisayarın tuttuğu değerden daha büyük")
    elif(sayi == deger):
        print("Tebrikler cevabı buldunuz ")
        print(print("\u2764\ufe0f" * 10))
