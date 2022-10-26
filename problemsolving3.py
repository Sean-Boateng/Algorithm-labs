# Write a method that determines if a number is happy or sad

# def happy_number(s):
#     squaresum = set()
#     while s != 1:
#         s = sum(int(i)**2 for i in str(s))
#         if s in squaresum:
#             return False
#         squaresum.add(s)
#     return True


# print(happy_number(7))
# print(happy_number(400))


# Task 2: Prime Numbers
# A prime number is a number that is only divisible by one and itself.
# Write a method that prints out all prime numbers between 1 and 100 

# def prime_numbers():
#     for s in range(2, 101):
#         prime = True
#         for i in range(2, s):
#             if (s % i == 0):
#                 prime = False
#         if prime:
#             print(s)

   
# task2 = prime_numbers()


# def even_number():
#     for s in range(0 , 100):
#         if (s % 2==0):
#             print(s)
#         else:
#             continue

# testing= even_number()



# Task 3: Fibonacci
# A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Write a method that does the Fibonacci sequence starting at 1


a = 1
b = 2
n = 20
series = [1,1]
for x in range(2 , n):
    next = series[x - 1] + series[x - 2]
    series.append(next)

print(series)