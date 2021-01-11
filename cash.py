from cs50 import get_float
import math

cash = get_float("Change owed: ") *100

while cash < 0:
   cash = get_float("Change owed: ") *100

value_left = cash

numb_coins25 = 0

numb_coins10 = 0

numb_coins5 = 0

numb_coins1 = 0


if (cash/25) >= 1:

    numb_coins25 = (cash/25)

    value_left = cash - (math.floor(numb_coins25)*25)

    if (value_left/25).is_integer():
        print(math.floor(numb_coins25))


if (value_left/10) >= 1:

    numb_coins10 = value_left/10

    value_left = value_left - (math.floor(numb_coins10)*10)

    numb_coinsT =  math.floor(numb_coins25) +  math.floor(numb_coins10)

    if (value_left/10).is_integer():
        print(numb_coinsT)

if (value_left/5) >= 1:

    numb_coins5 = value_left/5

    value_left  = value_left - (math.floor(numb_coins5)*5)

    numb_coinsT =  math.floor(numb_coins25) + math.floor(numb_coins10) + math.floor(numb_coins5)

    if (value_left/5).is_integer():
        print(numb_coinsT)


if value_left >= 1:

    numb_coins1 = value_left

    value_left = value_left - (math.floor(numb_coins1))

    numb_coinsT =  math.floor(numb_coins25) + math.floor(numb_coins10) + math.floor(numb_coins5) +  math.floor(numb_coins1)

    if (value_left/1).is_integer():
        print(numb_coinsT)






