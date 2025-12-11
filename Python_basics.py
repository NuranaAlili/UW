# Part 1. Introductions

# 1. Create a variable my_name that stores your name (a string). [1pt]


my_name = "Nurana"

# 2. Create a variable my_age that stores your age (as a number). [1pt]

my_age = 30

# 3. Define a function make_introduction() that takes in two arguments: a name and an age. The function should return a string of the format "Hello, my name is {NAME} and I'm {AGE} years old." (replacing {NAME} and {AGE} with the arguments). [6pt]

# Note that you can turn a number into a string using the built-in str() function.

def make_introduction(name, age):
    return ("Hello, my name is " + name + " and I'm " + str(age) + " years old.")

# 4. Create a variable my_intro by passing your variables my_name and my_age into your make_introduction() function. Print the variable after you create it. [2pt]

my_intro = make_introduction(my_name, my_age)
print(my_intro)

# 5. Create a variable loud_intro, which is your my_intro variable with all of the letters capitalized (use the upper() string method). Print the variable after you create it. [2pt]

loud_intro = my_intro.upper()
print(loud_intro)

# 6. Create a variable casual_intro by using the replace() string function to replace (substitute) "Hello, my name is", with "Hey, I'm" in your my_intro variable. You may need to look up the arguments for this function! Print the variable after you create it. [3pt]


casual_intro = my_intro.replace("Hello, my name is", "Hey, I'm")
print(casual_intro)

# 7. Create a variable intro_e_count that stores the number of times the letter 'e' (lower-case only) appears in the my_intro variable. Find a string method that will "count" the occurences. Print the variable after you create it. [3pt]


intro_e_count = my_intro.count("e")
print(intro_e_count)

# Part 2. Money

# 8. Define a function compound_interest() that takes three numbers as arguments: an initial bank balance (principle, in dollars), an annual interest rate (as a decimal, so use .05 as 5%), and a number of years. The function should calculate the continuous compound interest and return the resulting total balance after that many number of years. [9pt]

# See here for an example of the formula and a calculator you can use to check your work.
# Be sure and call your function with some testing numbers: $1000 at 6% for 5 years should lead to a balance of $1349.86.
# You will need to import the math module for mathematical functions.

import math
def compound_interest(initial_principle, interest_rate, years):
    total_balance = initial_principle * math.exp(interest_rate*years)
    return(round(total_balance, 2))

# 9. Define a function print_earnings() that takes three numbers as arguments: an initial principle, an annual interest rate (as a decimal, so use .05 as 5%), and a number of years. This function should print out the earnings over this period in the following format:

# Initial principle: $1000
# Annual interest rate: %6.0
# Interest earned in 5 years: $349.86
# Total value after 5 years: $1349.86
# You must use your previous compound_interest() function to calculate the amounts; don't write the same equation more than once! Note that interest rate should be printed as a percentage, monetary values should have a leading $, and you should round monetary values to the nearest penny. Don't worry about extra or missing trailing 0s (in values like %6.0 or $101.5). [7pt]


def print_earnings(initial_principle, interest_rate, years):
    total_balance = compound_interest(initial_principle, interest_rate, years)
    interest_earned = round(total_balance - initial_principle, 2)
    print("Initial principle: $" + str(initial_principle))
    print("Annual interest rate: %" + str(interest_rate*100))
    print(f"Interest earned in {years} years: ${interest_earned}")
    print(f"Total value after {years} years: ${total_balance}")

# 10. Define a function value_of_change() that takes in named arguments representing amounts of different US coins (quarters, dimes, nickels, and pennies)--each of the arguments should have a default value of 0. The function should return the total value in dollars of those coins. For example, 5 quarters, 4 dimes, 3, nickels, and 2 pennies have a value of 1.82 dollars. [6pt]

# Hint: add up all of the "cents" and then convert that into a number of dollars

def value_of_change(quarters = 0, dimes = 0, nickels = 0, pennies = 0):
    total_value = round((quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01), 2)
    return total_value

# 11. Define a function consolidate_change that takes as arguments counts of different US coins (similar to the previous function) and prints out the simplest number of bills and coins needed to make that amount. [11pt]

# For example, when called with arguments of 10 quarters, 9 dimes, 8 nickels, and 7 pennies, the function should print:

