gra = "xon" \
      "oxo" \
      "xox"
# sprawdzamy czy wygrane po przekatnych

if (gra[0] == gra[4] == gra[8]) or (gra[2] == gra[4] == gra[6]):
    if not gra[4] == "n":
        print("Wygrał {}".format(gra[4]))
# sprawdzmy kazdy rzad

elif (gra[0] == gra[4] == gra[8]):
    if gra[0] == "n":
        print("Wygrał {}".format(gra[4]))