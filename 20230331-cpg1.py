# convert temperature
import locale

# def menu():
#     print("1. Celcius to Fahrenheit")
#     print("2. Fahrenheit to Celcius")
#     print("3. End")
#     select = int(input("Choose a menu : "))
#     return select
# def ctf(c):
#     temp = c*9/5 +32
#     return temp
# def ftc(f):
#     temp = (f-32)*5/9
#     return temp
# def input_f():
#     f = int(input("Enter the temperature in degrees Fahrenheit : "))
#     return f
# def input_c():
#     c = int(input("Enter the temperature in degrees Celcius : "))
#     return c
# def main():
#     while True:
#         index = menu()
#         if index == 1:
#             t = input_c()
#             t2 = ctf(t)
#             print("Fahrenheit temp = ",t2,"\n")
#         elif index == 2:
#             t = input_f()
#             t2 = ftc(t)
#             print("Celcius temp = ",t2,"\n")
#         else:
#             break
# main()

# local and global variables

# def func():
#     x = 100
#     print(x)
# func()

# gx = 100
# def func1():
#     print(gx)
# def func2():
#     gx = 200
#     print(gx)
# print(gx)
# func1()
# func2()

# global gx 설정

# gx = 100
# def func1():
#     print(gx)
# def func2():
#     global gx
#     gx = 200
#     print(gx)
# func1()
# func2()
# print(gx)

# simple calculator

# def menu():
#     print("1. add")
#     print("2. sub")
#     print("3. reset")
#     print("4. End")
#     select = int(input("Choose a menu : "))
#     return select
# def add():
#     num = int(input("What number do you want to add? : "))
#     global total
#     total+=num
#     print("Total after adding",num,"is",total)
# def sub():
#     num = int(input("What number do you sub?"))
#     global total
#     total-=num
#     print("Total after substracting",num,"is",total)
# def reset():
#     global total
#     total = 0
#     print("Reset! Total =",total)
# total = 0
# print("##### Calculator #####")
# print("Total : ",total)
# while True:
#     index = menu()
#     if index == 1:
#         add()
#     elif index == 2:
#         sub()
#     elif index == 3:
#         reset()
#     else:
#         break

# Lambda function

# print((lambda x : x*3)(10))
# func = lambda x : x**3

# print(func(2))
# func = lambda x, y : x+y

# result = func(2,3)
# print(result)

# score = lambda x: "Pass" if x >=80 else "Fail"
# print(score(87))

# normal python vs lambda function
# def abc(num):
#     num*=3
#     print(num)
# abc(10)

# print((lambda x:x*3)(10))

# def func(num):
#     num **=3
#     print(num)
# func(2)
#
# func = lambda x:x**3
# print(func(2))

# def func(x):
#     return x+10
# result = func(2)
# print(result)
#
# func = lambda x : x+10
# result = func(2)
# print(result)

# def func(x,y):
#     sum = x+y
#     print(sum)
# func(11,22)
#
# func = lambda x,y : x+y
# sum = func(11,22)
# print(sum)

# map : map(function,iterable data type)

# mylist = [1.1,2.2,3.3]
# result = list(map(int,mylist))
# print(result)
#
# mylist = [1,2,3,4,5]
# def add_one(x):
#     return x+1
# result = []
#
# # normal python function
# for i in mylist:
#     result.append(i+1)
# print(result)

# map function
# result_2 = list(map(add_one,mylist))
# print(result_2)
#
# mylist = [1,2,3,4,5]
# def double(x):
#     return x*2
#
# result =[]
# for i in mylist:
#     result.append(i*2)
# print(result)

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = list(map(lambda x: x**2, myList))
# print(result)
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 4, 6, 8, 10]
# print(list(map(lambda x, y: x * y, list1, list2)))
#
# mylist = range(1,10)
# result = list(map(lambda x: x**2,mylist))
# print(result)
#
# mylist = range(1,10)
# result = list(map(lambda x:x**2,mylist))
# print(result)

# def game369():
#     var=[]
#     for x in range(1,11):
#         if x%3==0:
#             var.append("clap")
#         else:
#             var.append(x)
#     print(var)
# game369()
#
# game369 = list(map(lambda x: "clap" if x%3 ==0 else x,range(1,11)))
# print(game369)