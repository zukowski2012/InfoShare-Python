# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

liczba = input("Podaj liczbę z gry w ruletkę: ")
liczba = int(liczba)

liczby_czerwone = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
liczby_czarne = {2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35}

if liczba != 0:
    if liczba in liczby_czerwone:
        print("liczba czerwona")
    elif liczba in liczby_czarne:
        print("liczba czarna")
    else:
        print("To nie jest liczba z gry w ruletkę!")
else:
    print("Podałeś 0")

if liczba != 0:
    if liczba % 2 == 0:
        print("liczba parzysta")
    else:
        print("liczba niepatrzysta")



if liczba != 0:
    if liczba >= 18:
        print("liczba duża")
    else:
        print("liczba mała")