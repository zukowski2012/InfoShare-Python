# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

rok =  input("Podaj rok: ")
rok = int(rok)

if rok % 400 == 0 or rok % 100 != 0 and rok % 4 == 0:
    print("Rok jest przestępny!")
else:
    print("Rok nie jest przestępny! ")