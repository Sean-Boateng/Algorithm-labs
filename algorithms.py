#Cloned down repo using the terminal
#cd into the new folder
#run the git commands


# Declare a variable called favorite_number and store your favorite or lucky number within it. 
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


