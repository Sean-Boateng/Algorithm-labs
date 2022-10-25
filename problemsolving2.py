# Task 1: Reverse a String
# (HINT: Review the Algorithms + Problem Solving Lecture!)
# Write code that takes a string as input and returns the string reversed
# i.e. “Hello” will be returned as “olleH”


# def reverse_string():
#     user_input = input("What is your name?")[::-1]
#     print(user_input)

# task1 = reverse_string()



# Task 2: Capitalize a Letter

# Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”


# def capital():
#     user_input =input("WHat is your fav phrase?")
#     result = user_input.title()
#     print(result)

# task2 = capital()


# Task 3: Palindrome
# A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	


# Write code that takes a user input and checks to see if it is a Palindrome and reports the result




def palindrome():
    user_input = input("Give me an example of a palindrome.")
    user_input = user_input.upper()
    if user_input == user_input[::-1]:
        print("It is correct.")
    else:
        print("That is not correct.")

    
   

task3 = palindrome()







