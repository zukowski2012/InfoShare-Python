# chcemy sprawdzić, czy liczba podana do funkcji należy do zakresu 1 do 100

liczby = [10, 100, 500, 1000, 0, -1, 101, 99]

def czy_w_zakresie(liczba, zakres=range(100)):
    """sprawdza czy podana liczba jest w danym zakresie

    :param liczba: liczba do sprawdzenia
    :param zakres: range
    :return: True or False
    """
    if liczba in zakres:
        print(f"{liczba} należy do zakresu")
        return True
    else:
        print(f"{liczba} nienależy do zakresu")
        return False

for element in liczby:
    czy_w_zakresie(element)