gra = "xon" \
    "ono" \
    "xox"
#sprawdzamy czy wygrane po przekatnych

if gra[0] == gra[3] == gra[8] or gra[0] == gra[3] == gra[8]:
    if not gra[4] == "n":
        print("Wygrał {}".format(gra[4]))
#sprawdzmy akzdy rzad
elif gra[0:3] == "xxx" or gra[0:3] == "ooo":

#sprawdzamy po przekatnych