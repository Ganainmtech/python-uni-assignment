# Author: Sara Jane Kenny
# Purpose: A program that runs a practice quiz for students.

import random
import datetime

first_name = input("Enter your first name? ")
surname_name = input("Enter your surname? ")

score = 0
result = 0
feedback = ""
q_asked = 1
percentage = 0
user_finished = 'no'

f = open(f"logs.txt", "w")  # open filename, access mode
print(f"First Name: {first_name} - ", file=f)
print(f"Surname Name: {surname_name} - ", file=f)
f.close()

print(f"Welcome {first_name}")

while user_finished == 'no':

    # Get user choice of quiz
    print(f"\n1: Maths"
          f"\n2: Polish")
    user_choice = int(input(""))

    if user_choice == 1:
        num_math_q = int(input(f"\n{first_name} how many questions? "))
        for a in range(num_math_q):
            random_num_one = random.randint(1, 10)
            random_num_two = random.randint(1, 10)

            # to stop negatives numbers only do subtraction if 1st rand num is greater or equal to the 2nd rand num
            if random_num_one >= random_num_two:
                print(f"{q_asked}:", random_num_one, "-", random_num_two, "= ", end="")
                rand_math_ans = random_num_one - random_num_two
                user_ans = int(input(""))
                feedback += f"\n{q_asked}: {random_num_one} - {random_num_two} = {user_ans}"
            else:
                # else just add the rand nums together
                print(f"{q_asked}:", random_num_one, "+", random_num_two, "= ", end="")
                rand_math_ans = random_num_one + random_num_two
                user_ans = int(input(""))
                feedback += f"\n{q_asked}: {random_num_one} + {random_num_two} = {user_ans}"

            # Add to score and finished the string output
            if rand_math_ans == user_ans:
                score += 1
                feedback += f" \u2705"
            else:
                feedback += f" \u274C should be {rand_math_ans}"

            # Calculate the score percentage and add 1 to questions asked count
            percentage = float(score / q_asked * 100)
            q_asked += 1

            # If the questions are finished print the feedback from the quiz
            if q_asked > num_math_q:
                print("\nFeedback:")
                if rand_math_ans == user_ans:
                    print(f"{feedback}")
                else:
                    print(f"{feedback}")
        print(f"\n{first_name}, you got {percentage:,.0f}% \U0001F389")

    #user_finished = input(f"Are you finished? (yes/no)")
    #print("Goodbye!")

    elif user_choice == 2:
        connection = open("polish.txt", "r")

        for word in connection:
            word = word.rstrip()
            word = word.split(",")
            english_word = word[0]
            polish_word = word[1]

            print(f"{english_word} = ")
            user_word = input("")

            feedback += f"\n{english_word} = {user_word}"

            # Add to score and finished the string output
            if user_word == polish_word:
                score += 1
                feedback += f" \u2705"
            else:
                feedback += f" \u274C should be {polish_word}"

            percentage = float(score / 3 * 100)

        # If the questions are finished print the feedback from the quiz
        print("\nFeedback:")
        if user_word == polish_word:
            print(f"{feedback}")
        else:
            print(f"{feedback}")

        print(f"\nResult: {score}/3\n{first_name}, you got {percentage:,.0f}% \U0001F389")
        connection.close()

