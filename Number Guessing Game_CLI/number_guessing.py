import random, sys


def welcome_message():
    print("Welcome to the Number Guessing Game! \n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("4. Exit Game")

    choice = int(input())

    if choice == 1:
        chances = 10
        print("Great! You have selected the Easy difficulty level.")
        print(f"You have {chances} chances to guess the correct number.")
        print("Let's start the game!")
        return chances
    elif choice == 2:
        chances = 5
        print("Great! You have selected the Medium difficulty level.")
        print(f"You have {chances} chances to guess the correct number.")
        print("Let's start the game!")
        return chances
    elif choice == 3:
        chances = 3
        print("Great! You have selected the Hard difficulty level.")
        print(f"You have {chances} chances to guess the correct number.")
        print("Let's start the game!")
        return chances
    elif choice == 4:
        print("Thank You - Visit Again")
        sys.exit()
        # break

def rand_num_generator():
    rand_num = random.randint(1, 100)
    return rand_num

# def play_game():
#     return

def guessing_logic(chances, random_number):

    while chances:
        user_number = int(input("Enter your guess: "))

        if user_number == random_number:
            print(f"Congratulations! You Guessed the Correct Number")
        else:
            print("Incorrect! Guessed number is Wrong")

    return


chances = welcome_message()
random_number = rand_num_generator()

# print(chances)
# print(random_number)




