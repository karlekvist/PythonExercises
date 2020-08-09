# Challenge #375 [Easy] Print a new number by adding one to each of its digits.
# https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/

# Note after completion: Can be improved further on.

import math as m


def add_one(number):
    amount_of_digits = int(m.log10(number) + 1)
    power = 0
    result = 0
    for i in range(amount_of_digits):
        digit = int((number % pow(10, i+1)) / pow(10, i)) + 1
        result += digit * pow(10, power)
        power += 2 if digit == 10 else 1
    return result


inp = int(input("Please enter a number to increase: "))

print(add_one(inp))
