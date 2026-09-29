# Hurja kettukoodi joka ottaa kuvia osoitteesta randomfox.ca ja laittaa ne Kettukuvat kansioon
#testi

import requests
import os

kettukuvat_lista = []

a = 1
b = 1
c = 1

for i in range(100):
    kettukuva_url = requests.get("https://randomfox.ca/floof/").json()["image"]
    if kettukuva_url in kettukuvat_lista:
        print(f"{c} Sama kuva ({a}) ärr {kettukuva_url}")
        a+=1
    else:
        print(f"{c} Uusi kuva ({b}) hurraa")
        b+=1
        kettukuvat_lista.append(kettukuva_url)
    c+=1

d = 1
for i in kettukuvat_lista:
    kuvakuva = requests.get(i)
    if kuvakuva.status_code == 200:
        os.makedirs("Kettukuvat", exist_ok=True)
        with open(f"Kettukuvat/kettu_{d}.jpg", "wb") as f:
            f.write(kuvakuva.content)
        print(f"Kuva ladattu {d}")
        d+=1

print("Kaikki kettukuvat tallennettu kansioon Kettukuvat")