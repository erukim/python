# 2.1
# print(200,'+',300,'+',400,'=',900)

# 2.2
# width = 30
# height = 60
# print(width)
# print(height)

# 2.3
# width = 30
# height = 60
# area = width * height
# print("사각형의 면적 :", area)

# 2.4
# width = 40
# height = 20
# area = width * height / 2
# print("삼각형의 면적 :", int(area))

# 2.5
# base = int(input('정사각형의 밑변을 입력하시오 : '))
# area = base ** 2
# print('정사각형의 면적 :', area)

# 2.6
# print("1에서 10까지의 합 :", 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

# 2.7
# print('10! =', 1*2*3*4*5*6*7*8*9*10)

# 2.8
# print("a  n  a**n")
# for a in range(2, 7):
#     n = 2
#     print(a, n, a**n)

# 2.9
# print("섭씨  화씨")
# for celsius in range(0, 51, 10):
#     fahrenheit = (9/5) * celsius + 32
#     print(f"{celsius}  {fahrenheit:.1f}")

# 2.10
# celsius = int(input('섭씨온도를 입력하세요 : '))
# fahrenheit = (9/5) * celsius + 32
# print(f'섭씨 {celsius} 도는 화씨 {fahrenheit} 도 입니다.')

# 2.11
# fahrenheit = int(input("화씨 온도를 입력하세요: "))
# celsius = (fahrenheit - 32) * 5/9
# print("화씨", fahrenheit, '도는 섭씨', round(celsius,2), "도 입니다.")

# 2.12
# PI = 3.141592
# radius = 11
# circumference = 2 * PI * radius
# area = PI * radius ** 2
# print("원의 반지름 =", radius, ", 원의 둘레 =", circumference, ", 원의 면적 =", area)

# 2.13
# PI = 3.141592
# radius = float(input("원의 반지름을 입력하세요 : "))
# circumference = 2 * PI * radius
# area = PI * radius ** 2
# print("원의 둘레 = ", circumference, ", 원의 면적 = ", area)

# 2.14
# for i in range(1, 11):
#     sqrt_i = i ** 0.5
#     print(f"{i}의 제곱근: {sqrt_i}")

# 2.15
# import math
# a = int(input("밑변을 입력하세요: "))
# b = int(input("높이를 입력하세요: "))
# c = math.sqrt(a**2 + b**2)
# print("빗변의 길이:", c)

# 2.16
# z = 1 + 2j
# rotated_z = z * (0 + 1j)
# print("회전하기 전 :", z)
# print("90도 회전한 후 :", rotated_z)

# 2.17
# import cmath
# coord = complex(1, 2)
# print("회전하기 전 :", coord)
# angle = cmath.pi / 6
# rotated = coord * cmath.exp(angle * 1j)
# print("30도 회전한 후 :", rotated)
