# convert temperature

def menu():
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. End")
    select = int(input("Choose a menu : "))
    return select
def ctf(c):
    temp = c*9/5 +32
    return temp
def ftc(f):
    temp = (f-32)*5/9
    return temp
def input_f():
    f = int(input("Enter the temperature in degrees Fahrenheit : "))
    return f
def input_c():
    c = int(input("Enter the temperature in degrees Celcius : "))
    return c
def main():
    while True:
        index = menu()
        if index == 1:
            t = input_c()
            t2 = ctf(t)
            print("Fahrenheit temp = ",t2,"\n")
        elif index == 2:
            t = input_f()
            t2 = ftc(t)
            print("Celcius temp = ",t2,"\n")
        else:
            break
main()

