# oblicz ilosć liczb parzystych i nieparzystych w podanym zakresie

zakres = range(1, 101)
parzyste = 0
nieparzyste = 0

for liczba in zakres:
    if liczba % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print("Parzyste: {} nieparzyste: {}".format(parzyste,nieparzyste))

