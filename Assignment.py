# Author: Sara Jane Kenny
# Purpose: A program that runs a practice quiz for students.

import random

first_name = input("Enter your first name? ")
surname_name = input("Enter your surname? ")

score = 0
result = 0
q_asked = 1

f = open(f"feedback.txt", "w")  # open filename, access mode
print(f"First Name: {first_name}", file=f)
print(f"Surname Name: {surname_name}", file=f)
f.close()

num_math_q = int(input(f"\n{first_name} how many questions? "))

for a in range(num_math_q):
    random_num_one = random.randint(1, 10)
    random_num_two = random.randint(1, 10)

    print(f"{q_asked}:", random_num_one, "+", random_num_two, "= ", end="")
    rand_math_ans = random_num_one + random_num_two
    user_ans = int(input(""))

    if rand_math_ans == user_ans:
        score += 1
    else:
        if q_asked == 5:
            print(f"should be {rand_math_ans}")

    q_asked += 1

    for b in range(num_math_q):
        q_asked = 1

        print(f"\nFeedback:")

        print(f"\n{q_asked}:", random_num_one, "+", random_num_two, "=", user_ans, end="")

        if rand_math_ans == user_ans:
            print(" Correct")
        else:
            print(f" Incorrect, Should be {rand_math_ans}")

print(f"\n{first_name} you got {score}/{q_asked - 1}")
