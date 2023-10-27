import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gönderenin ve alıcının e-posta adreslerini ve parolalarını belirleyin
gonderen_email = "yourexamplez@gmail.com"
gonderen_parola = "yourPassword"
alici_email = "he_or_she_example@gmail.com"

# E-posta başlığı ve içeriği oluşturun
konu = "Kodlar Çalışıyor"
icerik = "Bu mail terminalden atılmıştır"

# E-posta mesajını oluşturun
mesaj = MIMEMultipart()
mesaj["From"] = gonderen_email
mesaj["To"] = alici_email
mesaj["Subject"] = konu
mesaj.attach(MIMEText(icerik, "plain"))

# SMTP sunucusuna bağlanın ve e-posta gönderin
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gonderen_email, gonderen_parola)
    server.sendmail(gonderen_email, alici_email, mesaj.as_string())
    server.quit()
    print("E-posta gönderildi!")
except Exception as e:
    print("E-posta gönderme hatası:", str(e))
