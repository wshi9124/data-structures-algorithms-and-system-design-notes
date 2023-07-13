"""
Start with an initial string of zeros. Choose any digit to flip. When a diget is fliped its value and those to the right switch state between 1 and 0. 
Given a target string of binary digets, determine the minimum number of flips required to achieve the target

Example:
target = 01011
initial string -> 00000
Flip 3rd digit -> 00111
Flip 2nd digit -> 01000
Flip 4th digit -> 01011
Return 3 flips to reach target  
"""

def flips(self, target):
    flips = 0

    # 0 will become 1 and 1 will become 0 after each move
    # but the substring before current index in unchanged so traverse from left to right
    for letter in target:
    # we can find the current bit of string using flips%2 because we increment flips once a bit changes.
    # if the current bit not equal to the expected bit we need to flip the string
        if int(letter) != flips%2:
            flips += 1

    return flips


    
    # currentValue = "1"
    # result = 0

    # zero_ascii_value = ord("0")

    # for i in range(len(target)):
    #     if target[i] == currentValue:
    #         result += 1

    #         currentValueInAsciiValue = ord(currentValue)
    #         currentValue = chr(zero_ascii_value + ((currentValueInAsciiValue + 1) % 2))
    # return result
