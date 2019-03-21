# 4P. program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

zakres = range(0,20)

for liczba in zakres:
    if liczba % 4 != 0:
        print(liczba)
    else:
        continue