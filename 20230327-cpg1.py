# Bundle code

# function < object < module

# function : 특정 작업을 위해 만든 명령어 모음
# 반복되는 동일한 작업이 필요할 때 function을 사용함

# def function name(parameter1, parameter2):
#   statement1
#   statement2

# def get_area(radius):
#     area = 3.14*radius**2
#     return area
# rad = int(input("radius? : "))
# result = get_area(rad)
# print(f"Area of a circle with radius {rad} = {result}")

# exercise : multiple arguments

# def get_sum(start,end):
#     sum = 0
#     for i in range(start,end+1):
#         sum+=i
#     return sum
# result = get_sum(1,10)
# print("get_sum(1,10) =",result)

# Function parameters can have default values.
# def greet(name, msg="how are you?"):
#     print(name + ", " + msg)
# greet("Anna")

# def greet(name, msg="how are you?"):
#     print(name + ", " + msg)
# greet("Anna","Welcome!")

# printPattern
# def printPattern(rows, char="A"):
#     for i in range(rows):
#         for j in range(rows):
#             print(char, end="")
#         print()
#
# printPattern(5)
# printPattern(5,"B")
# 새롭게 값을 넣어주면 그 값으로 출력된다.
# 기본 파라미터 값은 항상 넣어주어야 한다.

# def sub(x,y,z):
#     print("x=",x,"y=",y,"z=",z)
# sub(10,20,30)
# sub(x=10,y=20,z=30)
# sub(y=10,x=20,z=30)
# sub(10,y=20,z=30)

# sub(x=10,y=20,30) 이 명령은 오류를 출력함
# positional argument follows keyword argument

# Return multiple values

# def get_input():
#     return 2,3
# x,y = get_input()
# print(x)
# print(y)

# Quiz : why does it have an error?

# result = get_area(3)
# print("Area of aim-3주차 circle with radius 3 =",result)
# def get_area(radius):
#     area = 3.14 * radius**2
#     return area

# get_area is not defined
# result 항이 def 함수 이후에 나와야 한다.

# def main() :
#     result1 = get_area(3)
#     print("Area of aim-3주차 circle with radius 3=", result1)
# def get_area(radius):
#     area = 3.14*radius**2
#     return area
# main()

# 함수 안에는 아직 정의되지 않은 함수를 넣어도 괜찮음

# def sub():
#     pass

# pass를 하면 함수 안에 내용을 넣기전에 정의해둘 수 있다.

# asterisk (*)

# def varfunc(*args ):
#     print (args)
#
# print("Call with one value")
# varfunc(10)
#
# print("Call with multiple values")
# varfunc(10, 20, 30)

# def add(*args):
#     print(type(args))
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
#
# result1 = add(10)
# result2 = add(10, 20, 30)
# print(result1)
# print(result2)

# data types : tuple - 내부 원소의 내용을 바꿀 수 없다.

# def name_list(**kwargs):
#     result = ""
#     for kind, name in kwargs.items():
#         print(kind + " is " + name)
#         result += name
#     return result
#
# msg = name_list(first_name="gildong", last_name="Hong")
# print(msg)

# unpacking with the * operator

# alist = [1,2,3]
# print(alist)
# print(*alist)
# print(sum(*alist))

# def fruit_feature(fruit,color):
#     print(fruit + " is " + color)
# dic = {"fruit":"apple","color":"red"}
# fruit_feature(**dic)
# dic2 = {"fruit":"banana","color":"yellow"}
# fruit_feature(**dic2)

# def sum(aim-3주차,b,c):
#     print(aim-3주차+b+c)
# alist = [1,2,3]
# print(sum(*alist))

# 이거 오류 아닌가요?

# lambda function

# lambda argument : formula

# def func1(x):
#     return x+10
# func2 = lambda x:x+10
# result = func1(2)
# print(result)
# result = func2(2)
# print(result)