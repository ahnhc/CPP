# sum from 1 to 10

# i = 1
# sum = 0
# while i <= 10:
#     sum+=i
#     i+=1
# print("sum = ",sum)

# While statement with else

# i = 0
# while i < 3:
#     print(i,"Inside a loop")
#     i+=1
# else:
#     print("else part")

# Sum up nums as many as you want

# total = 0
# answer = "y"
#
# while answer == "y":
#     number = int(input("enter the number : "))
#     total+=number
#     answer = input("continue? (y / n) : ")
# print(f"Total sum is : {total}")

# exercise : math test

# import random
# Flag = True
# score = 0
# while Flag:
#     x = random.randint(1,100)
#     y = random.randint(1,100)
#     answer = int(input(f"{x} + {y} = "))
#     if answer == x+y:
#         print("Correct!")
#         score+=1
#     else:
#         print("Wrong!")
#         Flag = False
#         print(f"Your score is {score}")

# exercise : login program

# password = ""
# while password != "python is fun":
#     password = input("Enter your password : ")
# print("Login Successfully!")

# exercise : guessing random number

# import random
# flag = True
# failed = 0
# number = random.randint(1, 10)
# while flag:
#     entered = int(input("Enter your guess(number): "))
#     if number < entered:
#         print("Down!")
#         failed += 1
#     elif number > entered:
#         print("Up!")
#         failed+=1
#     else:
#         print(f"Congratulation. The # of attempts = {failed}")
#         print(f"The answer is {number}")
#         Flag = False
#         number = random.randint(1, 10)
#         failed = 0

# Nested loops
