# Define a variable my_name that contains your name (first and last) as a string.

my_name = "Nurana Alili"

# Use the len() function to determine how many characters are in your name (including punctuation),
# and assign that value to a variable name_length. Print out the name_length variable.

name_length = len(my_name)
print(name_length)

# Print the result of dividing 499 by your name_length, rounded to 1 decimal place.
# Use the round() function (you'll need to specify a second argument). ' \
#                              'It's fine to do this without creating a new variable.

print(round((499/name_length), 1))

# Print out your name with the uppercase letters made lowercase, and the lowercase letters made uppercase.
# You'll need to look for a string method that will swap the case of the string. ' \
#    'Remember that you call string methods using dot notation (e.g., my_string.method()). ' \
#         'It's fine to do this work without creating a separate variable.

print(my_name.swapcase())

# Define a variable fruits that contains the string "apples and bananas"
fruits = "apples and bananas"

# Use the replace() method to substitute all the "a"s in fruits with "ee".
#     Store the result in a variable called fruits_e.

fruits_e = fruits.replace("a", "ee")

# Use the replace() method to substitute all the "a"s in fruits with "o".
#     Store the result in a variable called fruits_o.

fruits_o = fruits.replace("a", "o")


# Print out the string "I like to eat " followed by each of fruits, fruits_e and fruits_o (three sentences total;
# you can use three print statements for this). You can even sing along!

print("I like to eat " + fruits)
print("I like to eat " + fruits_e)
print("I like to eat " + fruits_o)