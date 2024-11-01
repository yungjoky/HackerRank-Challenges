from itertools import combinations

#input_str is the string we want to input and max_length is the length of this string for example:
#Hack 2 - Hack is the string, 2 is the max length of this string so the generated output won't go past
# 2 letters.
input_str, max_length = input().split()
#max_length = int(max_length) represents the number to an actual integer.
max_length = int(max_length)

for r in range(1, max_length + 1):
    for combo in combinations(sorted(input_str), r):
        print("".join(combo))
