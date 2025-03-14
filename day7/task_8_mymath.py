
import math

#mymath.py 파일 생성
# 삼각형 넓이 = 1/2 * 밑변 * 높이
def triangle_area(base, height):
    return 0.5 * base * height

# 원의 넓이 = 파이 * 반지름^2
def circle_area(radius):
    return math.pi * radius **2

# 직육면체의 넓이 = 2*(높이*가로 + 가로*세로 + 세로*높이)
def rec_area(length, width, height):
    return 2 * (length * width + width * height + height * length)