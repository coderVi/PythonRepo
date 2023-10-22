from random import choice

def oyunu_oyna():
    secenekler = ["taş", "kağıt", "makas"]
    bilgisayar_secimi = choice(secenekler)
    
    while True:
        kullanici_secimi = input("Taş, Kağıt veya Makas? ").lower()
        
        if kullanici_secimi in secenekler:
            break
        else:
            print("Geçerli bir seçenek girin: Taş, Kağıt veya Makas")
    
    print(f"Bilgisayar {bilgisayar_secimi} seçti.")
    print(f"Siz {kullanici_secimi} seçtiniz.")
    
    if kullanici_secimi == bilgisayar_secimi:
        print("Berabere!")
    elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt"):
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")

oyunu_oyna()
