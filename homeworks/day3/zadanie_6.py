# 6. blackjack - na inpucie wejście 2 karty
#   wartości: 2-9, J Q K = 10, A = 1 lub 11
#   określ ruch jaki powinien być wykonany:
#   jeszcze jedna karta, stop,

card0 = str(input("Podaj pierwszą kartę:"))
card1 = str(input("Podaj drugą kartę:"))

# A = 1 lub 11
punkty_min = 0
punkty_max = 0
high_card_points = 10
low_ace_points = 1
high_ace_points = 11
win_points = 21

if card0 in "23456789":
    punkty_min = punkty_min + int(card0)
    punkty_max = punkty_max + int(card0)
elif card0 in "JQK":
    punkty_min = punkty_min + high_card_points
    punkty_max = punkty_max + high_card_points
elif card0 in "A":
    punkty_min = punkty_min + low_ace_points
    punkty_max = punkty_max + high_ace_points

if card1 in "23456789":
    punkty_min = punkty_min + int(card1)
    punkty_max = punkty_max + int(card1)
elif card1 in "JQK":
    punkty_min = punkty_min + high_card_points
    punkty_max = punkty_max + high_card_points
elif card1 in "A":
    punkty_min = punkty_min + low_ace_points
    punkty_max = punkty_max + high_ace_points

## mamy punkty
## sprawdzamy czy brać dalej

if punkty_min == 21 or punkty_max   == 21:
    print("stop, masz 21 pkt")
elif punkty_min > 18 or punkty_max > 18:
    print("stop, masz conajmniej 19 pkt")
else:
    print("jeszcze jedna")