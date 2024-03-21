import random
import time
from os import name as os_name

num = random.randint(1, 200)

def welcome_message():
    print("May I ask you for your name? : ")
    player_name = input()
    print(player_name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")

def make_guess():
    guesses_taken = 0
    while guesses_taken < 6:
        time.sleep(.25)
        guess_input = input("Guess: ")
        try:
            guess_num = int(guess_input)

            if 200 >= guess_num >= 1:
                guesses_taken += 1
                if guesses_taken < 6:
                    if guess_num < num:
                        print("The guess of the number that you have entered is too low")
                    if guess_num > num:
                        print("The guess of the number that you have entered is too high")
                    if guess_num != num:
                        time.sleep(.5)
                        print("Try Again!")
                if guess_num == num:
                    break
            if guess_num > 200 or guess_num < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:
            print("I don't think that " + guess_input + " is a number. Sorry")

    if guess_num == num:
        guesses_taken = str(guesses_taken)
        print('Good job, ' + player_name + '! You guessed my number in ' + guesses_taken + ' guesses!')

    if guess_num != num:
        print('Nope. The number I was thinking of was ' + str(num))

play_again = "yes"
while play_again == "yes" or play_again == "y" or play_again == "Yes":
    welcome_message()
    make_guess()
    print("Do you want to play again? (yes/no or y/n)")
    play_again = input()
