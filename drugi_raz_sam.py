# policz samogłoski i spółgłoski

zdanie = input("Podaj jakieś zdanie: ")

samogloski = 0
spolgloski = 0

lista_samoglosek = "aeiouyąęó"
for litera in zdanie:
    if litera.isalpha():
        if litera in lista_samoglosek:
            samogloski += 1
        else:
            spolgloski += 1
print(f"Samoglosek: {samogloski}, spółgłosek: {spolgloski}")
