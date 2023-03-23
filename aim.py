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

star = '*'
dot = '.'
print(star * 18, "AIM" ,star * 17)

major_list = ["컴퓨터공학부       ","바이오메디컬소프트웨어","","","",""]
classof_list = ["22학번","23학번","","","",""]
mbti_list = ["ISTP","ENTJ","INFP","ENFP","ENFJ","ISFP"]
name_list = ["강유정","안형찬","윤지오","정상윤","최예지","최하나"]


for i in range (6):
    print(star, i+1,dot,major_list[i],classof_list[i],mbti_list[i],name_list[i],star)
    i+=1
    
print(star * 40)