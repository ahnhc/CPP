# 코딩 문제 1번

print("Hello AIM!")

# 코딩 문제 2번

a = 4
star = '*'
blank = ' '
star_start = 1

for i in range(a,0,-1):
    print(blank * (i-1) + star_start * star)
    star_start +=2
    if star_start == 5:
        print(blank * (i-2),"AIM")

# 코딩 문제 3번


