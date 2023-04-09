# Word Input
word = input("Word: ")

# Shift Input
shift = input("Shift: ")
shift = int(shift)

# Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Character to Integer
char_to_int = list()
for character in word:
    for integer in range(len(alphabet)):
        if character == alphabet[integer]:
            char_to_int.append(integer)

# Integer to Character
# number_to_word = list()

# print(''.join(map(str, number_to_word)))

