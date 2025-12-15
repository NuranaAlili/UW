"""
Exercise: Python Scripts

In this exercise you will practice writing a simple Python script. This script will be an "interactive tech support" bot, which helps people with their computer problems:

Have you tried turning it off and on again? (y/n) y
How many times? 2
Try it one more time and get back to me.
The bold text is what is typed in by the user.

Note that you'll be building this program a bit "from the inside out." You can test your program by running the command: python exercise.py from the Terminal, and then interacting with it there. Note that the auto-marking is checking against particular sets of inputs and outputs, so will not give much feedback about the style or structure of your code.

Exercise Instructions
1. In your script, first define a function called ask_how_many_times(). This function takes in no arguments, and should prompt the user (using the input() function) with the question: "How many times?" The function should take the number that the user inputs (what is returned by the input() function), and return that value as a number.

input() returns a string; you can convert that string to a number using the int() function.

Make sure to include an extra space after the ? in the prompt so that there is some space before the user's input.

2. Next, define a function called ask_have_you_tried(). This function should expect a single argument, a string. It should do the following:

Prompt the user with the question "Have you tried ARGUMENT? (y/n)" (replacing the word ARGUMENT with whatever value was passed as the argument).

If the user enters a "y", then the function should ask them how many times they've tried that (using your ask_how_many_times() function). Note that you should save the returned value in a variable to keep your code clean.

Then if the number of times is less than 3, then the function should print the message "Try it one more time and get back to me." If the number of times is 3 or greater, then the function should print the message "I'll look into it and get back to you."

If the user enters a "n", then the function should print the message "Try that and get back to me."

3. Finally, your script should call your ask_have_you_tried() function, passing it an argument of "turning it off and on again" (src). However, you should only call this when your script is run as an executable script, not loaded as a module. You can check that the script is being run as a top-level script with an if statement:

if __name__ == "__main__":
    # is run as a script, call code here
Put this at the bottom of your script, after the functions are defined.
"""

def ask_how_many_times():
    num = int(input("How many times? "))
    return num

def ask_have_you_tried(str):
    response = input(f"Have you tried {str}? (y/n) ")
    if response == "y":
        num = ask_how_many_times()
        if num < 3:
            print("Try it one more time and get back to me.")
        else:
            print("I'll look into it and get back to you.")
    else:
        print("Try that and get back to me.")

if __name__ == "__main__":
    # is run as a script, call code here

    ask_have_you_tried("turning it off and on again" )