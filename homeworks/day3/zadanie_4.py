# oblicz ocenę na podstawie progu procentowego

ocena = input("Podaj liczbę zdobytych punktów bez znaku %: ")
ocena = int(ocena)

if ocena  <= 50:
    print("Ocena niedostateczna")
elif ocena <= 70:
    print("Ocena dostateczna")
elif ocena <= 90:
    print("Ocena dobra")
elif ocena <= 100:
    print("Ocena bardzo dobra")
else:
    print("Jesteś geniuszem!")
