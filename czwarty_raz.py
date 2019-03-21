wysokosc = int(input("Podaj wysokosc "))

#2n-1

napis_poczagtek = "*" * (2 * wysokosc - 1)
spacje = ""
while len(napis_poczagtek) >= 1:

    print("{}{}".format(spacje,napis_poczagtek))

    if len(napis_poczagtek) > 2:
        napis_poczagtek = napis_poczagtek[:-2]
        
        break