from cs50 import get_string
import string

length=0

# I divided this program in 3 separate functions each one is in charge of counting letters, words and sentences respectively.
a = get_string("Please type the text to evaluate the reading level?\n")

length = len(a)


def main ():

    total_letters = (len(a) - count_letters(a))

    index = round(0.0588 * ((total_letters * 100) / count_words(a)) - (0.296 * ((count_sentences(a) * 100) / count_words(a))) - 15.8)

# Here we evaluate the result of the index formula and state the level of readability of text.

    if (index < 1):

        print("Before Grade 1")

    elif (1 >= index or index < 16):

        print(f"Grade {round(index)}")

    else:

        print("Grade 16+")

# This first function is to count the spaces and punctuation of the text, I use a for loop
# for that. The remainder should be the letters, thats why I substract this fucntion from the
# strlength upwards.

def count_letters(a):

    L = 0

    for i in range(length):

        c = a[i]

        if c.isspace():

            L += 1

    for i in a:
        if i in string.punctuation:
            L += 1

    return L

#  This second function is to count the words in the text. I use a for loop to go trough the text
# and count the spaces using the logic that after each space there should be a word. I also
# covered the double spaces at the beginning and end of the text so that the grade should not be
# affected or also in the middle of words.

def count_words(a):

    count = 0

    for i in range(length):

        c = a[i]

        x = c.isspace() and a[i + 1].isspace()

        if (x):

            continue

        elif c.isspace() or c.isalpha and (i != length - 1) and count == 0:

            count += 1

        elif c.isspace() and (i != length - 1) and (count >= 1):

            count += 1

        elif c.isspace() and (i == length - 1):

            continue

        else:

            continue


    return count

# This last function is to count the sentences taking into consideration dots, exclamation
# points and interrogation signs as new setences I am also using a for loop that.

def count_sentences(a):

    S = 0
    for i in range(length):

        c = a[i]
        if ((c == '.') or (c == '!') or (c == '?')):

            S += 1

    return S


count_letters(a)
count_words(a)
count_sentences(a)
main()
