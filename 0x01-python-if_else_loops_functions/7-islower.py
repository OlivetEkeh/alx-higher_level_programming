#!/usr/bin/python3

def islower(c):
    # Get the Unicode value of the character
    unicode_value = ord(c)
    
    # Check if the Unicode value is within the range of lowercase letters
    return 97 <= unicode_value <= 122

# Test the function with example cases
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
