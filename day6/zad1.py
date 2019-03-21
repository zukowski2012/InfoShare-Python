#niech to będzie plik fun8

#odwracanie listy
#Chcemy odwrocic zdanie (stringa) literka po literce, czyli:
# dla "Ala ma kota" otrzymać "atok am alA"

def odwroc_string(zdanie):
    return zdanie[::-1]
moje_zdanie = "Ala ma kota"

print(odwroc_string(moje_zdanie))