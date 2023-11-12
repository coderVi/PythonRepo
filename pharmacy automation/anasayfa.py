import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from MainPage import Ui_MainPage
import sqlite3

class Form_Anasayfa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainPage = Ui_MainPage()
        self.mainPage.setupUi(self)
        self.kullanici = self.mainPage.label
        self.mainPage.tableWidget.setEnabled(False)
        self.mainPage.pushButton_2.setEnabled(False)
        self.mainPage.mn_listele.triggered.connect(self.kayitListele)
        self.mainPage.mn_sil.triggered.connect(self.gizle0)
        self.mainPage.pushButton.clicked.connect(self.kayit)
        self.mainPage.pushButton_2.clicked.connect(self.kayitSil)
        self.mainPage.mn_cikis.triggered.connect(self.cikis)
    def gizle(self):
        self.mainPage.tableWidget.setEnabled(True)
    def gizle0(self):
        self.mainPage.pushButton_2.setEnabled(True)
        
    def baglanti(self):
        try:
            with sqlite3.connect("./data.db") as baglan:
                imlec = baglan.cursor()
                imlec.execute("CREATE TABLE IF NOT EXISTS tbl_kayit(hastaAdi TEXT, hastane TEXT, eczAdi TEXT, ilacAdi TEXT, amac TEXT, fiyat TEXT)")
                return baglan
        except Exception as hata:
            print(f"Bağlantı Hatası: {hata}")
            QMessageBox.critical(self, "Hata Mesajı", "Bağlantı Hatası")
            return None

    
    def kayit(self):
        try:
            conn = self.baglanti()
            curr = conn.cursor()
            
            sorgu = "INSERT INTO tbl_kayit(hastaAdi, hastane, eczAdi, ilacAdi, amac, fiyat) VALUES (?, ?, ?, ?, ?, ?)"
            degerler = (
                self.mainPage.txt_hasta.text(),
                self.mainPage.txt_hastane.text(),
                self.mainPage.comboBox.currentText(),
                self.mainPage.txt_ilac.text(),
                self.mainPage.txt_amac.text(),
                self.mainPage.txt_fiyat.text()
            )

            curr.execute(sorgu, degerler)
            conn.commit()
            QMessageBox.information(self, "Bilgi", "Kayıt Başarılı")
            self.kayitListele()
        except Exception as hata:
            print(f"Kayıt Hatası: {hata}")

    def kayitListele(self):
        tablo = self.mainPage.tableWidget
        tablo.setEnabled(True)
        tablo.clear()
        self.topla()
        try:
            kolonlar = ["Hasta Adı", "Hastane", "Eczacı Adı","İlaç Adı", "İlaç Amacı", "İlaç Fiyatı"]
            tablo.setHorizontalHeaderLabels(kolonlar)
            baglan = self.baglanti()
            secim = baglan.cursor()
            secim.execute(" select * from tbl_kayit")
            kayitlar = secim.fetchall()
            if kayitlar:
                tablo.setRowCount(len(kayitlar))
                kayitSayi = 0
                for kayit in kayitlar:
                    for i in range(len(kolonlar)):
                        tablo.setItem(kayitSayi, i, QTableWidgetItem(str(kayit[i])))
                    kayitSayi += 1
            else:
                QMessageBox.warning(self, "Boş Liste", "Reçete Listesi Boştur")
                             
        except Exception as hata:
            QMessageBox.critical(self, "Hata Mesajı", "Hata \n" + hata)
        
    def kayitSil(self):
        try:
            conn = self.baglanti()
            curr = conn.cursor()
            curr.execute(f"DELETE FROM tbl_kayit WHERE hastaAdi = ?", (self.mainPage.txt_hasta.text(),))
            conn.commit()
            self.kayitListele()

            QMessageBox.information(self, "Bilgi", "Kayıt Silindi")
            
        except Exception as hata:
            print(f"Hata: {hata}")
    
    def cikis(self):
        from giris import Form_Giris
        self.girispenceresi = Form_Giris()
        self.girispenceresi.show()
        self.close()
        
    def topla(self):
        conn = self.baglanti()
        curr = conn.cursor()
        curr.execute("SELECT fiyat FROM tbl_kayit")
        cikti = curr.fetchall()
        toplam_fiyat = 0
        for row in cikti:
            fiyat = float(row[0])  
            toplam_fiyat += fiyat
        self.mainPage.txt_toplam.setText(f"Toplam Fiyat: {toplam_fiyat:.2f} TL")

        conn.close()


