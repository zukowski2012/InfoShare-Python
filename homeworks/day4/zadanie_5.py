# 5P. program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21

zakres = range(0, 100)

ciag_fibo = [0, 1]

for liczba in zakres:
    if ciag_fibo[-1] < 80:
        ciag_fibo.append(ciag_fibo[-1] + ciag_fibo[-2])

print(ciag_fibo)
