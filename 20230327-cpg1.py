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


