# Author: Sara Jane Kenny
# Purpose: A program that runs a practice quiz for students.

import random
import datetime

first_name = input("Enter your first name? ")
surname_name = input("Enter your surname? ")
date = datetime.date.today()

result = 0
feedback_lang = ""
lang_level = ""
feedback_math = ""
quiz_count = 0
percentage = 0
percentage_total = 0
user_finished = 'no'

f = open(f"logs.txt", "w")  # open filename, access mode

print(f"Welcome {first_name}")

while user_finished == 'no':

    # Get user choice of quiz
    print(f"\n1: Maths"
          f"\n2: Polish")
    user_choice = int(input(""))

    if user_choice == 1:
        q_asked = 1
        quiz_count += 1
        score = 0
        num_math_q = int(input(f"\n{first_name} how many questions? "))
        for a in range(num_math_q):
            random_num_one = random.randint(1, 12)
            random_num_two = random.randint(1, 12)

            # to stop negatives numbers only do subtraction if 1st rand num is greater or equal to the 2nd rand num
            if random_num_one >= random_num_two:
                print(f"{q_asked}:", random_num_one, "-", random_num_two, "= ", end="")
                rand_math_ans = random_num_one - random_num_two
                user_ans = int(input(""))
                feedback_math += f"\n{q_asked}: {random_num_one} - {random_num_two} = {user_ans}"
            else:
                # else just add the rand nums together
                print(f"{q_asked}:", random_num_one, "+", random_num_two, "= ", end="")
                rand_math_ans = random_num_one + random_num_two
                user_ans = int(input(""))
                feedback_math += f"\n{q_asked}: {random_num_one} + {random_num_two} = {user_ans}"

            # Add to score and finished the string output
            if rand_math_ans == user_ans:
                score += 1
                feedback_math += f" \u2705"
            else:
                feedback_math += f" \u274C should be {rand_math_ans}"

            # Calculate the score percentage and add 1 to questions asked count
            percentage = score / num_math_q
            percentage_total = percentage
            q_asked += 1

        # If the questions are finished print the feedback from the quiz
        if q_asked > num_math_q:
            print("\nFeedback:")
            if rand_math_ans == user_ans:
                print(f"{feedback_math}")
            else:
                print(f"{feedback_math}")
        print(f"\n{first_name}, you got {percentage:.0%} \U0001F389")

        percentage_avg = percentage_total / quiz_count

        print(f"{first_name} {surname_name} - MATHS - {date} : {percentage:.0%}", file=f)

        user_finished = input(f"Are you finished? (yes/no)")

    elif user_choice == 2:
        quiz_count += 1
        score = 0
        user_level = int(input(f"What is your current level {first_name}?"))

        if user_level == 1:
            connection = open("Polish1.txt", "r")
            lang_level = "Polish1"
        elif user_level == 2:
            connection = open("Polish2.txt", "r")
            lang_level = "Polish2"
        elif user_level == 3:
            connection = open("Polish3.txt", "r")
            lang_level = "Polish3"
        elif user_level == 4:
            connection = open("Polish4.txt", "r")
            lang_level = "Polish4"
        else:
            connection = open("Polish5.txt", "r")
            lang_level = "Polish5"

        for word in connection:
            word = word.rstrip()
            word = word.split(",")
            english_word = word[0]
            polish_word = word[1]

            print(f"{english_word} = ")
            user_word = input("")

            feedback_lang += f"\n{english_word} = {user_word}"

            # Add to score and finished the string output
            if user_word == polish_word:
                score += 1
                feedback_lang += f" \u2705"
            else:
                feedback_lang += f" \u274C should be {polish_word}"

            percentage = score / 3
            percentage_total = percentage

        # If the questions are finished print the feedback from the quiz
        print("\nFeedback:")
        if user_word == polish_word:
            print(f"{feedback_lang}")
        else:
            print(f"{feedback_lang}")
        print(f"\nResult: {score}/3\n{first_name}, you got {percentage:.0%} \U0001F389")

        if percentage > 70:
            if user_level < 5:
                print(f"The next time you use this program you should start with level {user_level + 1}")
        connection.close()

        percentage_avg = percentage_total / quiz_count

        print(f"{first_name} {surname_name}-{lang_level}-{date}: {percentage:.0%}", file=f)
        user_finished = input(f"Are you finished? (yes/no)\n")


print(f"Your average score for all quiz is {percentage_avg:.0%}"
      f"\nYour teacher can view details in log.txt")

f.close()
