# czy liczba jest podzielna przez 3, 5, 7
# musi wypisać program przez które z nich jest podzielna wpisana liczba

dane =  input("Podaj liczbę: ")
if dane.isdigit() and int(dane) != 0:
    liczba = int(dane)
    if liczba % 3 == 0:
        print("Liczba jest podzielna przez 3")
    if liczba % 5 == 0:
        print("Liczba jest podzielna przez 3")
    if liczba % 7 == 0:
        print("Liczba jest podzielna przez 3")



# do black jacka: if card0 in "23456789":
# dodał zadanie 11 dodatkowe