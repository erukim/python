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
# numbers = input("두 정수를 입력하시오: ")
# num1 = int(numbers[:numbers.find(' ')])
# num2 = int(numbers[numbers.find(' ')+1:])
# if num1 < num2:
#     small_num = num1
#     big_num = num2
# else:
#     small_num = num2
#     big_num = num1
# print(small_num, big_num)

# 3.6
# a, b, c = input("세 정수를 입력하시오 : ").split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a <= b and a <= c:
#     print(a, end=" ")
#     if b <= c:
#         print(b, c)
#     else:
#         print(c, b)
# elif b <= a and b <= c:
#     print(b, end=" ")
#     if a <= c:
#         print(a, c)
#     else:
#         print(c, a)
# else:
#     print(c, end=" ")
#     if a <= b:
#         print(a, b)
#     else:
#         print(b, a)

# 3.7
# score = int(input("게임점수를 입력하시오 : "))
# if score >= 1000:
#     print("고수입니다.")
# else:
#     print("입문자입니다.")

# 3.8
# x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
# x = int(x)
# y = int(y)
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

# 3.10
# a, b = input("두 정수를 입력하시오 : ").split()
# a = int(a)
# b = int(b)
# if a % b == 0:
#     print(str(a) + "(은)는 " + str(b) + "의 배수입니다.")
# else:
#     print(str(a) + "(은)는 " + str(b) + "의 배수가 아닙니다.")

# 3.11
# numbers = input("세 복권번호를 입력하시오 : ").split()
# if numbers[0] == '2' and numbers[1] == '3' and numbers[2] == '9':
#     print("상금 1억 원")
# elif numbers.count('2') + numbers.count('3') + numbers.count('9') == 2:
#     print("상금 1천만 원")
# elif numbers.count('2') + numbers.count('3') + numbers.count('9') == 1:
#     print("상금 1만 원")
# else:
#     print("다음 기회에...")

# 3.12
# import math
# x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
# x, y = int(x), int(y)
# distance = math.sqrt(x**2 + y**2)
# if distance <= 5:
#     print("원의 내부에 있음")
# else:
#     print("원의 외부에 있음")

# 3.13
# x, y = input("점의 좌표 x, y를 입력하시오 : ").split()
# x, y = int(x), int(y)
# distance = ((x-3)**2 + (y-4)**2)**0.5
# if distance <= 10:
#     print("원의 내부에 있음")
# else:
#     print("원의 외부에 있음")

# 3.14
# char = input("알파벳을 입력하시오 : ")
# if char in ['a', 'e', 'i', 'o', 'u']:
#     print(char, "(은)는 모음입니다.")
# else:
#     print(char, "(은)는 자음입니다.")
