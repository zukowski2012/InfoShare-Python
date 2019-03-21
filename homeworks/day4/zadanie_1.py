# 1P. program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1

reszta = float(input("Ile mam wydać reszty: "))
dostepne_monety = [5, 2, 1, 0.5, 0.2, 0.1]
reszta_w_monetach = []

# dopoki kwota jest wieksza niz 10 gr, to mozemy dalej wydawac reszte
while (reszta >= 0.1):
    for  moneta in dostepne_monety:
        if moneta <= reszta:
            #najpierw wydajemy monete
            reszta_w_monetach.append(moneta)
            #a teraz liczymy ile pozostało pieniędzy do wydania
            reszta = reszta - moneta
            break

czy_reszta = input("Mogę być winna grosika? t/n")

if czy_reszta.lower() == "nie":
    reszta_w_monetach.append(0.1)
print("Twoja reszta to: ")
for moneta in reszta_w_monetach:
    print("{}zł, ".format(moneta), end="")