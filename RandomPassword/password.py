import re

def parola_kontrol(parola):
    if len(parola) < 8:
        return False

    if not re.search(r'[.\-,\?!_]', parola):
        return False

    if not re.search(r'\d', parola):
        return False

    return True

parola = input("Parolanızı girin: ")

if parola_kontrol(parola):
    print("Geçerli bir parola girdiniz.")
else:
    print("Parola geçerli değil. Lütfen en az 8 karakter içeren, özel karakter ve rakam içeren bir parola girin.")

