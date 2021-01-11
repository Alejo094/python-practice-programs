from cs50 import get_int
import math


number=0
count=0
suma=0
numb_size= 0
luhns_factor=0

card_num = get_int("Number: ")

while (card_num<0):
    card_num = get_int("Number: ")

card_num = str(card_num)

l_num= len(card_num)

if ((l_num!=13 ) and (l_num!=15) and (l_num!=16)):

    print("INVALID")

if (l_num==13):

    for i in range(1,l_num,2):

        numb_size = int(card_num[i])
        luhns_factor =int(card_num[i])*2

        if luhns_factor >=10:
            suma +=math.floor(luhns_factor%100 /10) + luhns_factor %10
        else:
            suma += luhns_factor

    for i in range(0,l_num,2):
        suma+=int(card_num[i])

    if (int(card_num[0]) == 4 and suma%10 == 0):

        print("VISA")

    else:

        print("INVALID")

if (l_num==15):

    for i in range(1,l_num,2):

        numb_size = int(card_num[i])
        luhns_factor =int(card_num[i])*2

        if luhns_factor >=10:
            suma +=math.floor(luhns_factor%100 /10) + luhns_factor %10
        else:
            suma += luhns_factor

    for i in range(0,l_num,2):
        suma+=int(card_num[i])

    if int(card_num[0]) == 3 and suma%10 == 0 and (int(card_num[1]) == 7 or int(card_num[1]) == 4):

        print("AMEX")

    else:

        print("INVALID")

if (l_num==16):

    for i in range(0,l_num,2):

        numb_size = int(card_num[i])
        luhns_factor =int(card_num[i])*2

        if luhns_factor >= 10:
            suma +=math.floor(luhns_factor%100 /10) + luhns_factor %10
        else:
            suma += luhns_factor

    for i in range(1,l_num,2):
        suma+=int(card_num[i])

    if int(card_num[0]) == 4 and suma%10 == 0:

        print("VISA")

    elif int(card_num[0]) == 5 and suma%10 == 0 and (int(card_num[1]) <= 5):

        print("MASTERCARD")
    else:
        print("INVALID")


