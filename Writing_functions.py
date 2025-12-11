# Define a function add_three that takes a single argument and returns a value 3 greater than the argument.

def add_three(num):
    return num+3

# Call your add_three() function, passing it an argument of 7.
# Store the result in a variable ten, and print that variable.


ten = add_three(7)
print(ten)

# Try to call your add_three() function, passing it an argument of "7" (a string, in quotes).
# Consider: how could you help to avoid making this kind of error in the future?

# add_three("7")

# Define a function imperial_to_metric that takes in two arguments: a number of feet and a number of inches (in that order).
# The function should return the total length in meters. You'll need to look up the conversion factor to calculate this.

def imperial_to_metric(feet, inches):
    return (feet*0.3048) + (inches*0.0254)

# Define and print a variable height_in_meters by passing your height in imperial to the imperial_to_metric() function.


height_in_meters = imperial_to_metric(5, 2)
print(height_in_meters)


# Define a function compare_str_length that takes in 2 strings, and returns (does not print!) a sentence of the form

# "The difference in string lengths is N"
# Your function should work whether the first or second string is longer; consider using an absolute value.


def compare_str_length(str1, str2):
    N = str(abs(len(str1) - len(str2)))
    return "The difference in string lengths is " + N

# Pass two strings of different lengths to your compare_str_length() function.
# Do not print the returned value (though Jupyter will output it nonetheless).


compare_str_length("python", "jupyter")

# Define a function fraction_str() that takes two numbers as arguments representing a numerator and a denominator.
# the function should return a string version of that that fraction (e.g., "3/4").
# The arguments to this function should be keyword arguments named numerator and denominator, each with a default value of 1.
# You do not need to "simply" the fraction that you return.


def fraction_str(numerator = 1, denominator = 1):
    return (str(numerator) + "/" + str(denominator))

# Call the fraction_str() function with named arguments to produce the string "5/11", and print the result.
# Then for fun, try listing the (named) denominator argument before the numerator argument! What happens?


print(fraction_str(numerator = 5, denominator = 11))
print(fraction_str(denominator = 11, numerator = 5))


# Call the fraction_str() function only specifying a denominator argument of 3. Print the result.


print(fraction_str(denominator = 3))

# Call the fraction_str() function using positional arguments (unnamed arguments, just putting the values in order separated by a comma) to produce the string "11/5". Print the result.


print(fraction_str(11, 5))
