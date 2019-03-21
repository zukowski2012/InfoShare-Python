# 6P. program wypisujący tabliczkę mnozenia (1 do 10) dla podanej liczby
# uzyc formatowania stringow!

liczba = int(input("Proszę podać liczbę: "))
zakres = range(1,11)

for zmienna in zakres:
    wynik = zmienna * liczba
    print("{} * {} = {}".format(liczba, zmienna, wynik))