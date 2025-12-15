# Define a variable num whose value is a random whole number between 1 and 20 (use the random.randint() function).
# Print the variable.

import random
num = random.randint(1, 20)
print(num)

# Write a boolean expression that represents whether or not num is equal to 12.


print(num == 12)

# Write a boolean expression that represents whether num is either less than 5 or greater than 15.
# (Note that in programming, we always assume "strictly greater/less than" unless otherwise specified).
# Do not print out the result; just write the expression!

print(num < 5 or num > 15)

# Define a function is_odd_stat() that expects a single whole number as a argument.
# This function shold return a boolean value (True or False) representing whether or not the argument is between 3 and 18 (both inclusive) while also being an odd number.

# You can determine is a number is odd by using the module % operator to get the remainder when dividing by 2.
# So If a number % 2 is 0, then the number was even!

def is_odd_stat(n):
    return (3 <= n <= 18 and n%2 != 0)

# Call your is_odd_stat() function, passing in your random number as an argument to see if it works.


print(is_odd_stat(num))

# You can and should re-run the above cells multiple times to confirm that the logic holds for different random numbers!


# Define a variable word whose value is your favorite word (a string)


word = "Butterfly"

# Write a boolean expression that represents if the inputted word has more than 8 letters.


print(len(word)>8)

# Use the islower() string method to check if the inputted word was entered with all lower-case letters.


print(word.islower())

# Define a function has_i_or_n() that expects a string as an argument.
# This function should return a boolean value representing whether or not the word starts with the letter i or ends with the letter n.
# Use appropriate string methods to check what the word startswith and endswidth.
# Hint: first convert the word to a specific case (upper or lower) before checking the word ends; that way you only have to check a single case!


def has_i_or_n(str):
    str = str.lower()
    return str.startswith("i") or str.endswith("n")



# Call your has_i_or_n() function, passing your inputted word as an argument to see if it works!

print(has_i_or_n(word))

# Extra optional challenge: Define a function de_morgan() that takes in two boolean values (P and Q) and returns whether the De Morgan laws hold for those two values. That is:

# the negation of P and Q is the same as the negation of P or the negation of Q and
# the negation of P or Q is the same as the negation of P and the negation of Q

# Your function should return a boolean representing whether or not both of these statements are true for the given P and Q.
# Use parentheses to enforce order of operations!


def de_morgan(P, Q):
    return (not (P and Q)) == ((not P) or (not Q))
    return (not (P or Q)) == ((not P) and (not Q))

# Call your de_morgan() function for each possible value of P and Q (there are 4 possible combinations), printing the result, in order to demonstrate that these laws hold.


print(de_morgan(True, True))
print(de_morgan(True, False))
print(de_morgan(False, True))
print(de_morgan(False, False))


