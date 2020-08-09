# Challenge #372 [Easy] Perfectly Balanced. /r/dailyprogrammer
# Check if the amount of each character in a string are balanced
# without bonus points, and no validation


def balanced(string):
    return string.lower().count("x") == string.lower().count("y")


print("Enter string for evaluation: ")
inp = input()

if balanced(inp):
    print("Seems balanced to me")
else:
    print("Not balanced")







