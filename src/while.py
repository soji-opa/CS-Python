# while loop = syntax to write a while loop
""" structure - initializing statement; while condition; what you want done; 
what keeps condition running

A while loop in python can also have an else statement
"""

# i = 1
# while i<=5:
#     print('*' * i)
#     i = i + 1
# print("Done")

""" Guessing game """

secret_number = 9
guess_count = 0
guess_limit = 3
trials = guess_limit - guess_count
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("you won")
        break
    elif guess != secret_number and guess_count < guess_limit:
        trials = guess_limit - guess_count
        print(f"You have tried {guess_count} times and you have {trials} trials left")
        print("try again")

