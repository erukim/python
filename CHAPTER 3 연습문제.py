# 3.1
# (1) False
# (2) False
# (3) True
# (4) True
# (5) False
# (6) True
# (7) True
# (8) False
# (9) True
# (10) True
# (11) False
# (12) True
# (13) True
# (14) True
# (15) True
# (16) False

# 3.2
# name = input("이름을 입력하시오 : ")
# height = int(input("키를 입력하시오(단위 cm) : "))
# if height < 140:
#     print(name, "님은 놀이기구를 탈 수 없습니다.")
# else:
#     print(name, "님은 놀이기구를 탈 수 있습니다.")

# 3.3
# age = int(input('나이를 입력하시오 : '))
# height = int(input('키를 입력하시오 : '))
# if age >= 19 and height >= 150:
#     print('입장할 수 있습니다.')
# else:
#     print('입장할 수 없습니다.')

# 3.4
# age = int(input("나이를 입력하시오 : "))
# if age >= 20:
#     print("Adult")
# elif age >= 10 and age < 20:
#     print("Youth")
# else:
#     print("Kid")

# 3.5
# num1, num2 = map(int, input("두 정수를 입력하시오 : ").split())
# if num1 < num2:
#     small_num = num1
#     big_num = num2
# else:
#     small_num = num2
#     big_num = num1
# print(small_num, big_num)

# 3.8
# x, y = map(int, input("점의 좌표 x, y를 입력하시오 : ").split())
# if x > 0 and y > 0:
#     print("1사분면에 있음")
# elif x < 0 and y > 0:
#     print("2사분면에 있음")
# elif x < 0 and y < 0:
#     print("3사분면에 있음")
# else:
#     print("4사분면에 있음")

# 3.9
# num = int(input("정수를 입력하시오: "))
# if num % 2 == 0:
#     div2 = True
# else:
#     div2 = False
# if num % 3 == 0:
#     div3 = True
# else:
#     div3 = False
# if div2:
#     print(f"{num}는(은) 2(으)로 나누어집니다.")
# else:
#     print(f"{num}는(은) 2(으)로 나누어지지 않습니다.")
# if div3:
#     print(f"{num}는(은) 3(으)로 나누어집니다.")
# else:
#     print(f"{num}는(은) 3(으)로 나누어지지 않습니다.")
# if div2 and div3:
#     print(f"{num}는(은) 2와(과) 3 모두로 나누어집니다.")
# else:
#     print(f"{num}는(은) 2와(과) 3 모두로 나누어지지 않습니다.")
