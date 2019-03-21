# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku

dzien = input("Proszę podać dzień miesiąca: ")
miesiac = input("Proszę podać miesiąc (w mianowniku): ")
miesiac = int(dzien)

wiosna = ["kwiecień", "maj"]
lato = ["lipiec", "sierpień"]
jesien = ["październik", "listopad"]
zima = ["styczeń", "luty"]

if miesiac in wiosna or miesiac == "marzec" and dzien >= 21:
    print("Wiosna ")
