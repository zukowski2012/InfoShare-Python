# plik fun9
# dodać do lity (bazy) imię

def dodaj_imie(imie, baza=None):
    if baza == None:
        baza = []
    imie = imie.upper()
    baza.append(imie)
    return baza

anglicy = dodaj_imie("john")
print(anglicy)

francuzi = dodaj_imie("antoin")
print(francuzi)

anglicy = dodaj_imie("faosla", anglicy) # dopisujemy jako bazę "angilcy" żeby nam nie wyczyściło
print(anglicy)

rosjanie = dodaj_imie("sasha")
print(rosjanie)