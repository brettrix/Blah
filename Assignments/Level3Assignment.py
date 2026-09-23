#Author: Brett Rix

#Create a Python game in which the computer chooses a random 
#number and the player tries to guess that number. After each 
#valid guess, the program should tell the player whether to guess
#higher or lower.

import random

#Loop for continuous play
play_again = "Y"
while play_again == "Y" or play_again == "y":

    #Choose a random number.
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    #Start guessing loop and guess counter
    player_guess = int(input("What is your guess? "))
    number_of_guesses = 0

    #Game loop
    while player_guess != secret_number:

        #Number validation loop
        while player_guess > 100 or player_guess < 1:
            print("Pick a number between 1 and 100.")
            player_guess = int(input("What is your guess? "))

        #Hint generator
        if player_guess != secret_number:
            if player_guess > secret_number:
                print("The number is lower. Guess again.")
            else:
                print("The number is higher. Guess again.")

            #Increase counter and restart game loop
            number_of_guesses = number_of_guesses + 1
            player_guess = int(input("What is your guess? "))

    #Increase guess count to include correct guess in total guess count
    number_of_guesses = number_of_guesses + 1

    #print correct output based on total number of guesses
    print("Correct!")
    if number_of_guesses <= 3:
        print(f"Amazing! The number was {secret_number}.")
    elif number_of_guesses <= 5:
        print(f"Impressive! The number was {secret_number}.")
    elif number_of_guesses <= 7:
        print(f"Good job! The number was {secret_number}.")
    elif number_of_guesses <= 9:
        print(f"Took a little longer, but you got there! The number was {secret_number}.")
    elif number_of_guesses >= 10:
        print(f"You need to lock in. The number was {secret_number}.")
    print(f"You guessed it in {number_of_guesses} tries.")

    #Allow replay or end game
    print('Would you like to play again?') 
    play_again = input('Press "Y" to play again or any other letter to quit. ')