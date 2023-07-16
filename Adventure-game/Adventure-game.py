# Import necessary modules
import time
import random

colors = ["blue", "green", "red", "purple", "orange"]

# Define variables and constants
score = 0

# Define functions
# First function


def update_score(points):
    global score
    score += points
    print("Your score is:", score)

# Set up welcome message


def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)

wand_color = random.choice(colors)
print_pause("You find yourself standing in an open field,", 2)
print_pause("filled with grass and yellow wildflowers.", 2)

print_pause("Rumor has it that a wicked fairy is somewhere around here,", 2)
print_pause("and has been terrifying the nearby village.", 2)

print_pause("In front of you is a house.", 2)
print_pause("To your right is a dark cave.", 2)

# Second function
# Set up First initial choice


def knock_on_door(score):
    # Print the description of the First initial choice
    print_pause("You knock on the door, but no one answers. Do you:",2)
    print_pause("1. Walk away from the house and head towards the cave",2)
    print_pause("2. Keep knocking on the door of the house",2)

    # Start game loop
    # Start first loop
    while True:
        # Taking input(the choice)to continue the game
        choice = input("Enter your choice (1 or 2): ")
        # Suring the choice is valid(in 1 , 2 only)
        if choice in ["1", "2"]:
            break
        # If choice invalid print this message(ask for valid choice 1 & 2)
        else:
            print("Invalid choice. Please enter 1 or 2.")
    # first result in main loop
    if choice == "1":
        # Print description
        print_pause("You turn your back on the house and head towards the cave.",2)
        # Increase score
        update_score(1)
    # second choice in main loop
    elif choice == "2":
        # second result in main loop
        # Print the description
        print_pause("You keep knocking on the door, but still no one answers.",2)
        print_pause("You decide to give up and walk away.", 2)
        update_score(1)

    return score

# Third function
# Set up second initial choice


def enter_cave(score):
    # Print the description
    print_pause("You enter the dark cave and hear the sound of dripping water.",2)
    print_pause("Do you:",2)
    print_pause("1. Turn back and head towards the house",2)
    print_pause("2. Proceed further into the cave",2)

    # first loop in second initial choice
    while True:
        # Taking input(the choice)to continue the game
        choice = input("Enter your choice (1 or 2): ")
        # Suring the choice is valid(in 1 , 2 only)
        if choice in ["1", "2"]:
            break
        else:
            print_pause("Invalid choice. Please enter 1 or 2.",2)
    # first choice
    if choice == "1":
        # Print the description
        print_pause("You turn back and head towards the house.",2)
        update_score(1)
    # second choice
    elif choice == "2":
        treasure_chance = random.randint(1, 10)
        if treasure_chance <= 5:
            # Print the description
            print_pause("You proceed further into the cave,",2)
            print_pause("but find nothing of value.",2)
        else:
            print_pause("You proceed further into the cave and",2)
            print_pause("discover a hidden treasure!",2)
            # Increase score
            update_score(1)

    return score

# Fourth function


def make_choice(score):
    # Print the description
    print_pause("You are standing in front of a spooky house and a dark cave.",2)
    print_pause("What do you do?",2)
    print_pause("1. Knock on the door of the house",2)
    print_pause("2. Enter the cave",2)

    # Start loop
    while True:
        # Taking input(the choice)to continue the game
        choice = input("Enter your choice (1 or 2): ")
        # Suring the choice is valid(in 1 , 2 only)
        if choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    # first choice
    if choice == "1":
        score = knock_on_door(score)
    # second choice
    elif choice == "2":
        # Increase score
        score = enter_cave(score)

    return score

# Fifth function


def play_game():
    score = 0
    max_score = 3
    # Start the loop
    while score < max_score:
        score = make_choice(score)
        print_pause(f"Your current score is: {score} / {max_score}",2)

    if score == max_score:
        print_pause("Congratulations, you win!",2)
    else:
        print_pause("Sorry, you lose. Better luck next time!",2)

# Start the loop
while True:
    play_game()
    # Taking input(the choice)to continue the game or not
    play_again = input("Do you want to play again? Enter 'yes' or 'no': ")
    if play_again.lower() == "no":
        print_pause("Thanks for playing!",2)
        break