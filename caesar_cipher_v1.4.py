# Word Input
word = input("Word: ")

# Shift Input
shift = input("Shift: ")
shift = int(shift)

# Alphabet
alphabet = " abcdefghijklmnopqrstuvwxyz"

# Character to Integer
char_to_int = list()
for character in word:
    for integer in range(len(alphabet)):
        if character == alphabet[integer]:
            char_to_int.append(integer)

# Add number of shift to Integer
shift_char_to_int = list()
for digit in char_to_int:
    if digit != 0:
        sum_shift = shift + digit
        if sum_shift >= 1 and sum_shift <= 26:
            shift_char_to_int.append(sum_shift)
        elif sum_shift > 26:
            sum_shift = sum_shift % 26
            shift_char_to_int.append(sum_shift)
    else:
        sum_shift = digit
        shift_char_to_int.append(sum_shift)
            

# Integer to Character
int_to_char = list()
for character in shift_char_to_int:
    for integer in range(len(alphabet)):
        if character == integer:
            int_to_char.append(alphabet[integer])


print(''.join(map(str, int_to_char)))

