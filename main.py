#!/usr/bin/env python3
# Eventually make a Flashcard App.
# Be as abusive as possible.
# Add more controls and functionality.
# Keep "score".
# Add in multiple controls and score tracking.

import random

def main():
    while True:
        x = random.randint(9, 100)
        y = random.randint(9, 100)
        selection = input("Type \'END\' or \'I QUIT\' to stop being asked questions. Otherwise, push ENTER to continue.: ")
        if selection in {"END", "I QUIT"}:
            print("Way to take the easy way out. It's only simple math!")
            quit()

        while x + y >= 100:
            x = random.randint(9, 100)
            y = random.randint(9, 100)
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print("The answer has 3 digits, and you are probably stupid, so hopefully you get an easier question.")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
        else:
            print("The first number is ", x)
            print("The second number is ", y)
            answer = int(input("What is the sum of the first number and the second number? "))
            if answer == x + y:
                print("You got the right answer!")
            else:
                print("Learn how to add idiot.")



'''
def start_selection():
    print("Please choose your difficulty.")
    print("Enter 1 if you want numbers between 1 and 10.")
    print("Enter 2 if you want numbers between 1 and 100.")
    #difficulty = input("Please enter your desired difficulty: ")
'''

main()
