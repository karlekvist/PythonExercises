# Reddit/r/DailyProgrammer Challenge #374 [EASY]
# Take an integer N:
# 1 Add it's digits
# 2 Repeat until the result has 1 digit
# https://www.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence/


def additive_persistence(number):
    if number < 10:
        return 0
    return 1 + additive_persistence(sum(int(digit) for digit in str(number)))


print(additive_persistence(int(input("Please enter a number"))))
