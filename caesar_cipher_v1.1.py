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

# Add number of shift to Integer
shift_char_to_int = list()
for digit in char_to_int:
    sum_shift = shift + digit
    shift_char_to_int.append(sum_shift)    

# Integer to Character

# print(''.join(map(str, int_to_char)))

