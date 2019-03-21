# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

temperatura = input("Proszę podać temperaturę (bez jednostki): ")
temperatura = float(temperatura)
jednostka = input("Proszę podać jednostkę (C lub F): ")
F = temperatura * (9 / 5) + 32
F = str(F)
C = (temperatura - 32) * (5 / 9)
C = str(C)

if jednostka == "C" or jednostka == "c":
    print(F + "F")
elif jednostka == "F" or jednostka == "f":
    print(C + "C")
else:
    print("Coś poszło nie tak... :( ")
