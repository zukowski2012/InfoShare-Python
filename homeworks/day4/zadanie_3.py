# 3P. program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie

od = int(input("Podaj zakres od: "))
do = int(input("Podaj zakres do (włącznie): "))

parzyste = 0
nieparzyste = 0

liczby  = range(od,do + 1)

for wynik in liczby:
    if wynik % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f"Parzystych: {parzyste}, Nieparzystych: {nieparzyste}")