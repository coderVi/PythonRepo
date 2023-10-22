def bankamatik_para_cek(miktar):
    banknot_200 = miktar // 200
    kalan = miktar % 200
    banknot_100 = kalan // 100
    kalan %= 100
    banknot_50 = kalan // 50
    kalan %= 50
    banknot_20 = kalan // 20
    kalan %= 20
    banknot_10 = kalan // 10
    kalan %= 10
    banknot_5 = kalan // 5
    kalan %= 5

    print(f"{banknot_200} adet 200 TL")
    print(f"{banknot_100} adet 100 TL")
    print(f"{banknot_50} adet 50 TL")
    print(f"{banknot_20} adet 20 TL")
    print(f"{banknot_10} adet 10 TL")
    print(f"{banknot_5} adet 5 TL")

    if kalan > 0:
        print(f"{kalan} adet bozuk para")

miktar = int(input("Çekmek istediğiniz miktarı girin: "))
bankamatik_para_cek(miktar)
