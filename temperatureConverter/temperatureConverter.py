santigrat_sicaklik = float(input("Santigrat sıcaklık değerini girin: "))

fahrenheit_sicaklik = (santigrat_sicaklik * 9/5) + 32

kelvin_sicaklik = santigrat_sicaklik + 273.15

print(f"{santigrat_sicaklik} Santigrat = {fahrenheit_sicaklik} Fahrenheit")
print(f"{santigrat_sicaklik} Santigrat = {kelvin_sicaklik} Kelvin")
