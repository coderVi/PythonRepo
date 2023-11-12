import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from login import Ui_Login
import sqlite3
from anasayfa import Form_Anasayfa

class Form_Giris(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Ui_Login()
        self.login.setupUi(self)
        self.anasayfa = Form_Anasayfa()
        self.login.btn_see.clicked.connect(self.parolaGoster)
        self.login.pushButton_4.clicked.connect(self.uyeOl)
        self.login.btn_login.clicked.connect(self.girisYap)
        self.login.btn_forget.clicked.connect(self.hatirlatici)
    
    def parolaGoster(self):
        if (self.login.btn_see.isChecked()):
            self.login.txt_pass_login.setEchoMode(QLineEdit.EchoMode.Normal)    
        else:
            self.login.txt_pass_login.setEchoMode(QLineEdit.EchoMode.Password)
    
    def conn(self):
        with sqlite3.connect("./data.db") as connect:
            curr = connect.cursor()
            curr.execute("""create table if not exists tbl_log(email TEXT, username TEXT, password TEXT)""")
            return connect
        
    def uyeOl(self):
        try:
            baglanti = self.conn()
            baglan = baglanti.cursor()

            if (
                self.login.txt_mail.text() != ""
                and self.login.txt_pass_sign.text() != ""
                and self.login.txt_pass_sign_2.text() != ""
                and self.login.txt_un_sign.text() != ""
            ):
                if self.login.txt_pass_sign.text() == self.login.txt_pass_sign_2.text():
                    baglan.execute(f"""INSERT INTO tbl_log(email, username, password) VALUES ("{self.login.txt_mail.text()}", "{self.login.txt_un_sign.text()}", "{self.login.txt_pass_sign.text()}")""")
                    baglanti.commit()
                    QMessageBox.information(self, "Bilgi", "Kayıt Başarılı")
                else:
                    print(f"Password 1: {self.login.txt_pass_sign.text()}")
                    print(f"Password 2: {self.login.txt_pass_sign_2.text()}")
                    QMessageBox.warning(self, "Dikkat", "Şifreler Uyuşmuyor")
            else:
                QMessageBox.warning(self, "Dikkat", "Alanların Hepsi Dolu Olmak Zorundadır.")
        except Exception as hata:
            print(f"Genel Hata: {hata}")

    def girisYap(self):
        self.kullanici = self.login.txt_un_login.text()
        self.sifre = self.login.txt_pass_login.text()
        if (self.kullanici != "") and (self.sifre != ""):
            baglan = self.conn()
            cursor = baglan.cursor()
            cursor.execute(" select * from tbl_log")
            for kayit in cursor.fetchall():
                if (kayit[1] == self.kullanici) and (kayit[2] == self.sifre):
                    self.anasayfa.kullanici.setText(f"""Welcome To "{kayit[1]}" """.upper())
                    self.close()
                    self.anasayfa.show()
                    
        else:
            QMessageBox.critical(self, "Mesaj", "Kullanıcı Bilgileri Boş Geçilemez")
    
    def hatirlatici(self):
        self.kullaniciAdi = self.login.txt_un_login.text()
        self.parola = self.login.txt_pass_sign.text()    
        if (self.kullaniciAdi != ""):
            baglan = self.conn()
            cursor = baglan.cursor()
            cursor.execute(" select * from tbl_log ")
            for kullanici in cursor.fetchall():
                if (kullanici[1] == self.kullaniciAdi):
                    QMessageBox.information(self, "Kullanıcı Parola", f"{kullanici[1]} kullanıcısının Parolası \n{kullanici[2]}")