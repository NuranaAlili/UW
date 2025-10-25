# Asks the user for their name
def ask_for_name():
    name = input("What's your name? \n>")
    return name


# Asks a question with several options and returns the number the user chose
def ask_multiple_choice_question(question_prompt, choice_num):
    response = input(f"{question_prompt}\n> ")
    if response.isdigit():
        number = int(response)
        if 1 <= number <= choice_num:
            return number
        else:
            print(f"Please enter a number between 1 and {choice_num}.")
            return ask_multiple_choice_question(question_prompt, choice_num)
    else:
        print(f"Invalid option. Please enter a number between 1 and {choice_num}.")
        return ask_multiple_choice_question(question_prompt, choice_num)


# Asks the user to type their favorite travel activity & returns the score that is used later
def ask_favorite_activity():
    activity = input("What's your favorite thing to do while traveling?\n"
                     "Hiking, Walking, Resting, Relaxing, Reading, Eating, Exploring\n>"
                     )
    lower_activity = activity.lower()

    if lower_activity.startswith("h") or lower_activity.startswith("w"):
        return 3
    elif lower_activity.startswith("r"):
        return 1
    elif lower_activity.startswith("e"):
        return 2
    else:
        return 2


# Asks one main question and a follow-up question & returns the score (1-3) to represent activity level
def ask_branching_question():
    branching_question = ask_multiple_choice_question(
        "Do you prefer outdoor or indoor activities?\n"
        "1. Outdoor\n"
        "2. Indoor",
        2
    )

    if branching_question == 1:  # If outdoor
        first_follow_up = ask_multiple_choice_question(
            "Which would you rather do?\n"
            "1. Hiking trail\n"
            "2. Swimming\n"
            "3. Taking photos of nature",
            3
        )
        if first_follow_up == 1:
            return 3  # hiking - active
        elif first_follow_up == 2:
            return 2  # swimming - moderate
        else:
            return 2  # taking photos - moderate
    else:  # If indoor
        second_follow_up = ask_multiple_choice_question(
            "Which would you rather do?\n"
            "1. Reading\n"
            "2. Watching movies\n"
            "3. Visiting a museum",
            3
        )
        if second_follow_up == 1:
            return 1  # reading - passive
        elif second_follow_up == 2:
            return 2  # movies - moderate
        else:
            return 2  # museum - moderate


# Prints the final travel type based on the total score
def report_results(score, name):
    print("\n" + "*" * 30)
    print(f"Results for {name}:")
    print(f"Total score: {score}")

    if score <= 6:
        print("You are a 'Passive Traveler'")
        print("You enjoy calm schedules, easy days, and recharging on trips.")
    elif score <= 9:
        print("You are a 'Balanced Traveler'")
        print("You like a balance: some exploring, some relaxing.")
    else:
        print("You are an 'Active Traveler'")
        print("You enjoy staying active and fill your days with new experiences.")
    print("*" * 30 + "\n")


# Runs the whole quiz
def take_quiz():
    print("\n" + "*" * 40)
    print("Quiz: 'What Type of Traveler Are You?'")
    print("*" * 40 + "\n")
    name = ask_for_name()
    print("\n" + "*" * 40)
    print(f"\nHi {name}! Let's find out your travel style!\n")
    print("*" * 40 + "\n")
    # question 1 > Beach=1 (passive), City=3 (active), Mountains=3 (active), Forest=2 (mix)
    player_choice_1 = ask_multiple_choice_question(
        "What's your ideal vacation spot?\n"
        "1. Beach\n"
        "2. City\n"
        "3. Mountains\n"
        "4. Forest",
        4
    )
    if player_choice_1 == 2 or player_choice_1 == 3:
        q1_points = 3
    elif player_choice_1 == 1:
        q1_points = 1
    else:
        q1_points = 2

    # question 2 > 1=3 (active), 2=2 (mix), 3=1 (passive), 4=2 (mix)
    player_choice_2 = ask_multiple_choice_question(
        "How do you usually spend a day on vacation?\n"
        "1. Wake up early and explore all day\n"
        "2. Sleep in and go with the flow\n"
        "3. Spend most of the day relaxing\n"
        "4. Mix of exploring and relaxing",
        4
    )
    if player_choice_2 == 2 or player_choice_2 == 4:
        q2_points = 2
    elif player_choice_2 == 1:
        q2_points = 3
    else:
        q2_points = 1

    activity_points = ask_favorite_activity()
    branch_points = ask_branching_question()
    total_score = q1_points + q2_points + activity_points + branch_points
    report_results(total_score, name)


if __name__ == '__main__':
    take_quiz()