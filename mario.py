from cs50 import get_int

height = get_int("Height: ")

while height < 1 or height > 8:
    height = get_int("Height: ")

for j in range(height):
    i= height - 1
    print(" "* i + "#" *(j)
    height -=1