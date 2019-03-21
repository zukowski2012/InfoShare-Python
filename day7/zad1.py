# zadanie razem na zajęciach

osoba = ['pamela', 'kowalska', 50]

osoba_str = [ str(dane) for dane in osoba ]
print(osoba_str)

# laczymy dane z listy do jednego stringa

dane_do_zapisu = ",".join(osoba_str)

print(dane_do_zapisu)

# otworzyc plik w trybie do .. dopisywania

with open("osoby.txt", "a") as plik:
    plik.write((dane_do_zapisu + "\n"))