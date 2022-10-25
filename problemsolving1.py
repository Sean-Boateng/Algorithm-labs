# Task 1

# Declare a variable called favorite_number and store your favorite or lucky number within it. 
# Take a screenshot of your code that includes the file name/tab, line numbers, and code.
# Exclude the explorer sidebar
# Send the screenshot to your instructor chat channel.


# Task 2 
# Declare a variable called favorite_number and store your favorite or lucky number within it. 
# Use the random module to generate a random number between a range that includes your favorite number.
# Determine how many numbers away the random number was from your favorite number
# Send a screenshot of your completed code to your instructor chat channel.


# Task 3
# Create a while loop that generates a random number and checks if it matches your favorite number.
# Keep track of how many times the computer has guessed.
# Once the computer guesses the correct number, display a message explaining how many attempts it took the computer to guess your favorite number.

favorite_number = 3



 
import random

def random_numb():
    match = True
    counter = 0
    while True:
        counter += 1
        random_pick = random.randint(0,10)
        print(random_pick)
        difference = random_pick - favorite_number 
        difference = str(difference)
        if random_pick == favorite_number:
            counter = str(counter)
            print("You guessed right!")
            print("It took "+ counter + " tries.")
            break
        
        elif random_pick > favorite_number:
            print("Too much. You are " + difference + " above the number. Try again")
                
        elif random_pick < favorite_number:
            print("You are "  + difference + " under the number")
        
            

testing = random_numb()


