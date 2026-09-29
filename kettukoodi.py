# Hurja kettukoodi joka ottaa kettukuvien url osoitteet sivulta randomfox.ca ja laittaa ne tiedstoon kettukuvat.txt

import requests

kuvat = ""

a = 1
b = 1
c = 1

for i in range(10):
    oikeaKettukuva = requests.get("https://randomfox.ca/floof/").json()["image"]
    if oikeaKettukuva in kuvat:
        print(f"{c} Sama kuva ({a}) ärr {oikeaKettukuva}")
        a+=1
    else:
        print(f"{c} Uusi kuva ({b}) hurraa")
        b+=1
        kuvat = kuvat + oikeaKettukuva + "\n"
    c+=1

print("Tulokset tallennettu tiedostoon kettukuvat.txt")

with open("kettukuvat.txt", "w") as kettutiedosto:
    kettutiedosto.write(kuvat)