# Number of dollars: 3
# Number of quarters: 3
# Number of dimes: 1
# Number of nickels: 0
# Number of pennies: 2
# Total amount: $3.87
# You must use your previous value_of_change() method in this calculation to determine the total amount.
#
# Hint: think about converting the coins to a giant pile of pennies, and then determining how many (whole number) dollars you can divide them into. Then put those pennies aside, and determine how many (whole number) quarters you can make with the rest, etc.
def consolidate_change(quarters = 0, dimes = 0, nickels = 0, pennies = 0):
    total_amount = round(value_of_change(quarters, dimes, nickels, pennies)*100)
    dollars = int(total_amount // 100)
    total_pennies = total_amount % 100
    quarters_count = int(total_pennies // 25)
    total_pennies = total_pennies % 25
    dimes_count = int(total_pennies // 10)
    total_pennies = total_pennies % 10
    nickels_count = int(total_pennies // 5)
    pennies_count = int(total_pennies % 5)

    print(f"Number of dollars: {dollars}")
    print(f"Number of quarters: {quarters_count}")
    print(f"Number of dimes: {dimes_count}")
    print(f"Number of nickels: {nickels_count}")
    print(f"Number of pennies: {pennies_count}")
    print(f"Total amount: ${round(total_amount/100,2)}")


# 12. Call your consolidate_change() function to test it, passing in some number of coins for it to consolidate (the values you pass are your choice!) [1pt]


consolidate_change(10, 9, 8, 7)

# Part 3. Time
# Note: this is the hardest part of the assignment! Plan accordingly.


# 13. Import the date value from the datetime module. [2pt]


from datetime import date

# 14. Use the date() function from the datetime module to create a variable end_of_quarter that represents the last day of the current quarter (check the UW Calendar). Note that this function will return a value of type date (not a string or a number). [2pt]


end_of_quarter = date(2025, 12, 12)

# 15. Create a variable today that represents the current date. [2pt]


today = date.today()

# 16. Create a variable days_to_break that is how many days from the current date until the end of the current quarter. Hint: subtract the date variables you just made! Print the variable after you create it; your printed output can include a 00:00:00 timestamp. days_to_break will be a timedelta value (a difference in time), not a string! [2pt]


days_to_break = end_of_quarter - today
print(days_to_break)

# 17. Define a function when_can_vote_us() that takes as an argument a birth date (as a date value!). This function should return the date in which a person born on that day can legally vote in the US (i.e., when they turn 18 years old). [9pt]

# In order to calculate this date, you should use the dateutil.relativedelta module, which is included with Anaconda. You will need to import the relativedelta function from this module, which will let you specify a "time change" in terms of years (using a named argument) that can then be added (+) to a date value. See the examples for details.


from datetime import date
from dateutil.relativedelta import relativedelta

def when_can_vote_us(birth_date: date):
    return birth_date + relativedelta(years=+18)

# 18. Demonstrate your when_can_vote_us function works by printing out when someone born today will be able to vote. [2pt]


print(when_can_vote_us(today))

# 19. Define a function make_birthday_announcement() that takes in two arguments: a name (as a string), and a date of birth (as adate--not a string!). This function should return a string of the format "{NAME}'s birthday is in {N} days" (replacing {NAME} with the argument, and {N} with the number of days rom today until the person's next birthday). [16pt]

# This algorithm can be a bit tricky! A few tips:

# If you use the relativedelta() function rather than the subtraction operator to produce a "time difference", you'll be able to extract the number of days or years in that difference by by accessing the .days or .years properties (e.g., time_difference.years).
# Once you've determined how many years old the person currently is, you can use that number to figure out the date that they turn one year older (similar to how you calculated voting age).
# You can then calculate the time difference between the their next birthday and today. You can just use normal subtraction to calculate the difference, because the values are already relativedeltas. You can then access the number of .days in that difference value.
# Other approaches are also acceptable; the goal here is to practice with algorithmic approaches and functions!


def make_birthday_announcement(name, birth_date):
    today = date.today()
    time_difference = relativedelta(today, birth_date)
    age = time_difference.years
    next_birthday = birth_date + relativedelta(years=age+1)
    days_remaining = (next_birthday - today).days

    return f"{name}'s birthday is in {days_remaining} days"

# 20. Create a variable my_bday_announcement by calling your make_birthday_announcement() function and passing in your name (use your existing variable!) and your birthdate. Print the variable after you create it. [2pt]


my_bday_announcement = (make_birthday_announcement(my_name, date(1991, 6, 12)))
print(my_bday_announcement)
