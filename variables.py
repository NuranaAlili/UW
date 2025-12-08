# Define a variable food that stores your favorite kind of food (as a string). Print the variable.

food = "burger"
print(food)

# Define a variable restaurant that stores your favorite place to eat that kind of food (as a string).

restaurant = "Red Robin"

# Print the message "I'm going to RESTAURANT for some FOOD", using your variables for the restaurant and food.
# Use concatenation (+) to combine the variables with the other text.

print("I'm going to " + restaurant + " for some " + food)

# Define a variable num_friends that stores the value of the number of friends you would like to eat with.

num_friends = 4

# Print a message "I'm going with X friends!", where the X is replaced with the previous variable.
# Remember to use the str() function to convert the number into a string.

print("I'm going with " + str(num_friends) + " friends!")

# Define a variable meal_price, which is how expensive (in number of dollars) you think one meal at the restaurant would be. This price should be a float (not an even amount).
# Print the variable--you do not need to convert it into a string to do this!

meal_price = 15.50
print(meal_price)

# Update (re-assign) the meal_price variable so it stores a value that is 15% higher (it now includes a tip!).
# Print the updated variable. Note that if you run this cell multiple times, the price will keep getting bigger;
# you can "reset" the initial price by executing the previous cell.

meal_price = meal_price + meal_price*0.15
print(meal_price)

# Define a variable total_cost that has the total estimated cost of the bill for you and all of your friends (don't forget yourself!). ' \
# 'Use your previous variables! Print this variable.

total_cost = meal_price * (num_friends+1)
print(total_cost)

# Define a variable budget that stores your spending budget for a night out.

budget = 100

# Define a variable max_friends, which is the maximum number of friends you can invite, at the estimated meal price, and be within your budget.
# Use your previous variables (and don't forget to pay for yourself)! Print the resulting value.
# Be carefully that you only invite whole people! You can do this by changing the float into an int.

max_friends = int(budget/meal_price)-1
print(max_friends)

# Bonus: Define a variable chorus that is the string "FOOD time!\n" (with FOOD replaced by your variable) repeated once for each of the friends you are able to bring.
# Hint use the * operator to add a string to itself multiple times. Print out the chorus variable.
# The \n is a "newline" character, and it's how you include a line break in a string.

chorus = food + " time!\n"
print(chorus * num_friends)