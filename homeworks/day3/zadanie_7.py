# po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

miesiac = input("Podaj nazwę miesiąca: ")

miesiace_31_dni = ["styczeń", "styczen", "marzec", "maj", "lipiec", "sierpień", "sierpien", "październik", "pazdziernik", "grudzień", "grudzien"]
miesiace_30_dni = ["kwiecień", "czerwiec", "wrzesień", "listopad"]
luty = ["luty"]

if miesiac in miesiace_30_dni:
    print(miesiac + " ma 30 dni")
elif miesiac in miesiace_31_dni:
    print(miesiac + " ma 31 dni")
elif miesiac in luty:
    print(miesiac + " ma 28 lub 29 dni")
else:
    print("To nie jest nazwa miesiąca!")