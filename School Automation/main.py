import random , sqlite3 , os , time

class Ogr:
    
    def __init__(self , isim):
        while True:  
            print(f"""Selam Dostum {isim} Otomasyonuna hoşgeldin
                Yapmak İstediğin İşlemi Seç Lütfen
                1. Ekle
                2. Listele
                3. Güncelle
                4. Sil
                5. Çıkış
                """)
            sec = int(input("Seçiminiz : "))
            if sec == 1:
                self.bilgiGiris()
            
            elif sec == 2 :
                liste0 = self.listele()
                print(liste0)
                
            elif sec == 3 :
                print("Bu seçenek silip listelemenize yardımcı olur yani günceller")
                self.ogrSil()
                liste0 = self.listele()
                print(liste0)
                
            
            elif sec == 4:
                self.ogrSil()
                
            elif sec == 5:
                print("Program Kapatılıyor")
                time.sleep(3)
                exit()
                
            else:
                print("Hatalı Seçim")
        
    
        
    
    def bilgiGiris(self):
        self.ogrNo = int(input("Öğrenci No : "))
        self.ad = input("Adınız : ")
        self.soyad = input("Soyadınız : ")
        self.eposta = f"""{self.ad.replace(" ", "")}{self.soyad.replace(" ", "")}@ibb.com.tr""".lower()
        #replace i 2 isim oluştururken arada boşluk kalması sebebi ile ekledim. strip fonsiyonu işe yaramadı değiştirme methodunu kullandım
        self.dersler = self.dersSecim()
        self.adresGiris()
        self.ekle() 

        
    def adresGiris(self):
        self.sehir = input("Şehir Giriniz : ")
        self.tel = input("Telefon No : ")
        
    def ogrSil(self):
        sil1 = int(input("Silmek istediğiniz öğrenci No sunu giriniz : "))
        self.ogrNo = sil1  
        # Aşağıda ki bağlantı kodu eklemeyi ieriyordu onu bölmek istemedim tekrar 3 fonsiyon olmaması için. Ayrıca atama yapılmadan -
        # Kullanıcının girdiği öğrenci numarasını görmüyor buna dikkat edin :))
        with sqlite3.connect("ogrenciislemleri.db") as sil:
                curs = sil.cursor()
                curs.execute(f"DELETE FROM tbl_ogrenci WHERE ogrNo = '{self.ogrNo}'")
                sil.commit()
        print(f"{sil1} nolu öğrenci silindi.")
        return sil


    def dersSecim(self):
        ogrSecilenDersler = list()
        dersListe = ["Bilgisayar 101", "Programlama" , "Donanım" , "Veri Analizi" , "Web Tasarım", "C++"]
        while (len(ogrSecilenDersler) < 3):
            ders = random.choice(dersListe)
            if (ders not in ogrSecilenDersler):
                ogrSecilenDersler.append(ders)
        return ogrSecilenDersler   
    
    def baglanti(self):
        with sqlite3.connect("./ogrenciislemleri.db") as baglan:
            curr = baglan.cursor()
            curr.execute("""create table if not exists tbl_ogrenci(
                ogrNo TEXT, adi TEXT, soyad TEXT, eposta TEXT, sehir TEXT, tel TEXT, 
                dersler TEXT) """)
        return baglan
    
    def ekle(self):
        try:
            conn = self.baglanti()
            ekleSorgu = conn.cursor()
            ekleSorgu.execute(f"""INSERT INTO tbl_ogrenci VALUES(
                "{self.ogrNo}" , 
                "{self.ad}" , 
                "{self.soyad}" , 
                "{self.eposta}" , 
                "{self.sehir}" , 
                "{self.tel}" , 
                "{" - ".join(self.dersler)}")""")
            conn.commit()
            print("Kayıt Başarılı")
        except Exception as hata:
            print("hatalı giriş", hata)
    
    def listele(self):
        with sqlite3.connect("./ogrenciislemleri.db") as liste:
            currs = liste.cursor()
            currs.execute("SELECT * FROM tbl_ogrenci")
            sonuclar = currs.fetchall()  # fetchall db içinde ki tüm sorguları for döngüsü varmış gibi döndürür.
        return sonuclar


os.system("cls")  

isim = input("Otomasyon Adı : ")
        
Ogr(isim)
