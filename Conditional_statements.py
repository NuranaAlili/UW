# Define a function describe_length_difference() that takes in two strings as argument.
# The function should print one of the following sentences as appropriate:

# "The first string is longer by N characters"
# "The second string is longer by N characters"
# "The strings are the same length!"
#
# Try to only calculate the string difference once, and then use that value to determine what to print. Don't redo math if you can avoid it!


def describe_length_difference(str1, str2):
    if len(str1) > len(str2):
        print(f"The first string is longer by {len(str1)-len(str2)} characters")
    elif len(str2) > len(str1):
        print(f"The second string is longer by {len(str2)-len(str1)} characters")
    else:
        print("The strings are the same length!")

# Call your describe_length_difference() function by passing it different length strings to confirm that it works.
# Make sure to check all 3 conditions!


describe_length_difference("asdfgh", "asd")
describe_length_difference("ghk", "ghjhhj")
describe_length_difference("ghk", "ghk")

# Define a function lucky_sum() that takes in three numbers are arguments.
# This function should return the sum total of those three numbers, but ignoring any arguments that are either 4 or 13.
# Thus lucky_sum(5, 13, 11) would return a value of 16 (5+11), because the 13 would not be counted (as its unlucky). (This problem was adapted from CodingBat)

# Tip: consider checking for unlucky values and converting them into 0s, instad of trying to handle every possible combination of values.
# Caution: do not name a variable sum—that's a built-in function that you don't want to overwrite!
# You can call your lucky_sum function from this cell to test it. Make sure to try it with lots of different values!


def lucky_sum(num1, num2, num3):
    if (num1==4 or num1==13):
        num1=0
    if (num2==4 or num2==13):
        num2=0
    if (num3==4 or num3==13):
        num3=0
    return num1 + num2 + num3

print(lucky_sum(4, 10, 13))

# Consider the below decision tree:
#
# decision tree (in ed )
#
# This graph indicates a decision-making algorithm for choosing how many bedrooms (BR) to look for in an apartment, based on a number of factors. (The values here do not reflect Seattle housing... or any reality in fact. Just go with it).
#
# Define a function desired_bedrooms() that takes in 3 arguments in order: a number of expected occupants (a number), whether any of the occupants are partnered/married (a boolean), and a combined annual income (a number). The function should return the number of bedrooms that the user should look for.
#
# You can call your desired_bedrooms() function from this cell to test it. Make sure to try it with different values to test each path down the tree!


def desired_bedrooms(num_occupants, married, income):
    if num_occupants < 4:
        if income >= 40000:
            return 3
        else:
            if married:
                return 1
            else:
                return 2
    else:
        if married:
            return 3
        else:
            if income < 80000:
                return 2
            else:
                return 4

print(desired_bedrooms(3, True, 90000))


