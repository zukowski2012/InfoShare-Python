#### 1.PODSTAWOWE ####
# Napisz program, który będzie bazą kontaktów, program ma pytać użytkownika, co chce zrobić, dając mu minimum te opcje:
# dodanie imienia, usunięcie imienia, sprawdzenie czy imię jest w bazie,
# sprawdzenie ilości imion w bazie oraz zakończenie programu.

koniec = False
while not koniec:

    print("Wybierz co chcesz zrobić: \n"
          "Wybierz '1' aby sprawdzić ilości imion w kontaktach\n"
          "Wybierz '2' aby dodać nowy kontakt\n"
          "Wybierz '3' aby usunąć wybrany kontakt\n"
          "Wybierz '4' aby sprawdzić czy kontakt jest już w bazie\n")

    co_zrobic = int(input("Opcja: "))

    with open('baza2.txt', 'r+') as baza:
        baza = baza.readlines()

    if co_zrobic == 1:
        # sprawdzanie ilości imion
        liczba_kontaktow = len(baza)
        print(f"W Twojej książce znajduje się {liczba_kontaktow} kontaktów")
    elif co_zrobic == 2:
        # dodawanie elementu do listy
        imie = input("Proszę podać imię: ")
        baza.append(imie + '\n')
        print(f"Kontakt {imie.capitalize()} został dodany!")
    elif co_zrobic == 3:
        # usuwanie elementu z listy
        usuwane_imie = input("Proszę podać imię do usunięcia z bazy: ")
        element_usuwany = str(usuwane_imie+ '\n')
        print(baza)
        if element_usuwany in baza:
            baza.remove(element_usuwany)
            print(f"Kontakt {usuwane_imie} został skreślony z listy")
        else:
            print("Nie ma takiego elementu")
    elif co_zrobic == 4:
        # sprawdzanie czy element jest w bazie
        element_sprawdzany = str(input("Podaję imię, które chcesz sprawdzić w bazie: "))
        element_sprawdzany2 = element_sprawdzany + '\n'
        if element_sprawdzany2 in baza:
            print(f'{element_sprawdzany} jest na liście kontaktów')
        else:
            print(f'{element_sprawdzany} nie jest na liście kontaktów')
    else:
        break

    print("Chcesz wykonać kolejne operacje? Wpisz t lub n")

    kolejne = input()
    if kolejne == "n":
        koniec = True
    elif kolejne != "t":
        print("Niepoprawny wybór")
        break