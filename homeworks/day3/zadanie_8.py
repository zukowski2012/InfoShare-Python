# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

a = input("Podaj długość boku a: ")
b = input("Podaj długość boku b: ")
c = input("Podaj długość boku c: ")

if (a+b) > c or (a+c) > b or (b+c) > a:
    print("Trójkąt można narysować")
else:
    print("Trójkąta nie można narysować!")

if a != b and a != c and b != c:
    print("Trójkąt jest różnoboczny")
elif a == b == c:
    print("Trójkąt jest równoboczny")
else:
    print("Trójkąt jest równoramienny")