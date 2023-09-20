import math
figure = str(input())
area = 0
if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    r = float(input())
    area = math.pi * r * r
elif figure == "triangle":
    lenght = float(input())
    height = float(input())
    area = (lenght * height) / 2
print(f"{area:.3f}")