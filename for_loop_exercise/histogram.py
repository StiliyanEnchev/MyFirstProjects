count_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for num in range(count_numbers):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif current_num < 400:
        p2 += 1
    elif current_num < 600:
        p3 += 1
    elif current_num < 800:
        p4 += 1
    elif current_num >= 800:
        p5 += 1
p1_percentage = p1 / count_numbers * 100
p2_percentage = p2 / count_numbers * 100
p3_percentage = p3 / count_numbers * 100
p4_percentage = p4 / count_numbers * 100
p5_percentage = p5 / count_numbers * 100
print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")