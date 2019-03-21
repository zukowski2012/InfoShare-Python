# 7P. if elif else
# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

wiek = int(input("Proszę podać wiek psa: "))
if wiek <= 2:
    wiek_psi = wiek * 10.5
    print("Na ludzkie lata Twój pies ma: " + str(wiek_psi))
else:
    wiek_psi = (wiek - 2) * 4 + 21
    print("Na ludzkie lata Twój pies ma: " + str(wiek_psi))

